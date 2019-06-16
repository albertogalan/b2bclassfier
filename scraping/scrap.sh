#!/bin/bash


if [[ $# -eq 0 ]]; then
  echo "$red types=auto/manual  $reset"
  echo "Usage: ${FUNCNAME[0]} $green {testlist} $reset"
  exit 0
fi

TESTLIST=$1
MINCHAR=6
dir=$(pwd)
DATABASEDIR=$dir/data
LISTDIR=$dir/data
function tests(){

APPDIR=$dir
testname="$1"	
headless="$2"
list="$LISTDIR/$3"
searchkeys="$4"
keyword="$5"

# activate environment

$APPDIR/scraping/generaltests.py --file $DATABASEDIR/$testname --testname $testname --headless $headless --searchkeys "$searchkeys" --list "$list" --keyword "$keyword" 
}

while read f
  do
  if [ ${#f} -gt $MINCHAR  ]; then
     tests $f  	  
  else
  	echo less than $MINCHAR characters
  fi
done < $TESTLIST


