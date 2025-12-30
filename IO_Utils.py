import csv

def ReadTsv(filename):
    with open(f'{filename}', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = list(reader)
    return rows