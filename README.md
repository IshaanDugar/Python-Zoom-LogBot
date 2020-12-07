# Python-Zoom-LogBot
There you have it, an auto-logger for your Zoom meetings.

### YOU MUST HAVE THE PYTHON LANGUAGE INSTALLED ON YOUR DEVICE FOR THIS TO WORK ALONG WITH ALL THE LIBRARIES.
### INSTALL PYTHON FROM https://python.org or https://www.anaconda.com/
### INSTALL LIBRARIES BY TYPING 'pip install module' where module is the name of the library in the command prompt.

Type:
pip install csv     - Hit enter and let it download then type:

pip install pyautogui   - again press enter and let it download

Now, for you to use it, follow these steps for setting up your bot successfully.
#### (If you wanna be lazy, you gotta do a little preparations beforehand)

From the 'Zoom' folder from this repository, you will find files like 'Mon.csv', 'Tue.csv'.etc.


Inside these, you have to fill the timings and code and passwords, in the form 

  TIME, CODE, PASSWORD
  
  12:30, 12345678, 'ABCDEFGH'
  
  09:40, 98765432, None 
  

### NOTE: If you do not have any password for your meeting, type "None" after the comma.


### FOR TIMINGS BEFORE 10 AM, Please add a '0' before the hour value, like '9:30' as '09:30' or it won't work

Then, your bot is almost just done.

You just need to start the bot by giving the path in the command prompt(like C:/Users/.... to the folder where the bot is located, you give type 'cd' before the path) or terminal and type:

## python Logger.py

And there you go, your bot has started!

So all you gotta do is to turn on your PC and then just type in the path and start the bot and what else?
Maybe chill out and relax.

#### (I will soon give instructions to make the bot fully automatic -- that is, it starts with your computer and logs in.)
