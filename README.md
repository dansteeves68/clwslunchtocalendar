# CLWS Lunch to Calendar

For my family at City of Lakes Waldorf School in Minneapolis, MN

 - Every month we sign up for delivered lunches
 - The email we get lists lunches per day by person
 - I need to be reminded the mornings when anyone has 'no lunch,'
   so I can prepare a bag lunch that day

# Installation

 - Install dependencies (below)
 - Copy the contents of file `lunch.py`
 - Open Automator.app, create a service in python, paste contents into script field

# Usage

 - Select text in email
 - Select Service from menu
 - Creates a file on desktop 'Lunch YYYY-MM-DD.ics'
 - Open file, create a new calendar
 - Get reminders when I have to make lunch

# Dependencies

 - [`parsedatetime`](https://github.com/dansteeves68/parsedatetime) - requires my patch for "Mmm. DD" period abbreviations
 - [`icalendar`](http://github.com/dansteeves68/icalendar)

# TODO

 - make it automagically load into Calendar.app
