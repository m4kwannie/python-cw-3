# write your code here
favorite_animals = ['dog', 'cat', 'monkey', 'rabbit']

for animals in favorite_animals:
    print(animals)

favorite_animals[1]
print(f"the second animal from the list is the {favorite_animals[1]}")

favorite_animals.remove("monkey")
print(favorite_animals)

favorite_animals.append("parrot")
print(favorite_animals)

for animals in favorite_animals:
    print("i love",animals)

numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for num in numbers:
    numbers_sum = numbers_sum + num
print(numbers_sum)