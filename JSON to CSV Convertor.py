import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file) as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


