__author__ = 'Steven Porter'
import pandas as pd
import os

class ProcessError(Exception):
    pass

if __name__=="__main__":
    for file in os.listdir('raw_data'):
        base,ext = os.path.splitext(file)
        print ext
        if ext.lower() == '.tsv':
            df = pd.read_table(os.path.join('raw_data',file))
        elif ext.lower() == '.csv':
            df = pd.read_csv(os.path.join('raw_data',file))
        else:
            raise ProcessError('Unknown file type')

        df.to_json(os.path.join('json',base+'.json'))