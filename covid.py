import sys
import requests
import json
import urllib.request

def get_http_request(country):
    get = ('https://corona-stats.online/{}/?format=json'.format(country))
    data = urllib.request.urlopen(get).read().decode()
    obj = json.loads(data)
    #print(obj)
    #print('$ ' + obj['data'])
    for i in obj['data']:
        print("STATUS".center(40, "-"))
        print("Country:\t",i['country'])
        print("All Cases:\t",i['cases'])
        print("All Deatch:\t",i['deaths'])
        print("Cases Today:\t",i['todayCases'])
        print("Deatch Today:\t",i['todayDeaths'])

def check_connection():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout = timeout)
    except(requests.ConnectionError, requests.Timeout) as e:
        print("No Internet connection")
        sys.exit()

if __name__ == '__main__':
    check_connection()
    country = str(input("Country Name: "))
    get_http_request(country)
