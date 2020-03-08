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

        for row in reader:
            writer.writerow(row)
    
    print('Ran: Custom_Methods.duplicate_csv_file().')

# @DEBUG
# duplicate_csv_file()
