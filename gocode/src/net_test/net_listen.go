package main

import (
	"net"
)

func main() {
	tcpaddr, _ := net.ResolveTCPAddr("tcp", "192.168.21.23:12345")
	tcplisten, _ := net.ListenTCP("tcp", tcpaddr)
	for {
		conn, err := tcplisten.Accept()
		if err != nil {
			continue
		}
		conn.Write([]byte("hello world \r\n"))
		conn.Close()
	}

}
