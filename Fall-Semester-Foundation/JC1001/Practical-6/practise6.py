theKeysIwantToRemove = ["age","city"]
userProfile = {"name": "JP","age": "25","number of cats": 12,"city": "Bristol"}
merged = {}
for k,v in userProfile.items():
    if k  not in theKeysIwantToRemove:
        merged[k] = v
print(merged)