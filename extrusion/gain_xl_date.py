from datetime import datetime

def xl_date(day):
    time_format = "%d/%m/%Y"
    init = datetime.strptime("1/1/1900", time_format)
    if day == None:
        day = datetime.today()
    else:
        day = datetime.strptime(day, time_format)
    delta = day-init
    delta = delta.days + 2
    return delta

def convert_xl_normal(xl_date):
    time_format = "%d/%m/%Y"
    dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + xl_date - 2)
    return datetime.strftime(dt, time_format)