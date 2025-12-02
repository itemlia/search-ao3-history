import pandas as pd
ao3History = pd.read_excel("C:/Users/lia/Documents/ao3_expanded1.xlsx")

print(ao3History.columns)
print("enter column to be searched: ")
column = input()
print("enter top amount to be searched: ")
topAmount = input()
topAmount = int(topAmount)

def searchHistory(column, topAmount):
    values = ao3History[column].values
    toSearch = pd.Series(values)
    result = toSearch.value_counts()
    k=topAmount
    top = result.head(k)
    print(top)

    print("enter new column to be searched: ")
    newColumn = input()

    searchHistory(newColumn, topAmount)

searchHistory(column, topAmount)
