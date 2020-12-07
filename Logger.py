'''
HOPE YOU LIKE IT,
	ISHAAN

'''


'''
Importing all the necessary libraries
'''
import os 		
import csv
import time
import datetime 
import calendar
import pyautogui


'''
Creating a function to find what day of the week it is
'''
def findDay(date): 
    day = datetime.datetime.strptime(date, '%Y %m %d').weekday() 
    return (calendar.day_name[day]) 



def main(codenum,pwd=None):

	os.startfile('C:\\Users\\rakhe\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe') #ENTER THE PATH TO ZOOM.EXE FILE(Read Description for more details)

	joinbutton = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Join.png') #The primary join button
	
	while joinbutton == None:	#Searching for the join button

		joinbutton = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Join.png') 

		if joinbutton != None:	#Breaking the loop once it finds the button
			break

	#join
	pyautogui.click(joinbutton)	#Moving to the button

	#typemeeting

	code = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Code.png')
	while code == None :

			code = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Code.png')

			if code != None:
				break


	pyautogui.write(codenum)

	#clickjoin

	join2 = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\JoinCode.png')

	while join2 == None:
		join2 = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\JoinCode.png')

		if join2 != None:
			break

	pyautogui.click(join2)

	if pwd != None:
		passw = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Pwd.png')

		while passw == None:
			passw = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\Zoom\\Pwd.png')

			if passw != None:
				break

		pyautogui.click(passw)
		pyautogui.write(pwd)


#Finding what day it is

date = str(datetime.date.today()).replace('-', ' ')
day = findDay(date)


'''
Opening our timetable according to our day
'''
file = open(f'{os.getcwd()}\\Zoom\\{day[:3]}.csv')

csv_format = csv.reader(file)			#Using the csv module to open the file

data = list(csv_format)[1:]				#Converting the data into a list

timecode = {}

codepwd = {}
	
for sublists in data:
	if len(sublists) != 0:
		timecode[sublists[0]] = sublists[1]
		codepwd[sublists[0]] = sublists[2]

timecode['match'] = []

'''


PILING ALL UP TOGETHER


'''
while True:
	time.sleep(1)	#To prevent overuse of CPU
	t = datetime.datetime.now().strftime("%H:%M")	#Getting current time and trying to update it again and again
	if (t in timecode) & (t not in timecode['match']):
	      timecode['match'].append(t)
	      print(f'Logging in for the {t} class.')
	      f = open('LogRecord.txt','a')
	      f.write(f'Date: {datetime.date.today()}, Day: {day}: Logged in for the {t} class.\n')
	      f.close()
	      main(timecode[t], codepwd[t])