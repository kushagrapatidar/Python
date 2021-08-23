row= list()

#row-1
row.append(['Faacebook',0.0,'USD',2974676,3.5])

#row-2
row.append(['Instagram',0.0,'USD',2161558,4.5])

#row-3
row.append(['Clash of Clans',0.0,'USD',2130805,4.5])

#row-4
row.append(['Temple Run',0.0,'USD',1724546,4.5])

#row-4
row.append(['Pandora-Music&Radio',0.0,'USD',1126879,4.0])

data=dict()

colmn=list()
for i in range(len(row)):
    colmn.append([row[0][i],row[1][i],row[2][i],row[3][i],row[4][i]])

data['Track_name']=colmn[0]
data['Price']=colmn[1]
data['Currency']=colmn[2]
data['Rating_count_tot']=colmn[3]
data['User_rating']=colmn[4]

print('Track_name\t\t Price\t Currency\t Rating_count_tot\t User_rating')

for i in range(len(data['Track_name'])-1):
    print(data['Track_name'][i],'\t\t',data['Price'][i],'\t',data['Currency'][i],'\t\t',data['Rating_count_tot'][i],'\t\t',data['User_rating'][i])
print(data['Track_name'][4],'\t',data['Price'][4],'\t',data['Currency'][4],'\t\t',data['Rating_count_tot'][4],'\t\t',data['User_rating'][4])
print(len('\t\t'))