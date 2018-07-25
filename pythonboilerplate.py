import sys

red = []
blue = []
green = []

def print_pixel(arr, size):
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			print(arr[i][j], end=' ')
		print('')

def main(size):
	global red, blue, green
	# Write your logic below :
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			# red[i][j] = (255-red[i][j])
			# blue[i][j] = (255-blue[i][j])
			# green[i][j] = (255 - green[i][j])

			red[i][j] = min(255, red[i][j]+50)
			blue[i][j] = min(255, blue[i][j]+50)
			green[i][j] = min(255, green[i][j]+50)

if __name__ == '__main__':
	try:
		x,y = list(map(int, input().strip().split(' ')))
		for i in range(0, x):
			red.append(list(map(int, input().strip().split(' '))))
		for i in range(0, x):
			blue.append(list(map(int, input().strip().split(' '))))
		for i in range(0, x):
			green.append(list(map(int, input().strip().split(' '))))

		main((x,y))

		print(x,y)
		print_pixel(red, (x,y))
		print_pixel(green, (x,y))
		print_pixel(blue, (x,y))

	except Exception as e:
		print(e, file=sys.stderr)
		# raise e
		pass
