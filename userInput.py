# input 
from datetime import date
#first_name= input("Enter your first name: ") 
#response= input("Are you enjoying") 
#print(f"Hi {first_name}, Thanks for your"
      #f" response {response}")

# Assignement 
today = date.today()
print(today.year)
birthday_date = int(input("your birth date?"))
birthday_month = int(input("your birth month?"))
birth_date = date(today.year,birthday_month,birthday_date )
print(birth_date)
if birth_date < today:
    birth_date= date(today.year +1,birthday_month, birthday_date)
days = (birth_date-today).days

print(f"Hi Cutee,you have {round(days/7)} weeks to go for your birthday :)")
