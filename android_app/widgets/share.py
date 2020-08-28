import calendar

WEEKDAYS_MAPPING = {weekday_name: nr + 1
                    for nr, weekday_name in enumerate(calendar.day_name)}
