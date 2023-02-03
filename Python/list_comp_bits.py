
bits = [False, True, False, False, True, False]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(bits)
print(new_bits)
