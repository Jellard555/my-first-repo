theKeysIwantToRemove = ["age","city"]
userProfile = {"name": "JP","age": "25","number of cats": 12,"city": "Bristol"}
#merged = {k : userProfile[k] for k in userProfile
#if not in theKeysIwantToRemove}
#print(merged)
merged = {k:v for k,v in userProfile.items()
if k not in theKeysIwantToRemove}
print(merged)