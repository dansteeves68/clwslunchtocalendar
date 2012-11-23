# CLWS Lunch to Calendar

For my family at City of Lakes Waldorf School in Minneapolis, MN

 - Every month we sign up for delivered lunches.
 - The email we get lists lunches per day by person.
 - I need to be reminded the mornings when anyone has 'no lunch,'
   so I can prepare a bag lunch that day.

Steps to do

1. Take text of email.
2. Find (person, day) combinations with no lunch.
3. For each no-lunch day, add an entry to an ics file
   that I can load into Calendar.app.

# Dependencies

 - [`parsedatetime`](https://github.com/bear/parsedatetime)
 - [`icalendar`](http://pypi.python.org/pypi/icalendar/) - `pip install icalendar`


# TODO

 - write an ics file
 - sync source with gist
 - make it run as a service
 - make it automagically load into Calendar.app