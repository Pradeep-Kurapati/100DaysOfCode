package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

// Create new type 'deck'
// which is a Slice of strings

type deck []string

func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

func newDeck() deck {
	cards := deck{}
	cardSuits := []string{"Spades", "Clubs", "Diamonds", "Hearts"}
	cardValue := []string{"One", "Two", "Three", "Four"}

	for _, suit := range cardSuits {
		for _, value := range cardValue {
			cards = append(cards, value+" of "+suit)
		}
	}
	return cards
}

func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

// To convert out Slice of string (deck) into a string
func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}

// To save to file
func (d deck) saveToFile(filename string) error {
	return os.WriteFile(filename, []byte(d.toString()), 0666)
}

// To turn byte slice back into deck.
// We read byte slice from the local file.
func newDeckFromFile(filename string) deck {
	bs, err := os.ReadFile(filename)

	if err != nil {
		// Show user the error and quit the program
		fmt.Println("Error: ", err)
		os.Exit(1)
	}

	// Reading is successful
	s := strings.Split(string(bs), ",")
	return deck(s)

}

// To shuffle the order of byte slice "deck"
func (d deck) shuffle() {

	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)

	for i := range d {
		newPosition := r.Intn(len(d) - 1)

		// Swapping
		d[i], d[newPosition] = d[newPosition], d[i]
	}
}