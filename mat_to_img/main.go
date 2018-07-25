package main

import (
	"fmt"
	"image"
	"image/color"
	"image/png"
	"os"
)

func main() {

	// reads height and width
	var height, width int
	fmt.Scan(&height)
	fmt.Scan(&width)

	// reads the channel in order of red, green, blue
	red := read(height, width)
	green := read(height, width)
	blue := read(height, width)

	// Create a blank image height*width pixels
	newImage := image.NewRGBA(image.Rect(0, 0, width, height))

	// opens a file for writing to
	outputFile, err := os.Create("new_image.png")
	if err != nil {
		fmt.Print(err)
	}
	defer outputFile.Close()

	// sets pixels of the blank image
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			newImage.SetRGBA(x, y, color.RGBA{red[y][x], green[y][x], blue[y][x], 255})
		}
	}

	// Finally write the encoded image to the file
	png.Encode(outputFile, newImage)

}

// reads a particular channel of an image
func read(height int, width int) (c [][]uint8) {

	// makes the 2D slice for the channel
	c = make([][]uint8, height)
	for i := range c {
		c[i] = make([]uint8, width)
	}

	// reads from console
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			fmt.Scan(&c[y][x])
		}
	}

	return
}
