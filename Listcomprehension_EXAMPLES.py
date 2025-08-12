string = "Hello, world!"
characters = [x for x in string]

print(characters)

squares = [x ** 2 for x in range(1, 6)]
print(squares)


even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)


sentence = "O rato roeu a roupa do rei de Roma"
words = [word for word in sentence.split()]
print(words)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_numbers = list(set([x for x in numbers]))
print(unique_numbers)

primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, int(x**0.5)+1))]
print(primes)
