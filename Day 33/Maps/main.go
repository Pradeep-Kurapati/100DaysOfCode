package main

import "fmt"

func main() {

	// Type 1 : Creating maps
	colors := map[string]string {
	 	"red": "#ff0000",
	 	"green": "#ff4b57",
	 }

	// Type 2: Creating maps
	// var colors map[string]string 

	// Type 3: colors := make(map[string]string)
	
	// Sending Map as an argument
	printMap(colors)
}

// Function to print map

func printMap(c map[string]string) {
	for color, hex := range c {
		fmt.Println("Hex for ",color," is ",hex)
	}
}