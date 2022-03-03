from datetime import datetime, time
def date(dt1, dt2):
    timedelta=dt2-dt1
    return timedelta.days*24*3600+timedelta.seconds
date1=datetime.strptime('2003-10-17 03:37:21', '%Y-%m-%d %H:%M:%S')
date2=datetime.now()
print(f'{(date(date1, date2))} seconds')
