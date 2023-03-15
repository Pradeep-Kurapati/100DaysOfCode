package main

import (
	"fmt"
	"net/http"
)

func main() {
	links := []string{
		"http://google.com",
		"http://facebook.com",
		"http://stackoverflow.com",
		"http://golang.org",
		"http://amazon.com",
	}

	c := make(chan string)

	for _, link := range links {
		go checkStatus(link, c)
	}

	for i :=0; i < len(links); i++ {
		fmt.Println(<-c)
	}
}

func checkStatus(url string, c chan string) {
	_, err := http.Get(url)
	if err != nil {
		fmt.Println(url, " might be down!")
		return
	}
	c <- url + " is up!"
}