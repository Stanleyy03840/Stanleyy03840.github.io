

# Create Task Idea:
## Requirements:
* Input and an Output
* At least one list
* At least one procedure
* At least one algorithm

## Idea:
### health reporter
Using Javascript

#### Overview on Idea:
Calculates daily activities (can include the amount of time you watched movies) and notifies if you should take a break from the internet and go outside.

Input: user reports hours of sleep, hours of exercise, calorie intake, etc

Output: tells if the user is healthy. if unhealthy, tell the user how they can improve

List: values that the user inputs will be stored in a list

Procedure: if sleep < 8, and or if hours of exercise < 1, and or if calorie intake 2000, display unhealthy and give user suggestions about how to improve

Sequencing: First code asks for user input, then based on the information it receives it gives a specific output

Selection: If user inputs meet requirements, then they are labeled as 'healthy'

Iteration: repeats through questions until all questions are answered
PBL feature: we can also include aspects relating to screen time and time-watching movies. If the user inputs a large screentime amount, we will tell them to take a break and rest their eyes


# Create Task Responses:## 3a)
### i. Describes the overall purpose of the program
The purpose of this program is to survey people who are skeptible about their health lifestyles, and can get a better view of what habits to chane and what habits to keep going.

### ii. Describes what functionality of the program is demonstrated in the video
The program asks number of hours or frequency for some events, and yes or no questions to other events. 

### iii. Describes the input and output of the program demonstrated in the video
Input:
user inputs time since last annual checkup, time since last eye checkup, screen time, un/healthy diet, liters of water, exercise frequency, hours of sleep, frequency of drugs, alcohol, or smoking, yes/no signs of depression
Output:
if months since last checkup > 12, tells user to schedule annual checkup asap
if months since last eye checkup, tells user to schedule eye doctor appointment asap
if hours of screen time is greater than 8, tells user to try to decrease screen time
if diet is no, tells user to consume balanced levels of fruits, vegetabls, and red meats
if water is less than 3, tells user to drink at least 3 liters of water a day
if exercise - no, tells user to try exercising 30 minutes at least 3+ days a week
if sleep < 7.5, tells user to try to get at least 7.5 hours of sleep each night
if drugs > 1, t ells user to not do drugs
if alcohol > 3, tells user drinking is okay, but try to cut back
if smoke > 3, tells user to try to cut back on how much they smoke
if depression - yes, tells user to talk to talk to friends/famikly or seek professional help

## 3b)
### i. The first program code segment must show how data have been stored in the list. 
````
list[checkup, eyeDoctor, screens, diet, water, exercise, sleep, drugs, alcohol, smoke, depression,]
````

### ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 
````
checkup = input('how many months since last annual checkup')
eyeDoctor = input('how many months since last eye checkup')
screens = input('on average, how many hours do you use screens')
diet = input('are you eating healthy portions of fruits, vegetables, and red meats')
water = input('how many liters of water do you drink each day')
exercise = input('do you exercise at least 30 minutes for 3+ days a week')
sleep = input('on average, how many hours of sleep do you get each night')
drugs = input('how many times a week do you use drugs')
alcohol = input('how many times a week do you consume alcohol')
smoke = input('how many times a week do you smoke')
depression = input('have you experienced signs of depression/anxiety recently')
````

### iii. Identifies the name of the list being used in this response
list

### iv. Describes what the data contained in the list represent in your program
strings that are turned into integers

### v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently if you did not use the list 
if i wrote it without the list, I would have to write out each functions individually insteady of all the values consectuively in one list

## 3c)
### i. The first program code segment must be a student-developed procedure that: 
* Defines the procedure’s name and return type (if necessary)
* Contains and uses one or more parameters that have an effect on the functionality of the procedure
* Implements an algorithm that includes sequencing, selection, and iteration

````
def healthy(list):
    list[checkup, eyeDoctor, screens, diet, water, exercise, sleep, drugs, alcohol, smoke, depression,]

    if int(checkup) > 12:
        print("please schedule annual checkup with your doctor asap")
    else:
        print("continue keeping track of annual checkups")

    if int(eyeDoctor) > 24:
        print("please schedule eye doctor appointment asap")
    else:
        print("continue keeping track of eye exams")

    if int(screens) > 8:
        print("try to decrease screen time to 8 hours or less each day")
    else:
        print("your screen time is suitable")

    if diet == 'no':
        print("try to consume balanced levels of fruits, vegetables, and red meats")
    else:
        print("keep up your balanced diet")

    if int(water) < 3:
        print("try to drink at least 3 liters of water a day")
    else:
        print("keep drinking lots of water")

    if exercise == 'no':
        print("try exercising 30 minutes at least 3+ days each week")
    else:
        print("keep exercising 30 minutes at least 3+ days each week")

    if int(sleep) < 7.5:
        print("try to get at least 7.5 hours of sleep each night")
    else:
        print("continue getting 7.5+ hours")

    if int(drugs) > 1:
        print("please don't do drugs")
    else:
        print("stay drug free")

    if int(alcohol) > 3:
        print("drinking is okay, but try to cut back")
    else:
        print("keep up good drinking habits")

    if int(smoke) > 3:
        print("try to cut back on how much you smoke")
    else:
        print("try to quit smoking, and if you don't smoke already good job")

    if depression == 'yes':
        print("talk to friends/family or seek professional help")
    else:
        print("stay happy and keep making friends")
````

### ii. The second program code segment must show where your student-developed procedure is being called in your program.
````
healthy(list)
````

### iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
It takes in variables that the user inputs and compares it to given values to determine whether or not the user should change their habits

### iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
Algorithm has base values determing if a habit was healthy or not. Different message displayed depending of whether a habit is healthy or not. 

## 3d)
### i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
First call: 
````
    if int(water) < 3:
        print("try to drink at least 3 liters of water a day")
````

Second call:
````
    else:
        print("keep drinking lots of water")
````

### ii. Describes what condition(s) is being tested by each call to the procedure
Condition(s) tested by the first call:

The first call tests if the amount of water is less than 3 liters

Condition(s) tested by the second call

The second call tests if the amount of water is not less than 3 liters

### iii. Identifies the result of each call
Result of the first call:
The first call will result in the program displaying "try to drink at least 3 liters of water a day"

Result of the second call:
The second call will result in the program displaying "keep drinking lots of water"
