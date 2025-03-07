# Write code below 💖

import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 8, 25)
time_difference = next_birthday - today
days_away = time_difference.days 

if today == next_birthday:
  print(random_message)
else:
  print(f'My next birthday is {days_away} days away!')