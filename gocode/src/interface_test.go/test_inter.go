package main

import "fmt"

type Simpler interface {
	Get() int
}
type simple struct {
	x int
}

func (c *simple) Get() int {
	return c.x
}

func main() {
	t :=new(simple)
    t.x=10
	var o Simpler
    o=t
	a := o.Get()
	fmt.Println(a)
}
