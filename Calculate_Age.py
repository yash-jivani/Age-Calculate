
import datetime

# try-excepts -> handling user inputs

today = datetime.date.today()  # today's date (YYYY,MM,DD)
try:
    dob_y = int(input('[ YYYY ] Year of birth: '))
    dob_m = int(input('[ MM ] Month of birth: '))
    dob_d = int(input('[ DD ] Date of birth: '))
except:
    print('[-] Invaild input !')
    exit()

def monthToYear(month): # convert month to year 
    
    year = 0
    
    while month>0:
        month-=12    # total_month-12 = month 
        year+=1     # year = 1

    if month<0:  # if month => negative 
        year = year-1   # year - 1
        month = 12 + month   # add to 12 

    return month,year  # return tuple 

try:
    userDOB = datetime.date(dob_y, dob_m, dob_d)   # convert <str> to <datetime.date> class
except:
    print('[-] Invaild date of birth !')
    exit()

total_month = (today.year - userDOB.year)*12 + today.month - userDOB.month  # cal-months
total_year = today.year - userDOB.year  # cal-years
total_days = (today-userDOB).days  # cal-days
total_weeks = total_days/7
res_month,res_year = monthToYear(total_month)   # tuple unpacking

if total_days < 0:
    print('\n[!] You are not yet born !\n')
    exit()

print(f'\n[+] Your age is => {res_year} Year, {res_month} Months ')

ans = input("\n[!] Press 'y' to view more info : ")
if ans.lower()=='y':
    print(f'\n* Total Year => {res_year}\n* Total Month => {total_month}\n* Total Days => {total_days}\n* Weeks => {total_weeks}\n')
else:
    print('Quitting !\n')
