package main
import (
    "fmt"

)
type Rectangle struct {
    length int
    width int
}
func Area(p *Rectangle) int{
    return p.length*p.width
}

func main() {
    t :=&Rectangle{1,3}
    s:=Area(t)
    fmt.Println(s)

}
