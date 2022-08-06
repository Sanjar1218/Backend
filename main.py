
import requests
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
        try:
            r = requests.get('https://randomuser.me/api').json()
            # print(r.json())
            result = r['results'][0]
            

            if result['gender'] == 'male':
                i+=1
                print(i)
                dct['first_name']=result['name']['first']
                dct['last_name']=result['name']['last']
                dct['city'] = result['location']['country']
                dct['age'] = result['dob']['age']
                lst.append(dct)
        except:
            print('e')
            continue
    f.write(str(lst))

get_male_data('data1', 100)