Kepler planet detector classroom activity
=========================================

The python script and accompanying materials comprise an undergraduate or high school-level (computer) laboratory activity in which students discover extrasolar planets by fitting a toy planetary transit light curve model to real data from [NASA's Kepler space telescope](http://www.nasa.gov/mission_pages/kepler/main/index.html).

## Concepts addressed ##

* Exoplanets
* Solar/planetary system structure
* Planet detection
* Model fitting
* Data analysis
* Telescope observations

## Usage ##

Instructors can generate new html/javascript webpages for a specific Kepler star using the script getKID.py, or just use the pre-made light curve pages available [here](http://www.people.fas.harvard.edu/~nsanders/lab2/lab2.htm).

The document "Lab Manual.pdf" includes a description of and manual for the activity for students, including questions to discuss in a laboratory report.

## getKID.py ##

To use this script getKID.py, execute a command as follows:

	python getKID.py KID width1 width2 temp radius

Where the parameters are:

* KID is the Kepler ID number for the target object
* width1 is number of days to save for detrended data (defaults to 50 days -- larger numbers increase page load time)
* width2 is number of days for raw data (defaults to 100 days)
* Temp is temperature of star (to print on the web page)
* Radius is radius of star (to print on the web page)

You can [lookup information on candidate Kepler stars on the Kepler website](http://archive.stsci.edu/kepler/planet_candidates.html)

The script will download the raw Kepler data for the specified KID, perform some basic data reduction / detrending, and output a directory with an html/javascript page and associated data files, suitable for posting on a webserver.



