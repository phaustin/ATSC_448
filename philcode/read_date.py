from pathlib import Path
all_files = Path().glob("*")
all_files = list(all_files)
one_date = "mydata_200310301.cdf"
dump, the_date = one_date.split('_')
good_year, suffix = the_date.split('.')
year, month,day=int(good_year[0:4]), int(good_year[4:6]), int(good_year[6:8])
import datetime
the_date=datetime.datetime(year=year, month=month, day=day)
print(the_date)
