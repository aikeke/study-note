package main
import (
    "fmt"
    "flag"
)
func main(){
    name:=flag.String("name","ayf","姓名")
    age:=flag.Int("age",18,"年龄")
    flag.Parse()
    fmt.Println(flag.Args())
    fmt.Println(flag.NArg())
    fmt.Println(flag.NFlag())
    fmt.Println(*name,*age)


}
