import csv

def main(csv_file, keepdate):
    with open(csv_file, "r", encoding="utf-8") as infile, \
         open("date_cleaned.csv", "w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            if row[0] == keepdate:
                writer.writerow(row)
                
    print("Completed")
