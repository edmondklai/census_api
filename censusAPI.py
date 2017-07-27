import urllib.request
import pandas
from config import API_KEY


class my_Census:
    def __init__(self, API_KEY):
        self.key = API_KEY
        self.censusURL = 'https://api.census.gov/data/'
        self.year = "2015"
        self.survey = "acs5"
        self.fields = []
        self.filter = []
        self.query = ""


    def get_API_KEY(self):
        print(self.key)


    def contruct_query(self):
        fields = ",".join(self.fields)
        criteria = "&".join(self.filter)
        baseQuery = "https://api.census.gov/data/{}/{}?get={}&{}&key={}".format(
            self.year,
            self.survey,
            fields,
            criteria,
            self.key
        )
        self.query = baseQuery
        print(self.query)



    def set_year(self, year):
        self.year = year


    def set_survey(self, survey):
        self.survey = survey


    def set_field(self, fields):
        for field in fields:
            self.fields.append(field)


    def set_geoFilter(self, filter):
        for criteria in filter:
            self.filter.append(criteria)


    def get(self):
        request = urllib.request.Request(self.query)
        response = urllib.request.urlopen(request)
        print(pandas.read_json(response))




