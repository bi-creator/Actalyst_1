import requests
from datetime import datetime
currentime=str(datetime.now())
url = 'http://127.0.0.1:8000/streamData'
myobj = {'column_1':f"column_1 {currentime}", 'column_2':f"column_2 {currentime}", 'column_3':f"column_3 {currentime}",'column_4':f"column_4 {currentime}",'column_5':f"column_5 {currentime}"}
x = requests.post(url, json=myobj)
print(x)