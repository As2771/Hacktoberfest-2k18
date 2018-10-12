# Simple coin toss counter
import random

heads = 0
tails = 0

for i in range(0, 100):
	flip = random.randint(0,1)
	#print(flip)

	if flip == 0:
		heads += 1 # heads count
	else:
		tails += 1

print('Heads count is %i.' % heads)
print('Tails count is %i.' % tails)