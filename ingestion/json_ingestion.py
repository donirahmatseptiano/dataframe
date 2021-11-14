import json
import pandas as pd

def read_source(filename):
    with open(filename, 'r') as file:
        confs = file.readlines()

    dictConf = {}
    for conf in confs:
        line = conf.split('=')
        dictConf[line[0].strip()] = line[1].strip()

    return dictConf

def import_data(key, filename):
    listData = read_source(filename)

    with open(f'{listData[key]}.{key}', 'r') as f:
        data = json.loads(f.read())
    
    df = pd.json_normalize(data, record_path = ['data'])

    return df