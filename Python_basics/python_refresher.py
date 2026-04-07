"""
User Input
"""

first_name = input ('Enter your FirstName:')
days =input('Enter how many days before your birthday:')
no_of_weeks_to_birthday = ((int)(days))/7
roundedweeks = round(no_of_weeks_to_birthday,2)
print(f'Hi {first_name}. Your birthday is coming up in { roundedweeks} weeks')