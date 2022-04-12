letters = list(input().split())
vowels = ['a', 'o', 'e', 'u', 'y']
print(list(filter(lambda letter: letter in vowels, letters)))