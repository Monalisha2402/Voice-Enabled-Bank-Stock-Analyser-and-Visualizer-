from pandas_datareader import data, wb
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt, plotly

AIG = pd.read_csv("AIG.csv")
AIG = AIG.set_index('Date')
GS = pd.read_csv("GS.csv")
GS = GS.set_index('Date')
C = pd.read_csv("C.csv")
C = C.set_index('Date')
BAC = pd.read_csv("BAC.csv")
BAC = BAC.set_index('Date')
BCS = pd.read_csv("BCS.csv")
BCS = BCS.set_index('Date')
HSBC = pd.read_csv("HSBC.csv")
HSBC = HSBC.set_index('Date')
JPM = pd.read_csv("JPM.csv")
JPM = JPM.set_index('Date')
WFC = pd.read_csv("WFC.csv")
WFC = WFC.set_index('Date')
WBK = pd.read_csv("WBK.csv")
WBK = WBK.set_index('Date')
MS =pd.read_csv("MS.csv")
MS = MS.set_index('Date')
TD = pd.read_csv("TD.csv")
TD = TD.set_index('Date')
ICE = pd.read_csv("ICE.csv")
ICE = ICE.set_index('Date')

banks = ["AIG","GS","C","BAC","BCS","HSBC","JPM","WFC","WBK","MS","TD","ICE"]


#CONCATNING ALL THE TABLES IN ONE TABLE ALONG AXIS =1

bank_stock = pd.concat([AIG,GS,C,BAC,BCS,HSBC,JPM,WFC,WBK,MS,TD,ICE] ,axis =1 , keys = banks)

#SET THE COULUMN NAME LEVEL

bank_stock.columns.names = ['banks' ,"stock info"]

#EDA - EXPLORATORY DATA Analysis.
# What was the max close price for each bank stock throughout the time period
#other way using crosssection technique :
''' bank_stock.xs(key = 'Close',axis =1 , level ="stock info") ---> stck info is the level we set just above it
we can use cross section methos if we want other wise normal methos is best

'''

def max_close_call():
    print("\n*************Max close call for all banks*******************\n")
    for tick in banks:   
        print(tick, bank_stock[tick]['Close'].max())
        print("*****************************")


def min_close_call():
    print("\n************Min close call for all banks*********************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['Close'].min())
        print("*****************************")

def max_open_call():
    print("\n************Max open call for all banks***********************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['Open'].max())
        print("*****************************")


def min_open_call():
    print("\n*************Min open call for all banks***********************\n")
    for tick in banks:  
        print(tick, bank_stock[tick]['Open'].min())
        print("*****************************")

def max_high_call():
    print("\n*************Max High call for all banks************************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['High'].max())
        print("*****************************")

def min_high_call():
    print("\n*************Min High call for all banks************************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['High'].min())
        print("*****************************")

def max_low_call():
    print("\n*************Max Low call for all banks*************************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['Low'].max())
        print("*****************************")

def min_low_call():
    print("\n***************Min Low call for all banks**********************\n")
    for tick in banks: 
        print(tick, bank_stock[tick]['Low'].min())
        print("*****************************")

def max_volume_call():
    print("\n**************Max volume call for all banks********************\n")
    for tick in banks: 
        print(tick, bank_stock[tick]['Volume'].max())
        print("*****************************")

def min_volume_call():
    print("\n**************min volume call for all banks********************\n")
    for tick in banks:
        print(tick, bank_stock[tick]['Volume'].min())
        print("*****************************")


'''  print the return for each bank 
use pandas pct_change for return value , this will take at close column
creating return dataframe using empty dataframe
'''
returns = pd.DataFrame()
for tick in banks:
    returns[tick+' Return'] = bank_stock[tick]['Close'].pct_change()


def all_banks_return():
    print("\n   ********************************Return for all banks************************************         \n")
    print(returns)   


'''  create pair plot using seaborn of return dataframe'''

# here we are indexing as at column index 0 we have nan value as 
#at that time there were mo returns and stock operation 
#therefore from colum 2 i.e index 1 we will start

def pair_plot_returns():
    sns.pairplot(returns[1:])
    plt.show()    



# plot will show citi group had huge cross in reccssion
# many kore story you can find



'''best and worst stock for all bank depends on the return , tell the time stamp

'''

def all_banks_min_return():
    print("\n***********min return**********\n")
    print(returns.min())

def all_banks_max_return():
    print("\n***********max return**********\n")
    print(returns.max())

def all_banks_average_return():
    print("\n***********average return**********\n")
    print(returns.mean())

def all_banks_std_return():
    print("\n***********std of return**********\n")
    print(returns.std())

# most of the date would be aroun 2009 as that was the economic crash as can bee seen in plots as well

def all_banks_best_date_of_return():
    print("\n***********Best return date **********\n")
    print(returns.idxmax())
    
def all_banks_worst_date_of_return():
    print("\n***********worst return date **********\n")
    print(returns.idxmin())



# to get displot of return for year let say what so ever given
#you can add bins=50 to increase bins in plot

def return_plot_for_choosen_date_BAC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['BAC Return'],color='red',bins=100)
    plt.show()


def return_plot_for_choosen_date_JPM():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['JPM Return'],color='red',bins=100)
    plt.show()

def return_plot_for_choosen_date_C():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['C Return'],color='red',bins=100)
    plt.show()

def return_plot_for_choosen_date_MS():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['MS Return'],color='red',bins=100)
    plt.show()


def return_plot_for_choosen_date_WFC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['WFC Return'],color='red',bins=100)
    plt.show()


