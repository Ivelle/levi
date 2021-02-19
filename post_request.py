import requests

url = 'http://httpbin.org/post'
param = {'first_name': 'levi', 'second_name': 'kimani', 'age': '18'}


def post_request(url, param):
    response = requests.post(url, data=param)
    return response.text


print(post_request(url, param))
