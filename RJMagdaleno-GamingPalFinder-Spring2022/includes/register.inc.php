<?php

if(isset($_POST["submit"]))
{
	
	$username = $_POST["username"];
	$email = $_POST["email"];
	$password = $_POST["password"];
	$pswdRepeat = $_POST["pswdRepeat"];
	$game1 = $_POST["game1"];
	$game2 = $_POST["game2"];
	$game3 = $_POST["game3"];
	
	require_once 'dbh.inc.php';
	require_once 'functions.inc.php';
	
	if(emptyInputSignup($username, $email, $password, $pswdRepeat, $game1, $game2, $game3) !== false)
	{
		header("location: ../templates/register.php?error=emptyinput");
		exit();
	}
	if(invalidUsername($username) !== false)
	{
		header("location: ../templates/register.php?error=invalidusername");
		exit();
	}
	if(invalidEmail($email) !== false)
	{
		header("location: ../templates/register.php?error=invalidemail");
		exit();
	}
	
	if(pswdMatch($password, $pswdRepeat) !== false)
	{
		header("location: ../templates/register.php?error=pswdDontMatch");
		exit();
	}
	if(usernameExists($conn, $username, $email) !== false)
	{
		header("location: ../templates/register.php?error=usernameTaken");
		exit();
	}
	if(gameMatch($game1, $game2, $game3) !== false)
	{
		header("location: ../templates/register.php?error=repeatGame");
		exit();
	}
	
	createUser($conn, $username, $email, $password, $game1, $game2, $game3);
	
}
else
{
	header("location: ../templates/register.php");
	exit();
}