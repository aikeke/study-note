package main
import "fmt"
func main(){
    ch1 := make(chan int)
    go senddata(ch1)
    fmt.Println(<-ch1)
}
func senddata(ch chan int){
    for i:=0;;i++ {
        ch <- i
}

}
