package main

import "fmt"

func main() {
	c := make(chan int)
	q := 10
	go generateInts(c, q)

	for k := range c {
		fmt.Println(k)
	}

}

func generateInts(c chan int, q int) {
	for i := 0; i < q; i++ {
		c <- i
	}
	close(c)
}