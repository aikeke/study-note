package main

import (
	"fmt"
	"os"
)

func main() {
	//var s, sep string
	for a, arg := range os.Args[1:] {
		fmt.Println(a)
		fmt.Println(arg)
	}
}
