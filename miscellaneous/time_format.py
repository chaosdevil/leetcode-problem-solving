import datetime
import math

now = datetime.datetime.now()

date_list = []
date_list.append(datetime.datetime(2017, 3, 29, 10, 59, 24))
date_list.append(datetime.datetime(2017, 3, 29, 10, 12, 12))
date_list.append(datetime.datetime(2017, 3, 24, 17, 24, 54))
date_list.append(datetime.datetime(2017, 1, 14, 8, 43, 5))
date_list.append(datetime.datetime(2022, 8, 12, 17, 50, 00))

# print(date_list)

print(now.strftime('%B %d, %Y %I:%M:%S %p'))

for d in date_list:
	time_diff = (now - d).total_seconds()

	print(d.strftime('%B %d, %Y %I:%M:%S %p'))

	if time_diff <= 60:
		print(math.floor(time_diff), 'secs ago')
	elif time_diff <= 3600:
		print(math.floor(time_diff / 60), 'mins ago')
	elif time_diff <= 86400:
		print(math.floor(time_diff / 3600), 'hours ago')
	elif time_diff <= 86400 * 30:
		print(math.floor(time_diff / 86400), 'days ago')
	elif time_diff <= 86400 * 365.25:
		print(math.floow(time_diff / (86400 * 30)), 'months ago')
	else:
		print(math.floor(time_diff / (86400 * 365.25)), 'years ago')