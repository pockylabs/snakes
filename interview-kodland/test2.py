def count_vowels_consonants(baris):
    vowels = "aeiouAEIOU"
    count_vowels = sum(1 for char in baris if char.isalpha() and char.lower() in vowels)
    count_consonants = sum(1 for char in baris if char.isalpha() and char.lower() not in vowels)
    return count_vowels, count_consonants

input_lines = int(input("How many lines will there be? "))
puisi = []

for _ in range(input_lines):
    line = input()
    puisi.append(line)

total_vowels = 0
total_consonants = 0


for idx, line in enumerate(puisi, 1):
    count_vowels, count_consonants = count_vowels_consonants(line)
    total_vowels += count_vowels
    total_consonants += count_consonants

print("Number of vowels: ", total_vowels)
print("Number of consonants: ", total_consonants)
