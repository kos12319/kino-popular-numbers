import requests
import json
import operator
from collections import Counter
#εύρεση όλων των κληρώσεων για τις πρώτες δέκα μέρες
for i in range (1,10):
  l=[]
  for j in range (1,19):
    for k in range (0,10):
      day=i
      num=j
 #διεύθυνση όπου βρίσκουμε winning numbers    
      a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-0{day}/2021-02-0{day}?page{num}")       
      b=json.loads(a.content)
 #εύρεση winning numbers    
      c=(b["content"][k]["winningNumbers"]["list"])
# εισαγωγή σε λίστα όλων των winning numbers της μέρας
      l.extend(c)
  print("--------------")
  print("--------------")
  d = Counter(l)
  print(d)
  print("--------------")
  print("most used number for day", i, "is",max(d, key=d.get))
#εύρεση όλων των κληρώσεων για τις υπόλοιπες μέρες     
for i in range (10,27):
  l=[]
  for j in range (1,19):
    for k in range (0,10):
      day=i
      num=j
      a=requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-{day}/2021-02-{day}?page{num}")       
      b=json.loads(a.content)
      c=(b["content"][k]["winningNumbers"]["list"])
      l.extend(c)
  print("--------------")
  print("--------------")
  d = Counter(l)
  print(d)
  print("--------------")
  print("most used number for day", i, "is",max(d, key=d.get))