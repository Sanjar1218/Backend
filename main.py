
import requests
import json
from pprint import pprint
 
def get_male_data(file_name = 'data.json', n=1):
    if file_name.find('json')==-1:
        f = open(file_name+'.json', 'w')
    else:
        f = open(file_name, 'w')

    i=0;
    lst = []
    dct = {} 
    while i<n:

        r = requests.get('https://randomuser.me/api')
        # print(r.json())
        if r.status_code==200:
            data = r.json()
            result = data['results'][0]
            dct ={} 
            if result['gender'] == 'male':
                i+=1
                print(i)
                dct['first_name']=result['name']['first']
                dct['last_name']=result['name']['last']
                dct['city'] = result['location']['country']
                dct['age'] = result['dob']['age']
                lst.append(dct)
    dct1 = {'results':lst}
    json.dump(dct1, f, ensure_ascii=True, indent=2)
    f.close()

get_male_data('data1', 100)