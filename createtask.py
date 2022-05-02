
def healthy():
    print("---------------------")
    print("Directions: Enter response to each health question in order to try to stay alive. Submitting an unhealthy habit will end the game")
    print("")

# asks how long since last checkup, and gives positive/negative comment
    checkup = input('how many months since last annual checkup?  ')
    if int(checkup) <= 12:
        print("continue keeping track of annual checkups")
        print("")
    else:
        print("please schedule annual checkup with your doctor asap")
        print("")
        restart()

# asks how logn since last eye checkup, and gives positive/negative comment
    eyeDoctor = input('how many months since last eye checkup?  ')
    if int(eyeDoctor) <= 24:
        print("continue keeping track of eye exams")
        print("")
    else:
        print("please schedule eye doctor appointment asap")
        print("")
        restart()

# asks how long user spends on screens each day, and gives positive/negative comment
    screens = input('on average, how many hours do you use screens?  ')
    if int(screens) <= 8:
        print("your screen time is suitable")
        print("")
    else:
        print("try to decrease screen time to 8 hours or less each day")
        print("")
        restart()

# asks the user whether or not they have a good diet, and gives positive/negative comment
    diet = input('are you eating healthy portions of fruits, vegetables, and red meats? (yes/no)  ')
    if diet == 'yes':
        print("keep up your balanced diet")
        print("")
    else:
        print("try to consume balanced levels of fruits, vegetables, and red meats")
        print("")
        restart()

# asks the user how much water they drink in liters, and gives positive/negative comment
    water = input('how many liters of water do you drink each day?  ')
    if int(water) >= 3:
        print("keep drinking lots of water")
        print("")
    else:
        print("try to drink at least 3 liters of water a day")
        print("")
        restart()

# asks the user if they have good exercise habits, and gives positive/negative comment
    exercise = input('do you exercise at least 30 minutes for 3+ days a week (yes/no)?  ')
    if exercise == 'yes':
        print("keep exercising 30 minutes at least 3+ days each week")
        print("")
    else:
        print("try exercising 30 minutes at least 3+ days each week")
        print("")
        restart()

# asks the user how much sleep they get, and gives positive/negative comment
    sleep = input('on average, how many hours of sleep do you get each night?  ')
    if int(sleep) >= 7.5:
        print("continue getting 7.5+ hours")
        print("")
    else:
        print("try to get at least 7.5 hours of sleep each night")
        print("")
        restart()

# asks the user about their drug habits, and gives a positive/negative comment
    drugs = input('how many times a week do you use drugs?  ')
    if int(drugs) < 1:
        print("stay drug free")
        print("")
    else:
        print("please don't do drugs")
        print("")
        restart()

# asks the user about their alcohol habits, and gives a positive/negative comment
    alcohol = input('how many times a week do you consume alcohol?  ')
    if int(alcohol) <= 3:
        print("keep up good drinking habits")
        print("")
    else:
        print("try to keep alcohol consumption below to 3 times or less per week")
        print("")
        restart()

# asks the user about their smoking habits, and gives a positive/negative comment
    smoke = input('how many times a week do you smoke?  ')
    if int(smoke) == 0:
        print("continue to stay tobacco free")
        print("")
    elif int(smoke) <= 3:
        print("try to work toward staying tobacco free")
        print("")
    else:
        print("try to cut back on how much you smoke")
        print("")
        restart()

# aks the user about their mental health, and gives a positive/negative comment
    depression = input('have you experienced signs of depression/anxiety recently (yes/no)?  ')
    if depression == 'no':
        print("stay happy and keep making friends")
        print("")
    else:
        print("talk to friends/family or seek professional help")
        print("")
        restart()

# asks the user about if they want to take the survey again, and either restarts or exits
    survey_again = input('congratulations on your healthy habits! would you like to try the survey again? (yes/no)  ')
    if survey_again == 'yes':
        restart_survey()
    else:
        print("thank you for taking the survey")
        print("")
        exit()

# used when user input an unhealthy habit to display all the questions again
def restart():
    print("restarting survey. please enter healthier habits.")
    print("---------------------")
    healthy()

# used when user wants to take the survey again
def restart_survey():
    print("try inputting different values to see if they are healthy or not")
    print("")
    print("---------------------")
    healthy()

healthy()

