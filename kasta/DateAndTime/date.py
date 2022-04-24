import datetime
import calendar

now = datetime.datetime.now()
dateNow = datetime.datetime.today()
weekNow = calendar.day_name[dateNow.weekday()]
monthNow = now.month
dayNow = now.day

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

ordinal = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
 '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
 '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th',
 '29th', '30th', '31st']

def whatDay():
    return f'Today is {weekNow}, {months[monthNow-1]} the {ordinal[dayNow-1]}.'

def whatMonth():
    return f"It is {months[monthNow-1]}."

def fullDate():
    return f'In the calendar i can see that today is {now.strftime("%Y")}, month {now.strftime("%B")}, day {now.strftime("%d")}.'

def clockTime():
    return f'It is {dateNow.strftime("%H %M")}.'

def weekDay():
    return f'Today is a {weekNow}'

def dayOfTheYear():
    return f'The day of the year is {now.strftime("%j")}'


