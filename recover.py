#.csv files are not provided in 'hackdata.cn', so I recover them using code below:

import csv
with open(path, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print ','.join(row)
    

