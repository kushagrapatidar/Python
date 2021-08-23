import csv
opened_file=open('AppleStore.csv',encoding="utf8")
read_file=csv.reader(opened_file)

apps_data=list(read_file)

header=apps_data[0]
appsdata=apps_data[1:]
rating_sum=0.00
for row in appsdata:
    rating = float(row[8])
    rating_sum+=rating
print("rating sum = ",rating_sum)