def return_plot_for_choosen_date_HSBC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['HSBC Return'],color='red',bins=100)
    plt.show()

def return_plot_for_choosen_date_GS():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    sns.histplot(returns.loc[start_date:end_date]['GS Return'],color='red',bins=100)
    plt.show()


# yha loop ka ek kaam hai ki wo saaare plot ko ek ke uppr ek kr deta hai
'''
line plot showing close price for each bank for the entire time series
'''
def close_plot_for_all_bank():
    for tick in banks:
        bank_stock[tick]['Close'].plot(label=tick, figsize=(12,4))
    plt.legend()
    plt.show()

'''moving averages

plot the rolling 30 days average against the close price for some bank for some year
no. of days ko weekly moving average dekh skte aur bhi bahut kuch
agr bahut saare plot ek ke baad ek liko to wo super impose ho jaate hai
'''

def average_for_some_day_against_some_year_BAC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    BAC['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    BAC['Close'].loc[start_date:end_date].plot(label= 'BAC Close')
    plt.legend()
    plt.show()


def average_for_some_day_against_some_year_JPM():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    JPM['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    JPM['Close'].loc[start_date:end_date].plot(label= 'JPM Close')
    plt.legend()
    plt.show()


def average_for_some_day_against_some_year_C():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    C['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    C['Close'].loc[start_date:end_date].plot(label= 'C Close')
    plt.legend()
    plt.show()        


def average_for_some_day_against_some_year_GS():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    GS['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    GS['Close'].loc[start_date:end_date].plot(label= 'GS Close')
    plt.legend()
    plt.show()

def average_for_some_day_against_some_year_HSBC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    HSBC['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    HSBC['Close'].loc[start_date:end_date].plot(label= 'HSBC Close')
    plt.legend()
    plt.show()    


def average_for_some_day_against_some_year_MS():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    MS['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    MS['Close'].loc[start_date:end_date].plot(label= 'MS Close')
    plt.legend()
    plt.show()    


def average_for_some_day_against_some_year_WFC():
    start_date = input('input the start date in format YYYY-MM-DD')
    end_date = input('input the end date in format YYYY-MM-DD')
    window = int(input("enter how many days average you want"))
    plt.figure(figsize=(12,4)) # to strech the plot
    WFC['Close'].loc[start_date:end_date].rolling(window=window).mean().plot(label="moving average")
    WFC['Close'].loc[start_date:end_date].plot(label= 'WFC Close')
    plt.legend()
    plt.show()    

'''correlation of bank_stocks
sns.heat map ke andr jo likha hai wo df tha correlation ka'''

def stock_correlation_heat_map():
    sns.heatmap(bank_stock.xs(key='Close',axis=1,level = 'stock info').corr(),annot =True)
    plt.show()

