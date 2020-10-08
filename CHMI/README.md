
# original script is coming from Martin Matej Github 
- https://github.com/manmatej/chmu-process
- data available to download via script in his repository



## Series of scripts to handle CHMU data

### Poloha stanic merge
This script build upon Oto Kalab’s one, you can find here https://github.com/kalab-oto/chmu-poloha-stanic Use this script to merge into single file and filter duplicates. The output is also in this repository. You can simply download to proceed with downloading data. (stanice_ids.csv)

### Downloading script
To run this one, you need ids of stations. You can process them yourself or use “stanice_ids.csv” Script will download I hope all data, or you can decide which data. See: http://portal.chmi.cz/historicka-data/pocasi/denni-data/Denni-data-dle-z.-123-1998-Sb.#  
Result is bunch of zip files. 

### Unzip process
This one will handle downloaded zips. Only mean air temperature as example. Unzip, and process into flat data frame starting 01.01.1961 ending 31.01.2019. There are a lot of missing data, individual station vary in logging period. All data are merged together. 
See airTmean.jpg to check missing data. X axis = date, Y axis = station ID 