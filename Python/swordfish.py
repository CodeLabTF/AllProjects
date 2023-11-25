
while True:
    print("Whats your name?")
    name = input()
    if name != 'admin':
        continue
    print("Hello. Whats the password?")
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

