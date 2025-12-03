import pandas as pd
ao3History = pd.read_excel("c:/Users/lia/Documents/ao3_expanded1.xlsx", thousands=',')

global gTopOrBottom

global sort

ao3History.dropna(inplace=True)

ao3History["wordcount"].astype(float)

totalWordcount = ao3History["wordcount"].sum()
print("total wordcount =", totalWordcount)

print(ao3History.columns)
print("enter column to be searched: ")
column = input()



def searchHistory(column, topAmount):

    values = ao3History[column].values
    toSearch = pd.Series(values)
    result = toSearch.value_counts()
    k = topAmount

    if gTopOrBottom == 1:
        top = result.head(k)
    else:
        top = result.tail(k)

    if k > len(result):
        print("amount value too large please enter new one: ")
        topAmountRedo = input()
        topAmountRedo = int(topAmountRedo)
        searchHistory(column, topAmountRedo)
    else:
        print(top)

    print("would you like to search a new column?")
    answer = input()

    if answer == "yes":
        print("please enter a new column: ")
        newColumn = input()
        searchHistory(newColumn, topAmount)
    else:
        print("thanks for searching!")


def wordcountAscending():

    sortedHistory = ao3History.sort_values(by='wordcount',ascending=False)

    print("would you like to search top amounts or bottom amounts?")
    answer0 = input()

    if answer0 == "top":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        topOrBottom = 1
    elif answer0 == "bottom":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        topOrBottom = 0    
    
    values = sortedHistory["wordcount"].values
    result = pd.Series(values)
    
    k = topAmount

    if topOrBottom == 1:
        top = result.head(k)
    else:
        top = result.tail(k)

    print(top)

    print("would you like to search a new column?")
    answer = input()

    if answer == "yes":
        print("please enter a new column: ")
        newColumn = input()
        searchHistory(newColumn, topAmount)
    else:
        print("thanks for searching!")


def checkSort():
    global gTopOrBottom

    print("would you like to search top amounts or bottom amounts?")
    answer0 = input()

    if answer0 == "top":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        gTopOrBottom = 1
        searchHistory(column, topAmount)
    elif answer0 == "bottom":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        gTopOrBottom = 0
        searchHistory(column, topAmount)

if column == "wordcount":
    print("would you like to order wordcount in descending numerical order?")
    answer00 = input()
    if answer00 == "yes":
        wordcountAscending()
    else:
        checkSort()
else:
    checkSort()
