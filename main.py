import random
kios = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(_"
kiosl = 16
p = "".join(random.sample(kios, kiosl))
print(p)
