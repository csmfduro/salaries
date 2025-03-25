import csv
#file name set allowing easy access if file ever is lost
filePath = "Salaries Data\\salaries.csv"

def read(filePath):
    with open(filePath, "r") as f:
        csv_reader = csv.reader(f)
        #skips header as the column names are stored there
        next(csv_reader)
        data = [row for row in csv_reader]
        return data


data = read(filePath)
print(data)