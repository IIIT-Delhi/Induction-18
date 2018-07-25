#!/bin/python
from PIL import Image
import sys

red = []
blue = []
green = []

def print_index(pixels, size, index):
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			print(pixels[i,j][index], end=' ')
		print('')

def main(f_name, size):
	# This is the function that will act as a driver
	im = Image.new('RGB',size)
	pix = im.load()
	for i in range(0, size[0]-1):
		for j in range(0, size[1]-1):
			pix[i,j] = (red[i][j], blue[i][j], green[i][j])
	im.show()
	im.close()

if __name__ == '__main__':
	# Sanity check for correct script execution
	file_name = 'output.bmp'
	if len(sys.argv)>2:
		file_name = sys.argv[1]

	try:
		x,y = map(int, input().split(' '))
		for i in range(0, x):
			red.append(list(map(int, input().split(' ')[:-1])))
		for i in range(0, x):
			blue.append(list(map(int, input().split(' ')[:-1])))
		for i in range(0, x):
			green.append(list(map(int, input().split(' ')[:-1])))

		main(file_name, (x,y))
	except Exception as e:
		print('Hey !\nThere were some errors in the input data !', file=sys.stderr)

