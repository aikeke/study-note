package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	file, err := os.Open("/root/zabbix_api.py")
	if err != nil {
		fmt.Printf("%v\n", err)
	}
	fmt.Println(file)
	defer file.Close()
	reader := bufio.NewReader(file)
	for {
		line,err := reader.ReadString('\n')
		if err == io.EOF {
			break
		}

    	fmt.Print(line)
	}
}
