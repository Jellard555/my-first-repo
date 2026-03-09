c = 3*10**8
seconds = int(input("write a time in seconds"))
distance_m = seconds * c
distance_km = distance_m / 1000
distance_miles = distance_km * 0.6214
print(f"meters:{distance_m}m kilometers:{distance_km}km miles:{distance_miles}miles")