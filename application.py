import speech_recognition as sr , wikipedia, webbrowser, os, smtplib, datetime, pyttsx3
from voices import *
from stock_functions import *
from introduction_menu import *
from pandas_datareader import data, wb
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt, plotly
sns.set_style('whitegrid')

wish()
intro = "welcome to the world of stocks , i am your assistant for the stock market and can do simple task as per what you can see on your screen .Kindly choose the case by stating what you want to find out. Press any number and enter  when you are ready"
intro = intro.lower()
text_to_speach(intro)
introduction()
a = input("enter any number and press enter")
loop = "start"
while loop == "start":

    query = speech_to_text().lower()
    

    if "wikipedia" in query:
        text_to_speach("searching wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        text_to_speach("according to wikipedia")
        print(results)
        text_to_speach(results)

    elif "yahoo finance" in query:
        webbrowser.open("https://in.finance.yahoo.com/")

    elif "bombay stock exchange" in query:
        webbrowser.open("https://www.bseindia.com/")

    elif "economic times market"  in query:
        webbrowser.open("https://economictimes.indiatimes.com/markets")

    elif "world bank"  in query:
        webbrowser.open("https://www.worldbank.org/")

    elif "maximum close"  in query:
        max_close_call()

    elif "minimun close"  in query:
        min_close_call()

    elif "maximum open"  in query:
        max_open_call()

    elif "minimum open"  in query:     
        min_open_call()   
  
    elif "maximum high"  in query:
        max_high_call()

    elif "minimum high"  in query:  
        min_high_call()

    elif "maximum low"  in query:  
        max_low_call()
  
    elif "minimum low"  in query:
        min_low_call()

    elif "maximum volume"  in query:
        max_volume_call()

    elif "minimum volume"  in query:
        min_volume_call()

    elif "banks return"  in query:
        all_banks_return()

    elif "average return"  in query:
        all_banks_average_return()

    elif "maximum return"  in query:
        all_banks_max_return()

    elif "minimum return"  in query:
        all_banks_min_return()

    elif "standard deviation"  in query:
        all_banks_std_return()

    elif "worst"  in query:
        all_banks_worst_date_of_return()

    elif "best"  in query:
        all_banks_best_date_of_return()

    elif "return pair plot" in query:
        pair_plot_returns()

    elif "return plot of JP morgan"  in query:
        return_plot_for_choosen_date_JPM()

    elif "return plot of goldman"  in query:
        return_plot_for_choosen_date_GS()   

    elif "return plot of city"  in query:
        return_plot_for_choosen_date_C()

    elif "return plot of morgan stanley"  in query:
        return_plot_for_choosen_date_MS()   

    elif "return plot of wells"  in query:
        return_plot_for_choosen_date_WFC()   

    elif "return plot of hsbc"  in query:
        return_plot_for_choosen_date_HSBC()

    elif "return plot of bank of america"  in query:
        return_plot_for_choosen_date_BAC()

    elif "close plot"  in query:
        close_plot_for_all_bank()

    elif "average plot for JP morgan"  in query:
        average_for_some_day_against_some_year_JPM()

    elif "average plot of goldman"  in query:
        average_for_some_day_against_some_year_GS()   

    elif "average plot of city"  in query:
        average_for_some_day_against_some_year_C

    elif "average plot of morgan stanley"  in query:
        average_for_some_day_against_some_year_MS()   

    elif "average plot of wells"  in query:
        average_for_some_day_against_some_year_WFC()

    elif "average plot of hsbc"  in query:
        average_for_some_day_against_some_year_HSBC()

    elif "average plot of bank of america"  in query:
        average_for_some_day_against_some_year_BAC()   

    elif "heat map"  in query:
        stock_correlation_heat_map()                
                 
    text_to_speach("do you want me to continue my service or not , say start to continue and stop to stop, see menu again and anter number and hit enter to start") 
    introduction()
    b = input("enter any number and press enter and say your choice")
    counter = speech_to_text()
    if ("start" or "Start") in counter:
        loop = "start"
    else:
        loop = "stop"   
         
