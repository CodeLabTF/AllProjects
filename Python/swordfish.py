
while True:
    print("Whats your name?")
    name = input()
    if name != 'Konserv':
        continue
    print("Hello Konserv. Whats the password?")
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

