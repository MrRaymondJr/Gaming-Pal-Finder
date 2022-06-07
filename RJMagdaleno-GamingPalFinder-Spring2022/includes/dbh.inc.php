<?php

$serverName = "localhost";
$dBUsername = "root";
$dBPassword = "";
$dBName = "gamingpalfinder_database";

$conn = mysqli_connect($serverName, $dBUsername, $dBPassword, $dBName);

if(!$conn)
{
	die("Connecton failed:" . mysqli_connect_error());
}