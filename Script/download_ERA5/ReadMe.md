# How to use this script to download the ERA5 data automatically
This profile includes 4 files, '**down_era5.sh**', '**monitor.sh**', '**month**', '**vars**'. Their function will be descriped below.
> These scripts are suitable for the linux machine. 
* '**month**'  
This file sets the specific month number you need to download, including "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12".
> Attention 1: you ought to set the month number accroding to what mentioned above.
* '**vars**'   
This file sets the specific vars name.
> Attention 2: the vars name are shown at the bottom of the CDS website.
* '**down_era5.sh**'  
1. This file will create the python script to download the ERA5 data, and if your favorate dataset is not the "reanalysis era5 single levels", you  
can copy the basic script from the CDS Website(https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=overview) 
API button in the bottom of the website when you have chosen all the information you need.
2. Specific sets are shown in the script.
* '**monitor.sh**'  
This script monitors the downloading status. The Specific sets are shown in the script.
* Run
```
nohup bash monitor.sh  > monitor.log 2>&1 &
```
The results are stored in the "monitor.log" in the same dir. And the dirs "down_py"(python scripts), "log"(downloading log) and "ERA5"(Store  
the data) will be established automatically.
> Attention 3: You should copy all these four files into your own path.   
> Before you run:  
> * Check the dir site where you want to create  
> * Check the years, month and vars  
> * Check the dataset python script sample for the CDS website  
> * Evaluate the size of each data files, so you can set the suitable sleep time.
