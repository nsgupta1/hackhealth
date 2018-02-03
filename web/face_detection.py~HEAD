import requests
import json
import base64
'5359cde8ad'
emotions_headers = {'Ocp-Apim-Subscription-Key': '335dea58b93d4876a1fc177e71efdf2a'}
imgur_headers= {'Authorization': 'Bearer 988e6611d2eb4f9eb6584726553244666cc3f06c'}


def recognize(url):
    response = requests.post('https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize', json={'url':url},headers=emotions_headers)
    res = json.loads(str(response.content,'utf-8'))
    return res

def upload(file):
    res= requests.post('https://api.imgur.com/3/image',json={'image':file}, headers=imgur_headers)
    url = json.loads(str(res.content,'utf-8'))
    return url['data']['link']

if __name__ == '__main__':
    with open('img.jpg','rb') as f:
        res = upload(f)
        data = recognize(res)
        print(data)
