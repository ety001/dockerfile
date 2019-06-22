<?php
$email = getenv('EMAIL');
$authkey = getenv('AUTH_KEY');
$domain = $_GET['domain'] ? $_GET['domain'] : null; // example.com
$record = $_GET['record'] ? $_GET['record'] : null; // sub.example.com
$ip = $_GET['ip'] ? $_GET['ip'] : null;
// $ip = file_get_contents('https://api.ipify.org');

if (!$email || !$authkey || !$domain || !$record || !$ip) {
    echo 'no config';
    return;
}

$headers = [ 
    'X-Auth-Email: '.$email,
    'X-Auth-Key: '.$authkey,
    'Content-Type: application/json'
];

$data = [
    'type' => 'A',
    'name' => $record,
    'content' => $ip,
    'ttl' => 1,
    'proxied' => false,
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://api.cloudflare.com/client/v4/zones?name=$domain");
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
if (curl_errno($ch)) {
    exit('Error: ' . curl_error($ch));
}
curl_close ($ch);

var_dump($result, 40);
$json = json_decode($result, true);

$ZoneID = $json['result'][0]['id'];

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://api.cloudflare.com/client/v4/zones/$ZoneID/dns_records?name=$record");
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
if (curl_errno($ch)) {
    exit('Error: ' . curl_error($ch));
}
curl_close ($ch);

var_dump($result, 58);
$json = json_decode($result, true);

$DNSID = $json['result'][0]['id'];

$old_ip = $json['result'][0]['content'];

if ($old_ip === $ip) {
    echo "CloudFlare IP: $old_ip" . PHP_EOL;
    echo "Current IP: $ip" . PHP_EOL;
    echo "The IP doesn't have to be changed!" . PHP_EOL;
}
else {
    echo "CloudFlare IP: $old_ip" . PHP_EOL;
    echo "Current IP: $ip" . PHP_EOL;
    echo "The IP has to be changed!" . PHP_EOL;
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, "https://api.cloudflare.com/client/v4/zones/$ZoneID/dns_records/$DNSID");
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");  
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        exit('Error: ' . curl_error($ch));
    }
    echo "The IP has changed from $old_ip to $ip!" . PHP_EOL;
    var_dump($result, 87);
}