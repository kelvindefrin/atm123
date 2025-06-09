a={
    "Name":"Kelvin",
   "Age":23,
   "Phone_number":9585266976,
   "Department":"MCA",
   "Address":"11/28 pozhikarai"
   }
a["Name"]="akash"
a["Age"]="32"
a["Phone_number"]=9999999999
a["Department"]="MCA"
a["Address"]="Puthalam"
#print(a["Name"])
#print(a["Age"])
#print(a["Phone_number"])
#print(a["Department"])
#print(a["Address"])
#a.clear()
#a.pop("Age")
#a.popitem()
#print(a)
for i, y in a.items():
    print(f"{i}:{y}")