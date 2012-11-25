#!/usr/bin/python

import sys
text = sys.stdin.read()

pack_lunches = {}
person = ''

for line in text.split('\n'):
    if line.startswith('Childs Name:'):
        if 'Darcie' in line:
            person = 'Darcie'
        if 'Elliot' in line:
            person = 'Elliot'
        if 'Quinton' in line:
            person = 'Quinton'
    elif 'No ' in line:
        my_date = line.split(':')[0]
        if my_date not in pack_lunches:
            pack_lunches[my_date] = [person]
        else:
            pack_lunches[my_date].append(person)

import parsedatetime as pdt
parser = pdt.Calendar()

import icalendar as ical
from datetime import datetime, timedelta

cal = ical.Calendar()
cal.add('prodid', 'foo')
cal.add('version', '2.0')

for day_str in pack_lunches.keys():
    start = parser.parse(day_str)[0]
    dtstart = datetime(start[0], start[1], start[2]).date()
    dtend   = dtstart + timedelta(days = 1)
    trigger = datetime(start[0], start[1], start[2], 7, 0)
    
    summary = 'Pack lunch for %s' % " & ".join(pack_lunches[day_str])
    
    event = ical.Event()
    event.add('summary', summary)
    event.add('dtstart', dtstart)
    event.add('dtend',   dtend)
    alarm = ical.Alarm()
    alarm.add('trigger', trigger)
    alarm.add('action', 'DISPLAY')
    event.add_component(alarm)
    cal.add_component(event)

import os
filename = "/Users/dan/Desktop/Lunch %s.ics" % datetime.now().date()
print filename
f = open(filename, 'wb')
f.write(cal.to_ical())
f.close()