#!/usr/bin/python
import requests
import json
import time

nifi_url='http://172.25.40.138:9090/'
pg_name='Ray'
search_api='nifi-api/flow/search-results?q='
pg_api='nifi-api/flow/process-groups/'
pg_api_suffix='/controller-services'

def pg_search(pg_name):

    url = nifi_url+search_api+pg_name
    req_out = requests.get(url)
    json_out = req_out.json()
    print(json_out)

    for i in json_out['searchResultsDTO']['processGroupResults']:
        if i['name'] == pg_name:
            return i['id']
        break

def cs_search(pg_id):

    url = nifi_url+pg_api+pg_id+pg_api_suffix
    req_out = requests.get(url)
    json_out = req_out.json()
    print(json_out)
    cs_dic={}
    for i in json_out['controllerServices']:
        if i['component']['name'] == 'DRHiveConnectionPool':
            cs_dic[i['id']]=i['component']['properties']['hive-db-user']
        return cs_dic


def main():

#1. Get the first PG name from input.csv

#2. Search results for the PG

     pg_id = pg_search(pg_name)

#3. Find controller services ID for that PG ID where name of Controller service is DRHiveConnectionPool

     cs_id = cs_search(pg_id)

#4



if __name__ == "__main__":
     main()
