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



c = my_Census(API_KEY)
c.set_year("2015")
c.set_survey("acs5")
c.set_field(["NAME","B05010_001E"])
c.set_geoFilter(["for=tract:*", "in=county:19", "in=state:17"])
c.contruct_query()
c.get()
#c.get("2015", "acs5", "NAME,B05010_001E")


#
#dataset = b17010

"""
class Census:
    def __init__(self, key):
        self.key = key


    def get(self, fields, geo, year=2010, dataset='sf1'):
        fields = [','.join(fields)]
        base_url = 'http://api.census.gov/data/%s/%s?key=%s&get=' % (str(year), dataset, self.key)
        query = fields
        for item in geo:
            query.append(item)
        add_url = '&'.join(query)
        url = base_url + add_url
        print(url)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()




c = Census(API_KEY)
state = c.get(['P0010001'], ['for=state:25'])
# url: http://api.census.gov/data/2010/sf1?key=<mykey>&get=P0010001&for=state:25
county = c.get(['P0010001'], ['in=state:25', 'for=county:*'])
# url: http://api.census.gov/data/2010/sf1?key=<mykey>&get=P0010001&in=state:25&for=county:*
city = c.get(['P0010001'], ['in=state:25', 'for=place:*'])
# url: http://api.census.gov/data/2010/sf1?key=<mykey>&get=P0010001&in=state:25&for=place:*

# Cast result to list type
state_result = ast.literal_eval(state.decode('utf8'))
county_result = ast.literal_eval(county.decode('utf8'))
city_result = ast.literal_eval(city.decode('utf8'))

"""

