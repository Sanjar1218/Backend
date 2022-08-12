import requests
url = 'https://api.telegram.org/bot'
token = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'
update_id = -1
while True:
    r = requests.get(f'{url}{token}/getUpdates')
    if r.status_code==200:
        result = r.json()['result'][-1]
        print('restul: ', result)
        if update_id != result['update_id']:
            update_id = result['update_id']
            chat_id = result['message']['chat']['id']
            text = result['message']['text']
            if text=='stop':
                break
            payload = {'chat_id':chat_id, 'text':text}
            ask = requests.get(f'{url}{token}/sendMessage', params=payload)
            print(ask.status_code)