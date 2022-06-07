<?php
  include_once 'header.php'
?>
    <main>
      <h2>Register an Account</h2>
	  <p>Interested in becoming a member and making new friends? Fill in your information below to get started!</p>
	  <form action="../includes/register.inc.php" method="post">
	    <label for="username">Username</label>
		<input type="text" name="username" placehodler="Enter Username">
		<label for="username">Email</label>
		<input type="text" name="email" placehodler="Email">
		<label for="username">Password</label>
		<input type="password" name="password" placehodler="Password">
		<label for="username">Re-Password</label>
		<input type="password" name="pswdRepeat" placehodler="Repeat Password">
		<?php
          include_once 'games.php'
        ?>
		<br>
		<button type="submit" name="submit">Register</button>
	  </form>
	  <?php
	    if(isset($_GET["error"]))
		{
			if($_GET["error"] == "emptyinput")
			{
				echo "<p>Please fill in all fields!</p>";
			}
			else if ($_GET["error"] == "invalidusername")
			{
				echo "<p>Please enter a valid username!</p>";
			}
			else if ($_GET["error"] == "invalidemail")
			{
				echo "<p>Please enter a valid email!</p>"; 
			}
			else if ($_GET["error"] == "pswdDontMatch")
			{
				echo "<p>Please make sure both passwords are the same!</p>"; 
			}
			else if ($_GET["error"] == "stmtfailed")
			{
				echo "<p>Unexpected Error! Please try again!</p>";
			}
			else if ($_GET["error"] == "usernameTaken")
			{
				echo "<p>Username already taken! Please try again!</p>";
			}
			else if($_GET["error"] == "repeatGame")
			{
				echo "<p>Make sure each drop-down is a different game!</p>"; 
			}
			else if ($_GET["error"] == "none")
			{
				echo "<p>Successfuly registerd account!</p>"; 
			}
		}
	  ?>
	  
<?php
  include_once 'footer.php'
?>