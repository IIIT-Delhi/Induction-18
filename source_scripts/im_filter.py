#!/bin/python
from PIL import Image

import argparse
import io
import subprocess
import sys

red = []
blue = []
green = []

def print_index(pixels, size, index):
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			print(pixels[i,j][index], end=' ')
		print('')

def print_image(f_name):
	# This is the function that will act as a driver for input generation
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

def reconstruct_image(f_name, size):
	# This is the function that will act as a driver for reconstruction
	im = Image.new('RGB',size)
	pix = im.load()
	for i in range(0, size[0]-1):
		for j in range(0, size[1]-1):
			pix[i,j] = (red[i][j], blue[i][j], green[i][j])
	im.show()
	im.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-l","--level",
						help="""The level of filter that should be tested !
								Level 1 - Red filter\n
								Level 2 - Invert filter\n
								Level 3 - Grayscale filter\n
								Level 4 - Increase brightness\n
								Level 5 - Blurr filter\n
								----- Extra tasks -----\n
								Level 6 - Create a black frame on the image\n
								Level 7 - Draw a red cross on the image\n
						 	 """,
						type=int,
						choices=[1,2,3,4,5],
						default=1
						)
	parser.add_argument("-o","--output", help="output file name")
	parser.add_argument("command", help="command to run your program and get the desired output")
	parser.add_argument("path", help="path to image for which the filter is being built.")
	args = parser.parse_args()

	real_stdout = sys.stdout
	fake_stdout = io.StringIO()
	output_str = ''
	try:
		sys.stdout = fake_stdout
		print_image(args.path)
	except BrokenPipeError as e:
		print('Hey !\nThe input was not read completely !', file=sys.stderr)
	finally:
		sys.stdout = real_stdout
		output_str = fake_stdout.getvalue()
		fake_stdout.close()

	output = ''
	try:
		output = subprocess.check_output(args.command, shell=True, input=output_str, universal_newlines=True )
	except Exception as e:
		print("Could not run the command "+args.command)
	finally:
		output_str = output

	fake_stdin = io.StringIO(output_str)
	real_stdin = sys.stdin
	try:
		if args.output:
			file_name = args.output
		else:
			file_name = 'output.bmp'
		sys.stdin = fake_stdin
		x,y = map(int, input().split(' '))
		for i in range(0, x):
			red.append(list(map(int, input().split(' ')[:-1])))
		for i in range(0, x):
			blue.append(list(map(int, input().split(' ')[:-1])))
		for i in range(0, x):
			green.append(list(map(int, input().split(' ')[:-1])))

		reconstruct_image(file_name, (x,y))
	except Exception as e:
		print('Hey !\nThere were some errors in the input data !', file=sys.stderr)
	finally:
		sys.stdin = real_stdin
		fake_stdin.close()

