import requests
r = requests.get('https://api.github.com/events')
data = r.json()
my_list=[]
for i,data in enumerate(data):
    my_list.append(data['actor']['login'])
print(my_list)