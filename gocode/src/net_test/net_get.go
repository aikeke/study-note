package main

import (
	"fmt"
	"io/ioutil"
	"net"
)

func main() {
	tcpaddr, _ := net.ResolveTCPAddr("tcp", "www.baidu.com:80")
	tcpconn, _ := net.DialTCP("tcp", nil, tcpaddr)
	tcpconn.Write([]byte("GET / HTTP/1.1 \r\n\r\n"))
	data, _ := ioutil.ReadAll(tcpconn)
	fmt.Println(data)
    fmt.Println(string(data))

}
