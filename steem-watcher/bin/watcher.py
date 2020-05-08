#!/usr/bin/python3
#encoding:UTF-8
import json, os, sys, time
from contextlib import suppress
from concurrent import futures
from steem.blockchain import Blockchain
from steem.steemd import Steemd
import pymysql


env_dist = os.environ
steemd_url = env_dist.get('STEEMD')
if steemd_url == None:
    steemd_url = 'https://api.steemit.com'
print('STEEMD: %s' % steemd_url)

watch_account = env_dist.get('WATCH_ACCOUNT')
if watch_account == None:
    watch_account = 'steem'
print('WATCH_ACCOUNT: %s' % watch_account)

worker_num = env_dist.get('WORKER_NUM')
if worker_num == None:
    worker_num = 5
print('Worker num: %s' % (worker_num))
worker_num = int(worker_num)
env_block_num = env_dist.get('BLOCK_NUM')
if env_block_num == None:
    start_block_num = 0
else:
    start_block_num = int(env_block_num)

mysql_host = env_dist.get('MYSQL_HOST')
if mysql_host == None:
    mysql_host = '172.22.2.2'
print('MYSQL_HOST: %s' % (mysql_host))

mysql_user = env_dist.get('MYSQL_USER')
if mysql_user == None:
    mysql_user = 'root'
print('MYSQL_USER: %s' % (mysql_user))

mysql_pass = env_dist.get('MYSQL_PASS')
if mysql_pass == None:
    mysql_pass = '123456'
print('MYSQL_PASS: %s' % (mysql_pass))

steemd_nodes = [
    steemd_url,
]
s = Steemd(nodes=steemd_nodes)
b = Blockchain(s)
db_connection = None

def connect_db():
    global db_connection
    # Connect to the database
    try:
        db_connection = pymysql.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_pass,
            db='watcher',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except:
        print('mysql is not ready.')
        sys.exit()

def create_db():
    try:
        connection = pymysql.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_pass,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql = "CREATE DATABASE watcher";
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()
            print("Successfully added database")
        except:
            connection.rollback()
            print(sys.exc_info())
    except:
        print("MYSQL has not been ready.")
        sys.exit()
    finally:
        connection.close()

def create_table():
    try:
        connection = pymysql.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_pass,
            db='watcher',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        sql1 = '''
        CREATE TABLE `watcher`.`account_create_log` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `op_type` INT NOT NULL,
            `block_num` INT NOT NULL,
            `creator` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NOT NULL,
            `original_data` TEXT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NOT NULL,
            `timestamp` INT NOT NULL,
            PRIMARY KEY (`id`),
            INDEX `op_type_index` (`op_type`));
        '''
        sql2 = '''
        CREATE TABLE `watcher`.`task_log` (
            `block_num` INT NOT NULL,
            `status` INT NOT NULL,
            PRIMARY KEY (`block_num`));
        '''
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql1)
                cursor.execute(sql2)
            connection.commit()
            print("Successfully added table")
        except:
            connection.rollback()
            print(sys.exc_info())
    except:
        print("MYSQL has not been ready.")
        sys.exit()
    finally:
        connection.close()

def worker(start, end):
    global s, b, watch_account, db_connection
    print('start from {start} to {end}'.format(start=start, end=end))
    # keep log
    with db_connection.cursor() as cursor:
        sql = "INSERT INTO `task_log` (`block_num`, `status`) VALUES "
        data = []
        for i in range(start, end+1):
            data.append("(%s, 0)" % i)
        sql = sql + ','.join(data)
        # print(sql)
        cursor.execute(sql)
    db_connection.commit()
    # get block
    block_infos = s.get_blocks(range(start, end+1))
    # print(block_infos)
    sql = "INSERT INTO `account_create_log` (`op_type`, `block_num`, `creator`, `original_data`, `timestamp`) VALUES (%s, %s, %s, %s)"
    for block_info in block_infos:
        timestamp = int(time.mktime(time.strptime(block_info['timestamp'], "%Y-%m-%dT%H:%M:%S")))
        block_num = block_info['block_num']
        transactions = block_info['transactions']
        for trans in transactions:
            operations = trans['operations']
            for op in operations:
                if op[0] == 'claim_account' and op[1]['creator'] == watch_account:
                    # op_type 1 = claim_account
                    with db_connection.cursor() as cursor:
                        cursor.execute(sql, (1, block_num, op[1]['creator'], json.dump(op), timestamp))
                    db_connection.commit()
                if op[0] == 'create_claimed_account' and op[1]['creator'] == watch_account:
                    # op_type 2 = create_claimed_account
                    with db_connection.cursor() as cursor:
                        cursor.execute(sql, (2, block_num, op[1]['creator'], json.dump(op), timestamp))
                    db_connection.commit()
                if op[0] == 'account_create' and op[1]['creator'] == watch_account:
                    # op_type 3 = account_create
                    with db_connection.cursor() as cursor:
                        cursor.execute(sql, (3, block_num, op[1]['creator'], json.dump(op), timestamp))
                    db_connection.commit()
    # keep log
    with db_connection.cursor() as cursor:
        sql = "UPDATE `task_log` SET `status` = 1 where block_num >= %s and block_num <= %s" % (start, end)
        cursor.execute(sql)
    db_connection.commit()

def run():
    global start_block_num
    steemd_nodes = [
        steemd_url,
    ]
    s = Steemd(nodes=steemd_nodes)
    b = Blockchain(s)

    create_db()
    create_table()
    connect_db()

    while True:
        head_block_number = b.info()['head_block_number']
        end_block_num = int(head_block_number)
        if start_block_num == 0:
            start_block_num = end_block_num - 3
        if start_block_num >= end_block_num:
            continue
        with futures.ThreadPoolExecutor(max_workers=worker_num) as executor:
            executor.submit(worker, start_block_num, end_block_num)
        start_block_num = end_block_num + 1
        #time.sleep(3)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()