# Ant Eater 

## A Massive Lead Classification 

- Validation of potential customers base on the domain
- We use Web scraping and NLP classification techniques to resolve the problem massively

## Features

- Validate domains across different countries
- Validate domains in different languages
- Automatic testing if samples are good
- Output the domains are potential customers
- Scalable 
- Multiplatform ( Linux, Windows, Mac )

## How to install

`git clone git@github.com:albertogalan/anteater.git`

`pip3 install -r requirements.txt`

`cd scraping`

Create Selenium headless services on port 4444

`docker-compose up -d`


## How to use


### Scraping words frequency

`./test-list.sh ../data/company01.txt`

company01.txt is a file containing the information to scrap 

### company01 format
> freqcustomers  false customers.md "keyword1;keyword2;.."  "keysearch1;keysear2;keysearch3"
> freqdomaintovalidate  false domainstocheck.md "keyword1;keyword2;.."  "keysearch1;keysear2;keysearch3"

freqcustomers  is the output filename

freqdomaintovalidate  is the output filename

customers.md  list of customers domains

domainstocheck.md list of domains to check if they are potential leads

keyword1 ... are the keywords we want to find in the search engine something like:
   
   "site:domain.org  keyword"
    
keysearch1 ... are the keywords we want to check the frequency

list of domains that are actual customers

## Validate domains

`cd analysis`

copy the results of the scraping files in customers.csv  folder analysis

execute to analysis of customers

`python3 data_analysis.py ` 

customers.csv is the frequency file of the existing customers

>  Check leads if they are in cluster:  <16-06-19, agalan> > 
