# census_api
This is a census python class that design to make downloading data from the U.S. Census Bureau much easier using the Census API.  The class is still a work in progress therefore it has not been fully tested and has limited functionality. The disclaimer is that this is my first python/programming project therefore if you see something wrong or does not conform to the python convention, feel free to drop me a message and let me know.  

## How to use the code

### Obtain API KEY 
First, you will need to get a API key from the U.S. Census Bureau, you can obtain the API key at this link. Or getting more information about how to use the Census API.  
https://www.census.gov/developers/


### Construct an instance
Next is to construct an instance using the Census class
```python
    census = my_Census(API_KEY)
```

### Set parameters
After a census instance is created, you must set the different parameters you wish to download from the Census Bureau, there are four parameters that must be set in order to successfully download the data.  They are **survey**, **year**, **variable**, and **geographic location**.  

**SURVEY** is which survey you're interested in getting the data from, for example they can be American Community Survey 5 years estimate or Centennial Survey.  They can be lookup at https://api.census.gov/data.html.

**YEAR** is which year the suvey is from, year can be look up at the above link.

**VARIABLES** is the variables that you're interested in downloading from the Census Bureau.  For example, they can be Population, Median Household Income.  Variables is represent by name or an unique identifier, it can be look up at the above link.

**GEOGRAPHIC LOCATION** is which geograhic level set for the data, they can be at state level, county level, census tract level or other geographic unit available for that particular survey.  


```python
    year = "2015"
    survey = "acs5"
    fields = ["NAME",
              "GEOID"]
    geoFilter = ["for=block+group:*",
             "in=tract:*",
             "in=county:19",
             "in=state:17"]

    census.set_year(year)
    census.set_survey(survey)
    census.set_field(fields)
    census.set_geoFilter(geoFilter)
```

Currently, the input only take the format:
-year must be a string
-survey must be a string
-fields must be a list of string
-geoFilter must be a list of string 



The above code is set the parameter to the American Community Survey 5 years estimate for 2015.  The variables that will be download are the names and GEOID for Illinois(17), Champaign County(19), all census block groups in all census tract(*).

### Download the data
Once the parameter is set, use the following method to download the data.

```python
    census.download_data()
```

### Examine the data
Currently, you can examine the data using the following method which will display the head of the data and a summary table for the data.

```python
    census.head()
    census.summary()
```

### Export and Import Data
Currently only support export to CSV file and TXT file.  Import from TXT file.  

```python
    census.exportData(fileName, fileType)
    census.importData(fileName, fileType)

```

fileName is the input or output file name
fileType is the format the input or output file is in.  Currently only support "TXT", "CSV"




### Data Manipulation and Calculation
This is currently under development and features about manipulating the data will be added later on.  Any suggestions are welcome.




