import pandas

df = pandas.read_excel(r"C:\Users\Emiza\Downloads\mithila Phy Adt 29-08-23.xlsx")
list1 = []
for i in range(len(df['Row Labels'])-1):
    list1.append(df['Row Labels'][i])

print()