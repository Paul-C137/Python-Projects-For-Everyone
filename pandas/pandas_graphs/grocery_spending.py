#!/usr/bin/python3

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    excel_file = 'Spending_2023.xlsx'
    df = pd.read_excel(excel_file)
    # The sheet was called Groceries so it named the first column
    # Groceris.  Rename all the columns like shown below.
    df = df.rename(columns={'Unnamed: 1': 'Amount', 'Groceries' : 'Date'})
    # print the df and see that the columns were renamed
    print(df)
    # sometimes you may have to change the type of data in a column
    df['Amount']=df['Amount'].astype(int)
    # .plot() returns an object with attributes we can modify.
    # give the object a name and modify the attributes all you want
    # you can use the title keyword argument to add a title to the plot
    ax = df.plot(x='Date', y='Amount', title='Grocery Spending')
    ax.set_ylabel('Dollars')
    ax.set_xlabel('')
    # save the graph to a directory for later retrieval
    plt.savefig('graphs/grocery_spending_line.png')

if __name__ == "__main__":
    main()