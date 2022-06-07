<?php

function emptyInputSignup($username, $email, $password, $pswdRepeat, $game1, $game2, $game3)
{
	$result;
	if(empty($username) || empty($email) || empty($password) || empty($pswdRepeat) || empty($game1) || empty($game2) || empty($game3))
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function invalidUsername($username)
{
	$result;
	if(!preg_match("/^[a-zA-Z0-9]*$/", $username))
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function invalidEmail($email)
{
	$result;
	if(!filter_var($email, FILTER_VALIDATE_EMAIL))
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function pswdMatch($password, $pswdRepeat)
{
	$result;
	if($password != $pswdRepeat)
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function gameMatch($game1, $game2, $game3)
{
	$result;
	if($game1 == $game2 || $game2 == $game3 || $game3 == $game1)
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function createUser($conn, $username, $email, $password, $game1, $game2, $game3)
{
	$sql = "INSERT INTO player (username, email, password) VALUES (?, ?, ?);";
	$stmt = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($stmt, $sql))
	{
		header("location: ../templates/register.php?error=stmtfailed");
		exit();
	}
	
	$hashedPswd = password_hash($password, PASSWORD_DEFAULT);
	
	mysqli_stmt_bind_param($stmt, "sss", $username, $email, $hashedPswd);
	mysqli_stmt_execute($stmt);
	
	createUser_Games($conn, $username, $game1);
	createUser_Games($conn, $username, $game2);
	createUser_Games($conn, $username, $game3);
	
	header("location: ../templates/register.php?error=none");
	exit();
}

function createUser_Games($conn, $username, $game)
{
	$sql1 = "SELECT id FROM player WHERE username = ?;";
	$sql2 = "SELECT id FROM games WHERE gameName = ?;";
	$sql3 = "INSERT INTO player_games (userId, gameId) VALUES (?, ?);";
	
	$stmt1 = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($stmt1, $sql1))
	{
		header("location: ../templates/register.php?error=stmtfailed");
		exit();
	}
	mysqli_stmt_bind_param($stmt1, "s", $username);
	mysqli_stmt_execute($stmt1);
	$result = mysqli_stmt_get_result($stmt1);
	$uid = mysqli_fetch_assoc($result);
	
	
	$stmt2 = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($stmt2, $sql2))
	{
		header("location: ../templates/register.php?error=stmtfailed");
		exit();
	}
	mysqli_stmt_bind_param($stmt2, "s", $game);
	mysqli_stmt_execute($stmt2);
	$result = mysqli_stmt_get_result($stmt2);
	$gid = mysqli_fetch_assoc($result);
	
	
	$stmt3 = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($stmt3, $sql3))
	{
		header("location: ../templates/register.php?error=stmtfailed");
		exit();
	}
	mysqli_stmt_bind_param($stmt3, "ii", $uid['id'], $gid['id']);
	mysqli_stmt_execute($stmt3);
}

function emptyInputLogin($username, $password) 
{
	$result;
	if(empty($username) || empty($password))
	{
		$result = true;
	}
	else
	{
		$result = false;
	}
	return $result;
}

function usernameExists($conn, $username, $email)
{
	$sql = "SELECT * FROM player WHERE username = ? OR email = ?;";
	$stmt = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($stmt, $sql))
	{
		header("location: ../templates/register.php?error=stmtfailed");
		exit();
	}
	
	mysqli_stmt_bind_param($stmt, "ss", $username, $email);
	mysqli_stmt_execute($stmt);
	
	$resultData = mysqli_stmt_get_result($stmt);
	
	if($row = mysqli_fetch_assoc($resultData))
	{
		return $row;
	}
	else
	{
		$result = false;
		return $result;
	}
	
	mysqli_stmt_close($stmt);
}

function loginUser($conn, $username, $password) 
{
	$usernameExists = usernameExists($conn, $username, $username);
	
	if($usernameExists === false)
	{
		header("location: ../templates/login.php?error=wronglogin");
		exit();
	}
	
	$pswdHashed = $usernameExists["password"];
	$checkPswd = password_verify($password, $pswdHashed);
	
	if($checkPswd === false)
	{
		header("location: ../templates/login.php?error=wronglogin");
		exit();
	}
	else if($checkPswd === true)
	{
		session_start();
		$_SESSION["id"] = $usernameExists["id"];
		$_SESSION["username"] = $usernameExists["username"];
		header("location: ../templates/index.php");
		exit();
	}
}