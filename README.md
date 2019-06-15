A B2B domain Classifier 


# What is this tool?
## Marketing tool to validate company domains if they are potential Customers 

# Problem to resolve

## Small and Medium size companies  don't have the necessary human resource to find new leads

# Solution 

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


