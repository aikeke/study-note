package main

import "fmt"

func main() {
//	array := [5]int{1, 2, 3, 4, 5}
	slice := []int{100, 200,300}
    newslice :=slice[1:2]
    newslice=append(newslice,10)
	for _, v := range slice {
		fmt.Printf("%d", v)
	}
    fmt.Println(newslice)
    fmt.Println(slice)
}
