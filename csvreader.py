

import csv
with open('.csv', 'r') as file:
    reader = csv.reader(x.replace('\0', '') for x in file)

    for row in reader:
        print(row)



