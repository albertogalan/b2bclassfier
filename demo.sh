#!/bin/bash 
echo "SCRAPPING CUSTOMERS"
echo "...."
echo "...."
./scraping/scrap.sh ./data/democompany.txt
echo "SCRAPPING LEADS"
echo "...."
./scraping/scrap.sh ./data/demoleads.txt

echo "DOING ANALYSIS OF LEADS"
echo "...."
python -W ignore ./analysis/data_analysis.py
