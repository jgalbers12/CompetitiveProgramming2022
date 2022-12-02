import random

n = input()

print(n)
print("0 0")
for i in range(2, int(n)+1):
    t = random.randint(30, 50)
    n = random.randint(2t * 50, 2*t+50)
    print(f"{str(t)} 1 {i - 1} {str(n)}")