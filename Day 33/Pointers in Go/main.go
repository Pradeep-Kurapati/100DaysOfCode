package main

import "fmt"

type contactInfo struct {
	email string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contact contactInfo
}

func main() {

	jim := person{
		firstName: "Jim",
		lastName: "Kimmel",
		contact: contactInfo{
			email: "kimmyk@gmail.com",
			zipCode: 500018,
		},
	}
	
	// Option 1:-
	// jimPointer := &jim
	// jimPointer.updateName("Jimmy")

	// Option 2:-
	// Sending person instead of *person
	jim.updateName("Jimmy")
	jim.print()
}


func (pointerToPerson *person) updateName(newFirstNme string) {
	(*pointerToPerson).firstName = newFirstNme
}


func (p person) print() {
	fmt.Printf("%+v", p)
}
