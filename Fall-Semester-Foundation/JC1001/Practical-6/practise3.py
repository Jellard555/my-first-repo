userProfile = {"name": "JP","age": "25","number of cats": 12,"city": "Bristol"}
theKeysIwant = ["name","number of cats"]
merged = {k : userProfile[k] for k in theKeysIwant}
print(merged)