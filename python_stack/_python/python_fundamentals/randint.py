import random
def randint(min=0, max=100):
  range = max - min 
  return round(random.random() * range + min)

print(randint())
print(randint(max=50))
print(randint(min=50))
print(randint(min=50, max=150))
