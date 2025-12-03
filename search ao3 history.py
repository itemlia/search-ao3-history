import pandas as pd
ao3History = pd.read_excel("c:/Users/lhara/Documents/ao3_expanded1.xlsx", thousands=',')

global topOrBottom

global sort

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

    if topOrBottom == 1:
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
        print("thanks for searching :)")


def wordcountAscending():
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
    else:
        print("not a valid answer - please retype: ")
        answer0 = input()
    
    values = ao3History["wordcount"].sort_values
    result = pd.Series(values)
    
    k = topAmount

    if topOrBottom == 1:
        top = result.head(k)
    else:
        top = result.tail(k)

    if k > len(result):
        print("top amount value too large please enter new one: ")
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
        print("thanks for searching :)")


def checkSort():
    print("would you like to search top amounts or bottom amounts?")
    answer0 = input()

    if answer0 == "top":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        topOrBottom = 1
        searchHistory(column, topAmount)
    elif answer0 == "bottom":
        print("enter amount to be searched: ")
        topAmount = input()
        topAmount = int(topAmount)
        topOrBottom = 0
        searchHistory(column, topAmount)
    else:
        print("not a valid answer - please retype: ")
        answer0 = input()


if column == "wordcount":
    print("would you like to order wordcount in ascending order?")
    answer00 = input()
    if answer00 == "yes":
        wordcountAscending()
    else:
        checkSort()
else:
    checkSort()
