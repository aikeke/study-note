package main
import (
    "fmt"
    "bufio"
    "os"
    "strings"
)
func main() {
    inputReader := bufio.NewReader(os.Stdin)
    fmt.Println("please input some:")
    num :=0
    words :=0
    rows :=0
    for {
        input,_ :=inputReader.ReadString('\n')
        input=strings.TrimRight(input,"\n")
        switch input {
        case "S": 
            fmt.Printf("字符数%d,单词数%d,行数%d\n",num,words,rows)
            break
        default: 
            num=num+len(input)    
            rows=rows+1
            words=words+len(strings.Fields(input))
}
}
}
