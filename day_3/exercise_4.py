work_hours = int(input('How many hours did you work: '))
pay_rate = int(input('What is your pay/hr: '))
print(' Your weekly earning is:', 
      work_hours * pay_rate)

year = int(input('Please enter how long you have lived:'))
hour = 60
day = 24 * hour
week = day * 7
month = week * 4
year_sec = month * 12
new_year_seconds = year * year_sec

if year < 101:
    print('You have lived for this long:', 
          new_year_seconds)
else:
    print('No one can live this long')

for n in range(1,6):
    print(n,n**0,n**1,n**2,n**3)