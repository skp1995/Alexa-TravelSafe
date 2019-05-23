import requests
import json
# url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations"


def getPrecp():
    url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:85281&datatypeid = 'HPCP'&units=metric&startdate=2017-12-01&enddate=2017-12-01"
    headers = {'token': 'vOjZaFJddviHVVMMSiAYWTWLNVMNEJhf'}
    response = requests.get(url, headers = headers).json()
    precp = 0.0
    count = 0
    if len(response) != 0:
        response = response['results']
        for r in response:
            print(r)
            if r['datatype'] == "PRCP":
                count +=1
                precp += float(r['value'])
        print(precp/count)

getPrecp()