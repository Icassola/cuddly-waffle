#Import the data from json, trim to only csv and save for random

import json
with open ('conflict_data_full_lined.json') as file:
    raw_data_dict = json.load (file) 

conflict_venezuela = []

for observation in raw_data_dict:
    if observation['country'] == 'Venezuela':
        conflict_venezuela.append(observation)
print(conflict_venezuela)

