import csv
f = open('HOSPITAL.csv', 'r')
data = csv.reader(f)
header = next(data)
query = 'headach'
try:
    for row in data:
        if row[1] in query:
            name = row[0]
            Link = row[2]
            break
    print(name, Link)
except Exception as e:
    print(e)