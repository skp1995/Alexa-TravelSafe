from django.http import HttpResponse
from difflib import SequenceMatcher
from drivesafe.models import gps_coordinates
import datetime
import googlemaps
from googlemaps import convert
import requests
import json
import csv
# Create your views here.
def checkin(request):
    gps = request.GET.get('gps', '')
    if len(gps) == 0:
        return HttpResponse("error")
    else:
        temp = gps.split('~')
        t = gps_coordinates(time=datetime.datetime.now(), lat=temp[0], lon=temp[1])
        t.save()
        return HttpResponse("You sent me : "+ gps)


def respond(request):
    queryset = gps_coordinates.objects.all().order_by('-time')[:1]
    latest = str(queryset.get())
    latest = latest.split("~")
    parameters = ','.join(latest)
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+parameters+'&key=AIzaSyCIeAOMSMQAOyOHPpv-K36n8aRwSwZzMXI')
    response = r.json()
    response = response['results'][0]['address_components']
    print(response)
    ranks = {}
    fle = open('rank.csv', 'r')
    lines = fle.readlines()
    for line in lines:
        line = line.split(',')
        ranks[line[0]] = line[1]
    res_rank = 3
    s = ""
    for r_dict in response:
        if 'route' in r_dict['types']:
            for k,v in ranks.items():
                val = 0.9
                while True:
                    # print(val)
                    if val <= 0.2:
                        res_rank == 3
                        break
                    if SequenceMatcher(None, k, r_dict['short_name']).ratio() > val:
                        res_rank = int(ranks[k])
                        break
                    else:
                        val-=0.1
            #
            # print(r_dict['long_name'])
            # print(r_dict['short_name'])
            # if (r_dict['short_name'] in ranks):
            #     res_rank = int(ranks[r_dict['short_name']])
            # elif (r_dict['long_name'] in ranks):
            #     res_rank = int(ranks[r_dict['long_name']])

    print(res_rank)
    if res_rank == 3:
        s="I do not have any data for this location, I only keep track of bad roads, So probably this is safe "
    elif res_rank== 0:
       s= " This road is safe.There are no major fatal accidents reported here"
    elif res_rank==1:
       s="Caution advised .Few reported fatal accidents, please drive carefully. "
    elif res_rank==2 :
        s=" My Spider sense is tingling. Extreme caution advised. High rate of fatal accidents reported. Keep your eyes on the road "
    json_data = '{"msg": "'+s+'"}'
    res = json.loads(json_data)
    print(str(res))
    return HttpResponse(res)




