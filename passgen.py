import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$*"

all = lower + upper + numbers + symbols

length = 5

password = "".join(random.sample(all,length))
print(password)
