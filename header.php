<?php
  session_start();
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
	<title>Gaming Pal Finder</title>
	<link rel="stylesheet" type="text/css" href="../css/style.css">
  </head>
  <body>
    <header>
	  <h1> Gaming Pal Finder </h1>
	</header>
	<nav>
	  <div class="wrapper">
	    <ul>
		  <li><a href="index.php">Home</a></li>
		  <li><a href="about.php">About Us</a></li>
		  <?php
		    if(isset($_SESSION["id"]))
			{
				echo "<li><a href='matches.php'>Matches</a></li>";
		        echo "<li><a href='../includes/logout.inc.php'>Logout</a></li>";
			}
			else
			{
				echo "<li><a href='login.php'>Login</a></li>";
		        echo "<li><a href='register.php'>Register</a></li>";
			}
		  ?>
		</ul>
	  </div>
	</nav>