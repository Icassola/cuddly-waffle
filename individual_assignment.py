#Import the data from json, trim to only csv and save for random

import json

with open ('conflict_data_full_lined.json', encoding=utf-8) as file:
    raw_data_dict = json.load (file) 

venezuela_data = []

for observation in raw_data_dict:
    if observation['country'] == 'Venezuela':
        venezuela_data.append(observation)
print(venezuela_data)

import csv
header = []

for observation in venezuela_data:
    for key in observation.keys(): 
        if key not in header:
            header.append(key)
with open('venezuela_data.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header, lineterminator='\n', 
        delimiter=',')
    writer.writeheader()

    for observation in venezuela_data:
        writer.writerow(observation)