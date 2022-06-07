# Gaming-Pal-Finder
**Abstract** 
Many video game players suffer from antisocial behavior. Being afraid to communicate with fellow players hurts both the person and the gaming genre. This project, titled Gaming Pal Finder, aims to create the initial meeting point for friends by combining a website with a machine learning model. As users enter their top three favorite games and decide whether they like others based on their preferences, the model grows more robust and accurate. Utilizing a web application, database, and python machine learning model, this project plants a solid foundation for a viable product in the future.

# Instructions
**Installation**
The following applications are required to properly operate this project:
- XAMPP: Visit the website https://www.apachefriends.org, download the correct program version for your computer, and run the setup executable. Follow the instructions leaving all components selected and the installation folder as C:\xampp. Once downloaded, the modules should automatically select ports to be connected to. If those port(s) are already being used, you can change the connection by clicking the config button and changing the listen value in httpd.conf or port value in my.ini.
- Visual Studio Community: Visit the website https://visualstudio.microsoft.com/downloads, choose the free download for Visual Studio 2019/2022, and run the setup executable. In the workloads menu, it is recommended to select “Python development” and “Data storage and processing.” After finishing the installation, launch Visual Studio, create your environment, and navigate to “Continue without code.” Follow the steps at https://docs.microsoft.com/en-us/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-05-installing-packages?view=vs-2022 to ensure packages pandas, numpy, cloudpickle, pickleshare, matplotlib, matplotlib-inline, and mysql-connector-python are installed to be used for imports in the code.
- RJMagdaleno-GamingPalFinder-Spring2022: Copy the folder, follow path C:\xampp\htdocs, and paste the folder in that location. You may delete the other files in htdocs if desired. 
- GPF_Database.sql: Run the XAMPP application. Start Apache and MySQL. Open any web browser and enter http://localhost/phpmyadmin/ in the search bar. Select New from the list on the left. Enter “gamingpalfinder_database” with no quotations in the database name and press create. Select the new database from the left and switch to the SQL tab located at the top navigation bar. Find GPF_Database.sql in the RJMagdaleno-GamingPalFinder-Spring2022 folder and open it in a text editor like notepad. Copy all the code in the file and paste it into the textbox on the SQL page. Press the Go button. All queries should pass.
** Operating **
- Gaming Pal Finder website: Run the XAMPP application. Start Apache and MySQL. Open any web browser and enter http://localhost/ in the search bar. Click RJMagdaleno-GamingPalFinder-Spring2022/, then templates/ folder. Use the navigation links on the website to switch between web pages. Use register to create an account and login to log into the account. It is recommended to create an account on the website first, then use that account to log in. Once logged in, you can log out by pressing logout.
- CreateFinalDataset.py: Navigate through C:\xampp\htdocs\RJMagdaleno-GamingPalFinder-Spring2022\model\CreateFinalDataset and open CreateFinalDataset.sln in Visual Studio. In the code, you can edit the variable users on line 15 to change the size of the dataset. Press either F5 or Ctrl+F5 on your keyboard to run the application. Open …\model\CreateFinalDataset to review created datasets as .csv files. Close .csv files if you wish to rerun the project.
- ML-Model.py: Follow the steps from CreateFinalDataset.py above to create the .pkl files.  Copy GPF_numData.pkl and GPF_ratings.pkl from CreateFinalDataset and paste them inside …\model\ML-Model\ML-Model. Run the XAMPP application. Start Apache and MySQL. Open ML-Model.sln in Visual Studio inside …\model\ML-Model folder. Press either F5 or Ctrl+F5 on your keyboard to run the application. The first integer input is the id you wish to retrieve from the player table inside gamingpalfinder_database. The second integer input is added to the first to create a new, or access an old, id value used for the dataset. It is recommended to always use the dataset’s initial length from CreateFinalDataset.py for the second input. Open …\model\ML-Model\ML-Model to review updated datasets as .csv files. Close .csv files if you wish to rerun the project. Replace .pkl files if you wish to reset the data.
