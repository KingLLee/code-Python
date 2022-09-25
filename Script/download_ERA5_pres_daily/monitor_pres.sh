#! /bin/bash

year_begin=2022
year_end=2022

echo "Open up the monitor"

while [[ ${year_end} -le 2022 ]];

do

	bash daily_pres.sh ${year_begin}  ${year_end}
	

	echo "sleep 30 min, keep running"
	
	#sleep 30m
	
	echo "${year_begin}-${year_end} done!"
	
	#processID=$(ps -ef | grep *.py | grep -v "grep" | awk "{print $2}")

	#rm -rf ./down_py/era5*
	#rm -rf ./log/era5*



	year_begin=$((${year_begin}+1))
	year_end=$((${year_end}+1))

done

	





echo "Work has been done!!!"

