import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs1, lows1, dates1 = [], [], [] 
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            dates1.append(current_date)
            highs1.append(high)
            lows1.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates1,highs1, c='red', alpha=0.5)
ax.plot(dates1, lows1, c='green', alpha=0.5)
plt.fill_between(dates1, lows1, highs1, facecolor='blue', alpha=0.1)

title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# filename = 'data/sitka_weather_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)

#     dates, highs, lows = [], [], []
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
    
#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         high = int(row[5])
#         dates.append(current_date)
#         highs.append(high)
#         lows.append(int(row[6]))

# ax.plot(dates1,highs, c='red', alpha=0.5)
# ax.plot(dates1, lows, c='green', alpha=0.5)
# plt.fill_between(dates1, lows, highs, facecolor='blue', alpha=0.1)


plt.show()