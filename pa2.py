#ask user to enter month and the year

month=int(input("Enter the month:"))
year=int(input("Enter the year:"))

if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28 or 29 days")
else:
    print("not valid")

#if the month is Feb see if it is a leap year
if (year%100==0 and year%400==0):
    print("29 days")
elif (year%100!=0 and year%4==0):
    print("29 days")
elif month in (1,3,5,7,8,10,12):
    print("not a leap year")
elif month in (4,6,9,11):
    print("not a leap year")
else:
    print("not a leap year")

print("end of code")












