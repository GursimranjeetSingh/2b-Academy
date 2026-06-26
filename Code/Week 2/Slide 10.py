s = 'Python'

# P y t h o n
# idx 0 1 2 3 4 5
# neg -6 -5 -4 -3 -2 -1

print(s[0])     # P
print(s[-1])    # n
print(s[1:4])   # yth
print(s[::-1])  # nohtyP (reverse!)
print(s[::2])   # Pto
print(len(s))   # 6




##############################################################################


s = ' Hello, World! '

print(s.strip()) # 'Hello, World!'
print(s.upper()) # ' HELLO, WORLD! '
print(s.lower()) # ' hello, world! '
print(s.replace('Hello', 'Hi')) # ' Hi, World! '
print(s.split(',')) # [' Hello', ' World! ']
print(s.find('World')) # 8 (index) or -1
print(s.startswith(' H')) # True
print(s.count('l')) # 3
