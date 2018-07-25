package main

import (
	"fmt"
	"image"
	_ "image/gif"
	_ "image/jpeg"
	_ "image/png"
	"os"
)

func main() {

	// Reading arguments from commandline
	arg := os.Args[1:]

	if len(arg) <= 0 {
		fmt.Print("Enter a filename too ")
		fmt.Println(os.Args)
	}

	// opening file
	file, err := os.Open(arg[0])
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	// decoding the file as an image
	img, _, err := image.Decode(file)
	if err != nil {
		fmt.Printf("%s: %v\n", arg[0], err)
	}

	// getting height and width of the image
	bounds := img.Bounds()
	width, height := bounds.Max.X, bounds.Max.Y

	// I never knew 2D slices could be such a pain in ass
	red, green, blue := make([][]int, height), make([][]int, height), make([][]int, height)
	for i := range red {
		red[i], green[i], blue[i] = make([]int, width), make([]int, width), make([]int, width)
	}

	// storing image in red, green and blue matrix
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			r, g, b, _ := img.At(x, y).RGBA()
			// RGBA sucks. Max val is 65535 :/
			red[y][x], green[y][x], blue[y][x] = sm(r), sm(g), sm(b)

		}

	}

	// printing
	fmt.Printf("%d %d\n", height, width)
	printMat(red)
	printMat(blue)
	printMat(green)
}

func sm(x uint32) int {
	return int((float32(x) / 65535.0) * 255)
}

func printMat(mat [][]int) {
	for _, arr := range mat {
		for _, val := range arr {
			fmt.Printf("%d ", int(val))
		}
		fmt.Println()
	}
}
