import pandas as pd
ao3History = pd.read_excel("c:/Users/lhara/Documents/ao3_expanded1.xlsx", thousands=',')

ao3History["wordcount"].astype(float)

totalWordcount = ao3History["wordcount"].sum()
print("total wordcount =", totalWordcount)

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
    k = topAmount
    top = result.head(k)

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
        print("enter new column to be searched: ")
        newColumn = input()
        print("would you like to search a new top amount?")
        answer2 = input()
        if answer2 == "yes":
            print("enter new top amount to be searched: ")
            newTopAmount = input()
            searchHistory(newColumn, newTopAmount)
        else:
            searchHistory(newColumn, topAmount)
    else:
        print("would you like to search a new top amount?")
        answer3 = input()
        if answer3 == "yes":
            print("enter new top amount to be searched: ")
            newTopAmount = input()
            searchHistory(column, newTopAmount)
        else:
            print("thanks for searching :)")


searchHistory(column, topAmount)