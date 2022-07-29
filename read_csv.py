#reading data from CSV file
import csv
with open('test_meet.csv') as cs:
	csv_reader=csv.reader(cs)
	for line in csv_reader:
		print(line)
cs.close()
