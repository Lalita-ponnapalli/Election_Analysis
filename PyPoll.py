import csv
import os
dir(os)
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("Analysis","Election_analysis")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)    

