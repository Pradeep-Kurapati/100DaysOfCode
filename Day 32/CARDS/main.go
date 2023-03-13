package main

// import "fmt"

// import "fmt"

// import ("fmt")

func main() {

	// Creating a Slice
	cards := newDeckFromFile("my_cards.txt")
	cards.shuffle()
	cards.print()
}
