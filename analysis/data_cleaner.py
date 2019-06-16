import pandas as pd
import numpy as np

DATA = 'test1.csv'

df = pd.read_csv(DATA, sep=';')


def clean_data(db):
    db = db.drop(labels='mainsearch', axis=1)
    db = db.drop(labels='id', axis=1)

    # Removing 0 values
    for key in db.keys():
        for site in db[key].keys():
            if db[key][site] == 0:
                db[key][site] = np.nan  # replaces 0s with NaN
    # Drops null values
    db = db.dropna(axis=1, how='all')
    db = db.dropna(axis=0, how='all')
    # Reinsert 0 values to simplify later calculations
    db = db.fillna(value=0)

    return db
