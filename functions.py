import csv

def read_csv():
    array_x = []
    array_y = []
    with open('data.csv') as csv_file:
        # reading the CSV file
        data = csv.reader(csv_file)
        for row in data:
            # NEED SQUARE BRACKET TO ADD ELEMENT
            array_x += [float(row[0])]
            array_y += [float(row[1])]
        return [array_x, array_y]