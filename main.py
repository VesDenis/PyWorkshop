with open('sums.txt', 'r') as file:
  for nums in file:
    a, b = map(int, nums.split())
    print(a + b)