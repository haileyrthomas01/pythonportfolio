# minimum requirements:
# length >= 10
# min of 1 lowercase, uppercase, special chararcter, and number
# no other characters allowed

c, l, s, n = 0, 0, 0, 0

password = input('Enter password: ')
capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowletters = 'abcdefghijklmnopqrstuvwxyz'
specialchar = '!@#$%^&*()_+'
nums = '0123456789'

if (len(password) >= 10):
    for i in password:
        if (i in capletters):
            c+=1
        if (i in lowletters):
            l+=1
        if (i in specialchar):
            s+=1
        if (i in nums):
            n+=1

if (c >= 1 and l >= 1 and s >= 1 and n >= 1 and c + l + s + n = len(password)):
    print('Password is valid.')
else:
    print('Password invalid. Please try again.')