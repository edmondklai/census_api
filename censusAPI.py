import urllib.request
import ast
from config import API_KEY


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

