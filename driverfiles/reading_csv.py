import csv
d={}

def read_(filepath):
    with open(filepath) as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            key=(row[0])
            value=(row[1])
            # print(key,value)
            d[key] = value
        return d
