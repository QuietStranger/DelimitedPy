import datetime
import csv
from csv import reader, writer

def duplicate_csv_file(source_csv='default value', output_csv='default value'):
    # @DEBUG
    # print('Calling: Custom_Methods.duplicate_csv_file()')

    source_csv = ''
    source_csvPath = ''

    output_csv = 'temp.tmp'


    with open(source_csv) as input_file, open(output_csv, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        
        # .writerow If you want to insert a row before copying.
        writer.writerow(['name', 'size', 'modified'])

        for row in reader:
            writer.writerow(row)

# @DEBUG
# duplicate_csv_file()
