A B2B domain Classifier 



# Problem

You want to find customers, but where are they?

==== 


What do you do ?

- Find a in a database
- Search in google

======


This is half of your time

=====


# Solution The Anteater

- Find a customer is hard, as find ants

    =========


- You can do it yourself 
           
           or 

- you can get an Anteater


=====  ======

Demo(video):

= =  = == =  = = =

- Give me 10 customers, I give you 50 customers

- Or give 1000 leads and I give you the top 10th 

====  =======

How do we make money? 

PaaS  Pay as a Service

- Basic  -- Freelancers   50$/month 100 results
- Business  -- Small medium Size Companies  399$/month  1000 results
- Cooporate  -- Corporate    1200$/month 4000 results

100 customers = 20.000 $/month

===========

One company in Chemical industry 200 employees in China , 
want to search international customers

6000 $ for a database
4 months of salary for a marketing guy.

Our solution

We give Better results, cheaper results, faster results

============


Our vision

This is a unique service non-given by other suppliers
Scale up in China, Europe and USA

=============

Automatically give pick up 

what are the keywords
Provide the domains


===============







## A Massive Lead Classification 

- Validation potential customers base on the domain
- We use Web scraping and NLP classification techniques to resolve the problem massively

## Features

- Validate domains across different countries
- Validate domains in different languages
- Automatic testing if samples are good
- Output the domains are potential customers
- Scalable 
- Multiplatform ( Linux, Windows, Mac )



## How to install

`git clone git@github.com:albertogalan/b2bclassfier.git`

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

### Validate domains

`cd analysis`
`python3 domain-validation.py  --file customers.csv --filecheck leads.csv --output output.csv`

customers.csv is the frequency file of the existing customers

leads.csv is the frequency file of the domains to be validated


Company A has 200 customers , 

- Provides us the domain of each customer in to our service

domain01.org

domain02.org

domain03.org

Provides us some relevant keywords about their customers and products


He provides a list of domains 

We check every domain


