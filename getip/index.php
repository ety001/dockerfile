<?php
/**
 * Get IP address visitor
 * @return string
 */
function getIP() 
{
    $ip = $_SERVER['REMOTE_ADDR'];
 
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) 
    {
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } 
    else if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) 
    {
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }
 
    return $ip;
}
header('Access-Control-Allow-Origin: *');
echo getIP();
