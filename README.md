A B2B domain Classifier 


# What is this tool?
## Marketing tool to validate domains if they are potential Customers for B2B companies 

# Problem to resolve

## Small and Medium size companies  don't have the necessary human resource to find new leads

# Solution 

## A Massive Lead Classification 

- We create a solution to validate potential customers base on the domain
- We use Web scraping and NLP classification techniques to resolve the problem massively

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
outputfile  false list.md "keyword1;keyword2;.."  "keysearch1;keysear2;keysearch3"

outputfile  is the output filename

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


