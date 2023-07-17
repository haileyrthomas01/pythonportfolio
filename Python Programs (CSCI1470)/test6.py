user_input = input('Enter phone number: ')
phone_number = ''

nums = ['1','2','3','4','5','6','7','8','9','10','11',
       '12','13','14','15','16','17','18','19','20',
       '21','22','23','24','25','26']

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
               'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def convert():
    if user_input == alphabet[0] or user_input == alphabet[1] or user_input == alphabet[2]:
        phone_number += 1
    return phone_number

convert()
