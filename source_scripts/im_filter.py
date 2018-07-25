#!/bin/python
from PIL import Image

import argparse
import io
import subprocess
import sys
import textwrap

red = []
blue = []
green = []

def apply_filter(image, level):
	if level<0 or level >8:
		return
	im = Image.open(image)
	im = im.convert('RGB')
	size = im.size
	px = im.load()

	for i in range(0, size[0]):
		for j in range(0, size[1]):
			if level == 0:
				r,g,b = px[i,j]
				px[i,j] = (r,g,b)
			elif level == 1:
				# apply a red filter
				r,g,b = px[i,j]
				px[i,j] = (255,g,b)
			elif level == 2:
				# apply invert
				r,g,b = px[i,j]
				px[i,j] = (255-r, 255-g, 255-b)
			elif level == 3:
				# apply grayscale
				r,g,b = px[i,j]
				px[i,j] = (r,r,r)
			elif level == 4:
				# apply brightness
				r,g,b = px[i,j]
				px[i,j] = (min(255, r+50), min(255, g+50), min(255, b+50))
			elif level == 5:
				# apply dumb blurr
				r_temp = g_temp = b_temp = 0
				if i>=1 and i<size[0]-1 and j>=1 and j<size[1]-1:
					for p in [-1,0,1]:
						for q in [-1,0,1]:
							r_temp += px[i+p, j+q][0]
							g_temp += px[i+p, j+q][1]
							b_temp += px[i+p, j+q][2]
					r_temp = r_temp//9
					g_temp = g_temp//9
					b_temp = b_temp//9
					px[i,j] = (r_temp,g_temp,b_temp)
			elif level == 6:
				# create a black frame:
				if i>=0 and i<=10:
					px[i,j] = (0,0,0)
				if j>=0 and j<=10:
					px[i,j] = (0,0,0)
				if i>=size[0]-10 and i<size[0]:
					px[i,j] = (0,0,0)
				if j>=size[1]-10 and j<size[1]:
					px[i,j] = (0,0,0)
			elif level == 7:
				# create a red cross
				if i==size[0]-i:
					px[i,j] = (255,0,0)
				if j==size[1]-j:
					px[i,j] = (255,0,0)
			elif level == 8:
				# create a purple filter
				r,g,b = px[i,j]
				px[i,j] = (r+50, g, b+50)
	im.show(title='Level '+str(level)+" Expected")

def print_index(pixels, size, index):
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			print(pixels[i,j][index], end=' ')
		print('')

def print_image(f_name):
	# This is the function that will act as a driver for input generation
	im = Image.open(f_name)
	im = im.convert('RGB')
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
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			pix[i,j] = (red[i][j], green[i][j], blue[i][j])
	if f_name:
		im.save(f_name,"JPEG")
	im.show()
	im.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='helper program for image filtering',
									 formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-l","--level",
						help=textwrap.dedent("""Show sample output for a given level !
	Only for testing purpose. It will apply the filter to the given path to show how the result would ideally
	look like and then exit.
	Level 0 - No change
	Level 1 - Red filter
	Level 2 - Invert filter
	Level 3 - Grayscale filter
	Level 4 - Increase brightness
	Level 5 - Blurr filter
	----- Extra tasks -----
	Level 6 - Create a black frame on the image
	Level 7 - Draw a red plus sign on the image
	Level 8 - Purple filter
						 	 """),
						type=int,
						choices=[0,1,2,3,4,5,6,7,8]
						)
	parser.add_argument("-o","--output", help="output file name")
	parser.add_argument("command", help="command to run your program and get the desired output")
	parser.add_argument("path", help="path to image for which the filter is being built.")
	args = parser.parse_args()

	if args.level is not None:
		apply_filter(args.path,args.level)
		sys.exit(0)

	real_stdout = sys.stdout
	fake_stdout = io.StringIO()
	output_str = ''
	try:
		sys.stdout = fake_stdout
		print_image(args.path)
	except BrokenPipeError as e:
		print('Hey !\nThe input was not read completely !', file=sys.stderr)
	except FileNotFoundError as e:
		print('Invalid file ' + args.path)
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
		sys.stdin = fake_stdin
		x,y = map(int, input().strip().split(' '))
		for i in range(0, x):
			red.append(list(map(int, input().strip().split(' '))))
		for i in range(0, x):
			green.append(list(map(int, input().strip().split(' '))))
		for i in range(0, x):
			blue.append(list(map(int, input().strip().split(' '))))

		reconstruct_image(args.output, (x,y))
	except Exception as e:
		print('Hey !\nThere were some errors in the input data !', file=sys.stderr)
	finally:
		sys.stdin = real_stdin
		fake_stdin.close()

