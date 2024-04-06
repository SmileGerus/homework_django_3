import csv

with open('../data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    station_list = list(reader)
print(station_list[4]['Street'])