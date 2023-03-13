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

	jimmy := person{
		firstName: "Jimmy",
		lastName: "Kimmel",
		contact: contactInfo{
			email: "kimmyk@gmail.com",
			zipCode: 500018,
		},
	}

	fmt.Printf("%+v", jimmy)
}
