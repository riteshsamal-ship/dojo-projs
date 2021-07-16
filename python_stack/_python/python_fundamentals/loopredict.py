for i in range(1, 10, 1):
    print(i)            #1 2 3 4 5 6 7 8 9

for t in range(1, 10, 3):
    print(t)            #1 4 7

for y in range(5):
    if y < 5:
        print(y)        # 0 1 2 3 4
    elif y == 3:
        print("y is 3")

for j in range(20, 1, -3):
    print(j)                # 20 17 14 11 8 5 2

cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)             #London Paris Tokyo

numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):    
    print(x)                        # 0 7 1 13 2 8 3 42 The answer to life, the universe, and everything.
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")

for num in range(10):
    if num % 2 == 0:
        print("Hello")      # Hello 1 Hello 3 Hello 5 Hello 7 Hello 9
    elif num % 4 == 0:
        print("World")
    else:
        print(num)

pet_info = {
    "name": "Fido", 
    "age": 4, 
    "trick": "rolls over"
}
for key in pet_info:
    print(key)              #name Fido age 4 trick rolls over
    print(pet_info[key])    

things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():        #First, I will use the 20 minute rule and use the platform and other resources to find my answer 
    print(num + ", I will " + step)                     #Second, I will ask my classmates for help, like how I would ask a fellow employee at my job 
                                                            #Third, I will ask an available TA in a public setting, so everyone can benefit from my question
                                                                # Fourth, I will ask an available instructor