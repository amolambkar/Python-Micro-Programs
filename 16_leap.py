# author - Amol Ambkar 
# program to check
# year is leap
# or not

year = int(input("Year :"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
