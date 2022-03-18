#print("Hello World")
#Assign a variable for the file to load and the path
#file_to_load = r'C:\Users\ramak\OneDrive\Desktop\resources\election_results.csv'
#election_data = open(file_to_load,'r')
#print(file-to_load)
#import csv
#dir(csv)
#file_to_load = 'C:\\Users\ramak\OneDrive\Desktop\resources\election_results.csv'


import csv
dir(csv)
import os
dir(os)
#Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.

#with open(file_to_load) as election_data:
#Print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis","election_analysis.txt")
# Using the with statement open the file as a text file.
txt_file = open("file_to_save", "w")
# Write some data to the file. 
txt_file.write("Hello World")   