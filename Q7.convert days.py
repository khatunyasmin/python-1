a=int(input("Enter tha value of days:"))
year=a/365
Weeks=(a%365)/7
days=(a%365)%7
print("convert value day to year is",year)
print("convert value day to week",Weeks)
print("convert value days to day",days)