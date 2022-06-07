<?php
  include_once 'header.php'
?>
    <main>
      <h2>Login</h2>
	  <p>Welcome back! Enter your username & password to be log into your account. Don't have an accoutn? Select the register button and create one!</p>
	  <form action="../includes/login.inc.php" method="post">
		<label for="username">Username/Email</label>
	    <input type="text" name="username" placehodler="Username/Email">
		<label for="password">Password</label>
		<input type="password" name="password" placehodler="Password"> <br>
		<button type="submit" name="submit">Log In</button>
	  </form>
	  <?php
	    if(isset($_GET["error"]))
		{
			if($_GET["error"] == "emptyinput")
			{
				echo "<p>Please fill in all fields!</p>";
			}
			else if ($_GET["error"] == "wronglogin")
			{
				echo "<p>Incorrect information! Please try again!</p>";
			}
		}
	  ?>
<?php
  include_once 'footer.php'
?>