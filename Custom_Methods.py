import datetime
import csv
from csv import reader, writer

# import os.path
from pathlib import Path

def duplicate_csv_file(source_csv='input.csv', output_csv='temp.tmp'):
    # @DEBUG
    print('Running: Custom_Methods.duplicate_csv_file() ...')

    source_csv = Path(source_csv)

    source_csvPath = Path(output_csv)


    with open(source_csv) as input_file, open(output_csv, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        
        # .writerow If you want to insert a row before copying.
        writer.writerow(['name', 'size', 'modified'])

        # Actual copying line by line.
        for row in reader:
            writer.writerow(row)
    
    print('Ran: Custom_Methods.duplicate_csv_file().')

import unicodedata

# @DEBUG
# duplicate_csv_file()

def check_utf8():
    # @DEBUG
    print('Running: Custom_Methods.check_utf8() ...')

    singleCharacter = 'ê'
    print(singleCharacter.encode())


    singleCharacter = 'ê'
    print('first string character: ' + singleCharacter)
    print('length of first string= ' , len(singleCharacter))

    multipleChars = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
    print('second string character: ' + multipleChars)
    print('length of second string= ' , len(multipleChars))
    
    # print(singleCharacter + multipleChars)

    # testStr = singleCharacter
    # testStr = testStr.encode(encoding='UTF-8', errors='strict')

    print('singleCharacter: ' + str(singleCharacter.encode(encoding='UTF-8', errors='strict')))
    print('multipleChars: ' + str(multipleChars.encode(encoding='UTF-8', errors='strict')))
    # print('singleCharacter' + str(singleCharacter.encode(encoding='UTF-8', errors='strict')))

    print(multipleChars.encode(encoding='us-ascii', errors='strict'))


def get_headers_csv(csvFilePath='./test_csv.csv'):
    # if not csvFilePath:
    #     # headers = 'error'
    #     pass
    # else:
    #     csvFilePath = str(csvFilePath)
    
    # csvFilePath = Path(csvFilePath)
    with open(csvFilePath, newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        

        for row in reader:
            print(row)

        print(reader.)
        
        # .writerow If you want to insert a row before copying.
        # writer.writerow(['name', 'size', 'modified'])

        # Actual copying line by line.
        # for row in reader:
        #     writer.writerow(row)
get_headers_csv()