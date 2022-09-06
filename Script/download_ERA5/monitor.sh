#! /bin/bash

# This is the monitor script to monitor the era data download.

# Create dir
mkdir -p ERA5
mkdir -p down_py
mkdir -p log

# Set the time period
year_begin=1979
year_end=1985

echo "Open up the monitor"

# If you should download the data to the other end time, you can change the "2020" to another one.

while [[ ${year_end} -le 2020 ]];

do

  # Call the shell "down_era5.sh"
	bash down_era5.sh ${year_begin}  ${year_end}
	

	echo "sleep 40 min, keep running"
	
	# You can use the 'sleep' to adjust the period "year_begin - year_end" download time.
  sleep 40m  
	
	echo "${year_begin}-${year_end} finished!!!!!"
	

	# Set the length of the period
 
	year_begin=$((${year_begin}+7))
 
	year_end=$((${year_end}+7))

done



echo "Work has been done!!!"
