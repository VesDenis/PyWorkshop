planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

with open('solar.txt', 'a') as file:
  for planet in planets:
    file.write(planet)
    file.write('\n')