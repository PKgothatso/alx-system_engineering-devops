#COMMAND LINE FOR THE WIN#

This README file is for the command line for the win project, the CMD CHALLENGE a cool game challenging you on BASH skills.Everything is done via the command line.

-Requirements:
General
A README.md file, at the root of the folder of the project, is mandatory
This project will be manually reviewed.
As each task is completed, the name of that task will turn green
Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format
Specific
In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

References :

SFTP Guide
SFTP File Transfer Tutorial
Here are the steps to follow:

Take the screenshots of the completed levels as mentioned in the general requirements.
Open a terminal or command prompt on your local machine.
Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
Once connected, navigate to the directory where you want to upload the screenshots.
Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.
NOTE :
The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/

-Tasks
the project has 3 advanced tasks

##Steps for png files transfer using SFTP##:

This project required the use of the SFTP (Secure File Transfer Protocol) command-line tool to transfer screenshots from a local machine to a sandbox environment. Here are the steps I followed:

1. *Take Screenshots*:
 I took screenshots of the completed levels as required by the project guidelines.

2. *Open Terminal*:
I opened a terminal on my local machine.

3. *Establish SFTP Connection*:
I used the SFTP command-line tool to establish a connection to the sandbox environment. The necessary hostname, username, and password were provided.

    sftp> username@hostname
    sftp > password: ************

4. *Navigate to Directory*:
Once connected, I navigated to the directory where I wanted to upload the screenshots.

   sftp> cd /root/alx-system_engineering-devops/command_line_for_the_win/

5. **Upload Screenshots**:
I used the SFTP 'put' with the '-p' flag command to upload the screenshots from my local machine to the sandbox environment.

  sftp> put -p "C:\\Users\\Accountname\\Pictures\\Screenshots\\0-first_9_tasks.png"
  sftp> put -p "C:\\Users\\Accountname\\Pictures\\Screenshots\\1-next_9_tasks.png"
  sftp> put -p "C:\\Users\\Accountname\\Pictures\\Screenshots\\2-next_9_tasks.png"

6. **Confirm Transfer**:
I confirmed that the screenshots had been successfully transferred by checking the sandbox directory.
   
  sftp> ls

7. **Exit SFTP**:
Lastly, I exited the SFTP connection.

  sftp> exit

This process ensured that the screenshots were successfully transferred to the sandbox environment before being pushed to GitHub.

