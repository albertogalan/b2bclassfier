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
cd analysis
python -W ignore ./data_analysis.py
cd ..
