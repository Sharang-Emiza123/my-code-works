import pandas as pd, statistics as st

df = pd.read_csv(r"C:\Users\Emiza\Downloads\SMconsumer-Aug23-SO.csv")

soids = []

for i in range(len(df['soID'])-1):
    soids.append(df['soID'][i])

itemids = []

for i in range(len(df['ItemId'])-1):
    itemids.append(df['ItemId'][i])


maxItem = max(itemids, key=itemids.count)
count = itemids.count(maxItem)

dict1 = dict()

for i in range(len(df['ItemId'])):
    dict1[df['CreatedDate']]


# print(len(sumofitem.keys()))
# print("total products dispatched ",sum(df['TotalDispatched']))        
print(df['CreatedDate'])
# print(df['CreatedDate'][0])
# print("most sold SKU is {0} sold {1} items.".format(maxItem, count)) 
# print("number of SOs processed -",len(list2))
