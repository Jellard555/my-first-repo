userProfile = {"name": "JP","age": "25","number of cats": 12,"city": "Bristol"}
theKeysIwant = ["name","number of cats"]
merged = {}
for k,v in userProfile.items():
    if k in theKeysIwant:
        merged[k] = v
print(merged)