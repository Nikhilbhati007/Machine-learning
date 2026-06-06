import requests
response=requests.get("https://django-rapid-api.herokuapp.com/")

print(respone.status_code)
#error code:301,400,401,404,503
res=json.loads(response.text)
for i in res:
    print(i)