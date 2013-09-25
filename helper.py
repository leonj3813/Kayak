import string
import time
import datetime
from dateutil import rrule

def filter_results(soup):
    """Given a kayak soup, returns the list [price, 1st Departure time, 2nd Departure time]"""
    output = []
    for each in soup.find_all(class_ = "flightresult"):
        # find the price and print it out
        price = each.find(class_ = "results_price")
        flight = [price.string.strip()]
        
        # find the first leg of the trip
        leg1 = each.find(class_= "singleleg0")
        Departure = string.replace(string.replace(leg1.find(class_ = "flightTimeDeparture").string.strip(),'p', 'PM'),'a','AM')
        flight.append(time.strptime(Departure, "%I:%M%p"))
                
        # find the second leg of the trip
        leg2 = each.find(class_ = "singleleg1")
        Departure = string.replace(string.replace(leg2.find(class_ = "flightTimeDeparture").string.strip(),'p', 'PM'),'a','AM')
        flight.append(time.strptime(Departure, "%I:%M%p"))

        # append price and times to return array
        output.append(flight)
    return output

def return_URLs():
    """Generates the URLs for finding flights on the weekend on kayak"""
    base_url = "http://www.kayak.com/flights/SCE-ATL/"
    today = datetime.date.today()
    dates = list(rrule.rrule(rrule.WEEKLY, count=1, byweekday=rrule.FR(1),
        dtstart=today))
    
    date_format = "%Y-%m-%d"
    URLs = []
    for date in dates:
        range = date.strftime(date_format) + "/" + (date + datetime.timedelta(days=2)).strftime(date_format)
        URLs.append(base_url + range)
    return URLs