import csv
import datetime

# life list: name, date, location, thumbnail
# images: name, location, date, file path

def date_to_string(date):
    return f'{date.strftime("%B")} {int(date.strftime("%d"))}, {date.strftime("%Y")}'

if __name__ == '__main__':
    list = 'assets/images/birds/_life_list.csv'
    images = 'assets/images/birds/_species.csv'
    
    entries = {}
    with open(list, 'r') as life_list:
        reader = csv.reader(life_list, delimiter=',')
        for row in reader:
            row = [item.strip() for item in row]
            date = datetime.date.fromisoformat(row[1])

            key = ''.join(filter(str.isalpha, row[0])).lower()
            entries[key] = {
                'name': row[0],
                'date': date,
                'location': f'{row[2]}, {row[3]}, {row[4]}',
                'thumbnail': None if len(row)==5 else f'assets/images/birds/thumbnails/{row[5]}',
                'images': []
            }
    
    keys = entries.keys()
    keys = sorted(keys)
    # keys = sorted(keys, key=(lambda x: entries[x]['date']), reverse=True)
    
    with open(images, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            row = [item.strip() for item in row]
            date = datetime.date.fromisoformat(row[4])

            key = ''.join(filter(str.isalpha, row[0])).lower()
            entries[key]['images'].append({
                'date': date,
                'location': f'{row[1]}, {row[2]}, {row[3]}',
                'file': f'{row[5]}',
            })

    out = open('_data/life_list.yml','w')
    out.write(f'# This file was automatically generated\n# original: {list}\n\n')
    for key in keys:
        entry = entries[key]

        out.write(f'- name: {entry["name"]}\n')
        out.write(f'  date: {date_to_string(entry["date"])}\n')
        out.write(f'  location: {entry["location"]}\n')
        if entry['thumbnail']:
            out.write(f'  thumbnail: {entry["thumbnail"]}\n')
        
        if entry['images']:
            out.write(f'  images:\n')
            for image_entry in entry['images']:
                out.write(f'   - file: {image_entry["file"]}\n')
                out.write(f'     date: {date_to_string(image_entry["date"])}\n')
                out.write(f'     location: {image_entry["location"]}\n')
        
        out.write('\n')