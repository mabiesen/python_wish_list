import csv
import unicodecsv

#Receives data as list of sublists, with a sublist representing a row
def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def csv_reader(myfilepath):
    file_row = []
    cr = csv.reader(open(myfilepath,"rb"))
    for row in cr:
        for item in row:
            file_row.append(item)
    return file_row

def csv_writer_uni(data,path):
    w = unicodecsv.writer(open(path, "wb"))
    for line in data:
        w.writerow(line)
    del w
