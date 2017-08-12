# Sentimental_Analysis_Demenetization
We have done a sentimental Analysis on demonetization that took on 8th November 2016 our main aspect was to understand from people point of view how it effected in a positive or a negative manner
a) In this i have attached 2 python script , Requirements  :
1. analyse.py 
-- This script is used to extract data from the twitter using their API
2 . pandas-plot.py
-- This script is used to produce graphs from the csv files 

 b) There are two graphs that would be plotted from two csv files one demonetization.03.csv(figure_1.png)  and other one would be demonetization.04.csv(figure_2.png)

c ) there is a file README.md which contains all the data to run this script in your system

# twitter-sentiment
A command line utility to analyse twitter sentiment for any given topic and writes output to a CSV file.

## Installing
```
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
create a `.env` file and with the following contents
```
CONSUMER_KEY=<consumer key here>
CONSUMER_SECRET=<consumer secret here>
ACCESS_TOKEN=<access token here>
ACCESS_TOKEN_SECRET=<access token secret here>
```

## Running
```
(venv) $ ./analyse.py [query] [outfile] --threshold [threshold] --limit [limit]
```
For eg.
```
(venv) $ ./analyse.py “demonetization” demonetization.csv --threshold 0 --limit 5 
```
