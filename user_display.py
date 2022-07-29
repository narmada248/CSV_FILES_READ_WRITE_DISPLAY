#take input from user and display the csv file data
import csv
with open("test_meet.csv","a+") as cs:
	csv_writer=csv.writer(cs)
	ans="y"
	while(ans=="y" or ans=="Y"):
		S_ID=input("enter student id:")
		S_NAME=input("enter student name:")
		S_COUNTRY=input("enter student country:")
		csv_writer.writerow([S_ID,S_NAME,S_COUNTRY])
		ans=input("do u want to enter more records into csv file y/n?")
	cs.seek(0)
	csv_reader=csv.reader(cs)
	for line in csv_reader:
		print(line)
cs.close()
	
