from datetime import date, timedelta
print('yesterday: ', date.today()-timedelta(1))
print('tofay: ', date.today())
print("tomorrow: ", date.today()+timedelta(1))