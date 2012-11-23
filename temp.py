import icalendar as ical
from datetime import datetime

cal = ical.Calendar()
cal.add('prodid', 'foo')
cal.add('version', '2.0')

event = ical.Event()
event.add('summary', 'My summary')
event.add('dtstart', datetime(2012,12,1).date())
event.add('dtend',   datetime(2012,12,2).date())
alarm = ical.Alarm()
alarm.add('trigger', datetime(2012,12,1,7,0,0))
alarm.add('action', 'DISPLAY')
event.add_component(alarm)
cal.add_component(event)
print cal.to_ical()

f = open('dan_exa.ics', 'wb')
f.write(cal.to_ical())
f.close
f.close()
exit()
