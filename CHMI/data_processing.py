import os
import pandas as pd
import csv
from itertools import groupby
from datetime import datetime

rootdir = ("C:\\Users\\elisk\\Desktop\\Data\\CHMU\\CHMU_historical_data\\")
os.chdir(rootdir)

ending = 'T_N.csv'

rootdir = ("inputs")

def data_processing(data):
    date = datetime(int(data[0]), int(data[1]), int(data[2]))
    date = [date.strftime('%d.%m.%Y'), ]
    # station_id = data[-2]
    # appending_data += station_data[station_id]
    return date

data = {'METADATA' : {
            'headers' : ["Station_id", "Station_name", "Measure_start", "Measure_end", "Longitude", "Latitude", "Elevation", "Station", "Variable"],
            'data' : [],
        },
        'DATA' : {
            'headers' : ["Year", "Month", "Day", "Desc", "Value", "Station", "Variable", "Datetime"],
            'data' : [],
            'extra_processing' : data_processing
        }}

""" station_data = {}
station_file = ("stanice_ids.csv")
with open(station_file,  encoding="cp1250") as csvfile:
    csv_lines = csv.reader(csvfile, delimiter=";")
    headers = next(csv_lines)
    headers.pop(0)
    data['DATA']['headers'] += headers
    for line in csv_lines:
        station_id = line[0]
        station_data[station_id] = line
 """

for subdir, dirs, files in os.walk(rootdir):
    for entry in files:
        if entry.endswith(ending):
            file_path = os.path.join(subdir, entry)
            last_header = ""
            is_header = False
            row_index = 0
            with open(file_path,  encoding="cp1250") as csvfile:
                csv_lines = csv.reader(csvfile, delimiter=";")
                for line in csv_lines:
                    if len(line) > 0:
                        is_header = len(line) == 1
                        if is_header:
                            last_header = line[0]
                            row_index = 0
                        row_index += 1

                        if last_header in data and not is_header and row_index > 2:
                            file_index = len(line)
                            station = entry.split('_')[0]
                            variable = entry.split('_')[1]
                            line.append(station)
                            line.append(variable)
                            
                            if 'extra_processing' in data[last_header]:
                                line += data[last_header]['extra_processing'](line)                           
                        
                            data[last_header]['data'].append(line)

    for data_header in data:
        with open(f"outputs\\processed_{data_header}_{ending}.csv", 'w', newline='', encoding='cp1250') as csvfile:
            datawriter = csv.writer(csvfile, delimiter = ';', quotechar = '"')
            ## quotechar does work!!!!
            datawriter.writerow(data[data_header]['headers'])
            for line in data[data_header]['data']:
                #print(line)
                datawriter.writerow(line)

                