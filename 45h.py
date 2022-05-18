import requests
import csv
region = str(input('enter region code = '))
codes1 = ['01', '05', '07']
codes2 = [12, 14, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59, 61, 63, 65, 68, 71, 73, 74, 80, 85]
a = int(region) in codes2
b = region in codes1
if a is False:
    if b is False:
        print('enter another code')
        exit(0)

print('Ректор / в.о. директора / Президент / В.о. ректора / В.о. директора коледжу / Директор / Т.в.о.директора ')
value1 = str(input('Введіть(Скопіюйте) 1 із запропонованих вище параметрів: '))
r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region+'&exp=json')

universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data2 = [{k: row[k] for k in ['university_name', 'university_name_en', 'university_director_post']}
                  for k in ['university_director_post'] for row in universities if row[k] == value1]

with open('universities_'+region+'.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open('ua_en.csv', mode='w', encoding='CP1251') as fw:
    writer = csv.DictWriter(fw, fieldnames=filtered_data2[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data2)
