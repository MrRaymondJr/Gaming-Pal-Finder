      </div>
    </main>
    <footer>
	  <p>
	    <a href="index.php">Home</a>
		<a href="about.php">About Us</a>
		<?php
		    if(isset($_SESSION["id"]))
			{
				echo "<a href='matches.php'>Matches</a>";
		        echo "<a href='../includes/logout.inc.php'>Logout</a>";
			}
			else
			{
				echo "<a href='login.php'>Login</a>";
		        echo "<a href='register.php'>Register</a>";
			}
		  ?>
	    <br>Copyright &copy; Gaming Pal Finder 2022<br>rjmagdaleno@csu.fullerton.edu
	  </p>
	  
    </footer>
  </body>
</html>