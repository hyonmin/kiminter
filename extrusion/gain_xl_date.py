from datetime import datetime
import time

def xl_date(day):
    time_format = "%Y/%m/%d"
    init = datetime.strptime("1900/1/1", time_format)
    if day == None:
        day = datetime.today()
    delta = day-init
    delta = delta.days + 2
    #print(delta)
    return delta