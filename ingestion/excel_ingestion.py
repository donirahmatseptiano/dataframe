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
    df = pd.read_excel(listData[key]+'.'+key)

    return df