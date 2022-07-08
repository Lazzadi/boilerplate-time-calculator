def add_time(start, duration, startDay = None):
  weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

  #considering all inputs will be identical we can determine the initial hour, minutes, AM/PM and time to add through a split
  hours = int(start.split(':')[0])
  minutes = int((start.split(':'))[1].split(' ')[0])
  hourFormat = (start.split(':'))[1].split(' ')[1]
  hoursAdd = int(duration.split(':')[0])
  minutesAdd = int(duration.split(':')[1])

  #Variable daysLater to store number of passing days
  daysLater = 0

  #Program adds minutes to our time. If minutes are 60 or more we add 1 to the hour counter and deduct 60 minutes from the minutes variable
  #Everytime hours becomes more than 12 we switch the hour format and deduct 12 from the hour. Also when the format changes from PM to AM we add 1 to the days later counter
  minutes = minutes + minutesAdd
  if(minutes>59):
    hours = hours + 1
    minutes = minutes - 60
    if (hours>=12 and hourFormat == 'PM'):
      hours = hours - 12
      hourFormat = 'AM'
      daysLater = daysLater + 1
    elif (hours >= 12 and hourFormat =='AM'):
      hours = hours - 12
      hourFormat = 'PM'

  #Program adds the hours and calculates how many days have passed and if the format should be changed.
  #The hour variable then becomes hours%12 to reflect the correct hour
  hours = hours + hoursAdd
  if(hours>=24):
    daysLater = daysLater + int(hours/24)
    
    if((hours%24)>=12 and hourFormat == 'AM'):
      hourFormat = 'PM'
  
    if((hours%24)>=12 and hourFormat == 'PM'):
      hourFormat = 'AM'
      daysLater = daysLater + 1
    hours = hours%12

  #If hours is more than 12 (but less than 24) hour is adjusted in the AM/PM format and on day is added to counter if it is needed
  if (hours>12 and hourFormat == 'PM'):
      hours = hours - 12
      hourFormat = 'AM'
      daysLater = daysLater + 1
  elif (hours > 12 and hourFormat =='AM'):
      hours = hours - 12
      hourFormat = 'PM'
  
  #There is a posibility hour becomes 00 but since this hour doesn't exist in the AM/PM format we will change it back to 12
  if (hours == 0):
    hours = 12

  #in case minutes are less then 10 we want to display them with a 0 in front
  if (minutes<10):
    minutes = '0' + str(minutes)

  #Algorithm for displaying results
  if(startDay!=None):
    if(startDay.title() in weekdays and daysLater == 0):
        newWeekDay = weekdays.index(startDay.title()) + int(daysLater%7)
        new_time = (f'{hours}:{minutes} {hourFormat}, {weekdays[newWeekDay]}')
    
    elif(startDay.title() in weekdays and daysLater == 1):
        newWeekDay = weekdays.index(startDay.title()) + int(daysLater%7)
        new_time = (f'{hours}:{minutes} {hourFormat}, {weekdays[newWeekDay]} (next day)')
    
    elif(startDay.title() in weekdays and daysLater > 1):
        newWeekDay = (weekdays.index(startDay.title()) + int(daysLater))%7
        new_time = (f'{hours}:{minutes} {hourFormat}, {weekdays[newWeekDay]} ({daysLater} days later)')
    
  if(startDay == None and daysLater == 0):
      new_time = (f'{hours}:{minutes} {hourFormat}')
    
  elif(startDay == None and daysLater == 1):
      new_time = (f'{hours}:{minutes} {hourFormat} (next day)')
    
  elif(startDay == None and daysLater>1): 
      new_time = (f'{hours}:{minutes} {hourFormat} ({daysLater} days later)')

  return(new_time)