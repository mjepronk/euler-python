# vim: sw=4:ts=4:et:ai

import datetime

counter = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        first_of_the_month = datetime.datetime(year, month, 1)
        if first_of_the_month.weekday() == 6:
            counter += 1

print("Result: %i" % counter)

