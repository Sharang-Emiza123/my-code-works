from collections import OrderedDict
import pandas as pd, statistics as st

# df = pd.read_excel(r"C:\Users\Emiza\Downloads\SMconsumer-Aug23-SO.xlsx")
df = pd.read_excel(r"D:\Users\shara\Downloads\SMconsumer-Aug23-SO.xlsx", parse_dates=['CreatedDate'])

list1 = []
list2 = []
for i in range(len(df['soId'])-1):
    list1.append(df['soId'][i])


for i in list1:
    if i not in list2:
        list2.append(i)

dates = dict()

for i in range(len(df['soId'])):
    dates[df['soId'][i]] =  df['CreatedDate'][i]

# print(df['CreatedDate'])

for i, j in dates.items():
    print("SO with ID - {0} processed on {1}".format(i,j)) 

# itemid = []

# for i in range(len(df['ItemId'])):
#     itemid.append(df['ItemId'][i])

# count = itemid.count('TOR3') 


# print(count)
print(len(dates.keys()))
# print(list2)

# print("total products dispatched ",sum(df['TotalDispatched']))        
# print(len(list1))
# print("number of SOs processed -",len(list2))