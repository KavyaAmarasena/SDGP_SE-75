<?php

$dbhost = "lacalhost";
$dbuser = "root";
$dbpass = "";
$dbname = "Learnly_db";

if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname))
{
    die("failed to connect!");
}