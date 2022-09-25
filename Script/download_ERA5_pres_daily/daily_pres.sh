#! /bin/bash

year_begin=$1
year_end=$2

echo "Begin to download：$1 - $2 ERA5 data"

for var in `cat pres_var`
do

	mkdir -p  /mnt/group10109share/data/ERA5_for_vic/${var}


	for year in `seq ${year_begin} ${year_end}`
	do
		
		for mon in `cat month`
		do
			
			for day in `cat days`
			do

			filename=era5.hourly.${var}.${year}.${mon}.${day}

			cat>./down_py/${filename}.py<<EOF

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            '${var}',
        ],
        'pressure_level': [
            '100', '125', '150',
            '175', '200', '225',
            '250', '300', '350',
            '400', '450', '500',
            '550', '600', '650',
            '700', '750', '775',
            '800', '825', '850',
            '875', '900', '925',
            '950', '975', '1000',
        ],
        'month': [
            '${mon}',
        ],
        'year': [
            '${year}',
        ],
        'day': [
            '${day}',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
    },
    '/mnt/group10109share/data/ERA5_for_vic/${var}/${filename}.nc')

EOF

nohup python ./down_py/${filename}.py  > ./log/${filename}.log 2>&1 &

			done
		done
	
	done
	
#	echo "downloading: ${year} -- ${var}, and sleep 10m"
#	sleep 10m
	

done
