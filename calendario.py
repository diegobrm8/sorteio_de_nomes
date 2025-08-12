import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
year = 2024
cal_content = cal.formatyear(year)


print(cal_content)