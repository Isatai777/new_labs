#ex1
from datetime import date, timedelta
current_date = date.today()
new_date = current_date - timedelta(days=5)
print(new_date)

# #ex2
from datetime import date , timedelta
current_date = date.today()
tomorrow_date = current_date + timedelta(days=1)
yesterday_date = current_date - timedelta(days=1)
print(f"current date is , {current_date}")
print(f"yesterday date is , {yesterday_date}")
print(f"tomorrow date is , {tomorrow_date}")


# ex3
from datetime import datetime, timedelta
current_datetime = datetime.now()
print(current_datetime.strftime("%H"),":",current_datetime.strftime("%M") ,":", current_datetime.strftime("%S"))  



#ex4
from datetime import datetime

date1 = datetime(2024, 3, 9, 12, 50, 0)  
date2 = datetime.now() 
time_difference = date2 - date1
seconds_difference = time_difference.total_seconds()

print(f"{int(seconds_difference)} seconds")