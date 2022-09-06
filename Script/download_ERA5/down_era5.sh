#! /bin/bash

# Input the parameters
year_begin=$1
year_end=$2

echo "Begin to download：$1 - $2 ERA5 data"

for var in `cat vars`

do

	mkdir -p  ./ERA5/${var}


	for year in `seq ${year_begin} ${year_end}`

	do
		for mon in `cat month`
		do
			# Naming convention
			filename=era5.hourly.${var}.${year}.${mon}

# Create specific python script, you can change the script below if you needed.
			cat>./down_py/${filename}.py<<EOF

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            '${var}',
        ],
        'year': [
            '${year}',
        ],
        'month': [
            '${mon}',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
        ],
    },
    './ERA5/${var}/${filename}.nc')

EOF

# run the python script and output the log file to specific dir.
nohup python ./down_py/${filename}.py  > ./log/${filename}.log 2>&1 &

		done
	
	done

done
