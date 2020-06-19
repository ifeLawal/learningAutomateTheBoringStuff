import csv, sys
import os


# get current working directory 
os.getcwd()

# change working directory with relative typing
# print(os.chdir('../'))

# change directory to the path directory name while adding the abspath
# os.path.join(sys.path[0], 'filename') is a better implementation
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# exampleFile = open('example.csv')
# with open('example.csv', newline='') as csvfile:
#     exampleReaderW = csv.reader(csvfile)
#     for row in exampleReaderW:
#         print('Row # %d, %s' % (exampleReaderW.line_num,row))

#     csvfile.close()

# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)

# for row in csv.reader(['one,two,three']):
#     print row

# csv reader and writer
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam','eggs','bacon','ham'])
# outputWriter.writerow(['Hello,world!','eggs','bacon','ham'])
# outputWriter.writerow([1,2,3.141592,4])
# outputFile.close()

# outputFiletsv = open('example.tsv', 'w', newline='')
# outputWriter = csv.writer(outputFiletsv,delimiter='\t',lineterminator='\n\n')
# outputWriter.writerow(['apples','orange','grapes'])
# outputWriter.writerow(['eggs','bacon','ham'])
# outputWriter.writerow(['Spam']*6)
# outputFiletsv.close()


# dict reader and writer. Better in situations when you need a header
# reading
# if you already have a header
# with open('exampleWithHeader.csv', newline='') as dictFile:
#     dictReader = csv.DictReader(dictFile)
#     for line in dictReader:
#         print(line['Timestamp'],line['Fruit'],line['Quantity'])

#     dictFile.close()
# print('-'*20)

# # if you need to provide a header
# with open('example.csv', newline='') as csvfile:
#     exampleCSVReader = csv.DictReader(csvfile,['time','name','amount'])
#     for line in exampleCSVReader:
#         print(line['time'],line['name'],line['amount'])

#     csvfile.close()

# writing
dictFile = open('outputDict.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(dictFile, ['Name','Pet','Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})
outputDictWriter.writerow({'Name':'Alice','Phone':'555-9999'})
outputDictWriter.writerow({'Phone':'555-5555','Name':'Alice','Pet':'dog'})
dictFile.close()
