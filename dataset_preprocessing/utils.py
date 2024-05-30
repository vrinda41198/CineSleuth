import csv


def writeToCSV(file_name, dict_object):
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict_object.items():
            writer.writerow([key, value])