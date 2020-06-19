# uses python3 syntax
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory

import csv, os, sys

cwd = os.getcwd()
os.chdir('./removeCsvHeader')
cwd = os.getcwd()

os.makedirs('headerRemoved',exist_ok=True)

# Loops through every file in the current working directory
for csvFilename in os.listdir('.'): 
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')
    # read the CSV file in (skipping first row)
    csvRows = []
    with open(csvFilename, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            if csvReader.line_num == 1:
                continue
            csvRows.append(row)
          
        #  write out the csv files
        outputFile = open(os.path.join('headerRemoved', csvFilename), 'w',newline='')
        outPutWriter = csv.writer(outputFile)
        for row in csvRows:
            outPutWriter.writerow(row)
        
        csvFile.close()


    
