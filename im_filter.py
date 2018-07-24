#!/bin/python
from PIL import Image
import sys

def print_index(pixels, size, index):
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			print(pixels[i,j][index], end=' ')
		print('')

def main(f_name):
	# This is the function that will act as a driver
	im = Image.open(f_name)
	pixels = im.load()
	print(im.size[0], im.size[1])
	# print red pixels
	print_index(pixels, im.size, 0)
	# print blue pixels
	print_index(pixels, im.size, 1)
	# print green pixels
	print_index(pixels, im.size, 2)

	im.close()

if __name__ == '__main__':
	# Sanity check for correct script execution
	if len(sys.argv)<2:
		print('Usage: '+str(sys.argv[0])+' <path to image file here>', file=sys.stderr)
		exit(1)

	file_name = sys.argv[1]
	try:
		main(file_name)
	except BrokenPipeError as e:
		print('Hey !\nThe input was not read completely !', file=sys.stderr)

