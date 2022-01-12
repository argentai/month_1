from datetime import datetime

birthday = input("Enter your date of birth: ")

bday = datetime.strptime(birthday, '%d/%m/%Y')

print(f'Day: {bday.day}')
print(f'Month: {bday.month}')
print(f'Year: {bday.year}')
