from math import floor

num_of_tiles=int(input('Enter number of tiles: '))

max_side=floor(num_of_tiles**(1/2))

print('The largest square has side length {}.'.format(max_side))
