#write data into CSV file
import csv
with open("test_meet.csv","a+") as cs:
	cs_writer=csv.writer(cs)
	cs_writer.writerow(["222","jai","india"])
	print("record inserted Succeefully")
	cs.seek(0)
	csv_reader=csv.reader(cs)
	for line in csv_reader:
		print(line)	

cs.close()
