import datetime
from dateutil import rrule
today = datetime.date.today()

dates = list(rrule.rrule(rrule.WEEKLY, count=10, byweekday=rrule.FR(1),
    dtstart=today))
	
date_format = "%Y-%m-%d"
for date in dates:
    two_days = date + datetime.timedelta(days=2)
    print date.strftime(date_format) + "/" + two_days.strftime(date_format)
	