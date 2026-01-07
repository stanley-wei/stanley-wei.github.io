import csv
import datetime

if __name__ == '__main__':
    list = 'assets/images/birds/_species.csv'
    out = open('_data/life_list.yml','w')
    
    out.write(f'# This file was automatically generated\n# original: {list}\n\n')
    
    with open(list, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            row = [item.strip() for item in row]
            date = datetime.date.fromisoformat(row[4])

            out.write(f'- name: {row[0]}\n')
            out.write(f'  thumbnail: assets/images/birds/thumbnails/{row[5]}\n')
            out.write(f'  location: {row[1]}, {row[2]}, {row[3]}\n')
            out.write(f'  date: {date.strftime("%B")} {int(date.strftime("%d"))}, {date.strftime("%Y")}\n\n')
