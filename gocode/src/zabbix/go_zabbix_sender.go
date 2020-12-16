package main

import (
    "encoding/binary"
    "encoding/json"
    "flag"
    "fmt"
    "io/ioutil"
    "net"
    "os"
    "unsafe"
)

const (
    ConstHeader       = "ZBXD"
    ConstHeaderLength = len(ConstHeader)
    Version           = 1
)

//封包
func Packet(message []byte) []byte {
    return append(append(append([]byte(ConstHeader),
        IntToBytes(Version, 4)...),
        IntToBytes(len(message), 8)...), message...)

}

//整形转换成字节
func IntToBytes(n, x int) []byte {

    // 小端处理
    b := make([]byte, x)
    i := uint32(n)
    binary.LittleEndian.PutUint32(b, i)
    if x == 4 {
        var bx []byte
        bx = append(bx, b[0])
        return bx
    }
    return b
}

// 是否小端
func IsLittleEndian() bool {
    var i int32 = 0x01020304
    u := unsafe.Pointer(&i)
    pb := (*byte)(u)
    b := *pb
    return (b == 0x04)
}

// 请求协议
type ReqPt struct {
    Data    []map[string]string `json:"data"`
    Request string              `json:"request"`
}

func sender(conn net.Conn, endpoint, key, value string) {
    var data map[string]string
    data = make(map[string]string)
    data["host"] = endpoint
    data["value"] = value
    data["key"] = key
    var datas []map[string]string
    datas = append(datas, data)
    reqData := ReqPt{
        Data:    datas,
        Request: "sender data",
    }
    reqDataSlice, _ := json.Marshal(reqData)
    _, err := conn.Write(Packet(reqDataSlice))
    if err != nil {
        fmt.Println("bad packet ", err)
    }

    bys, err := ioutil.ReadAll(conn)
    if err != nil {
        fmt.Println("bad request ", err)
    }
    var reciveText = string(bys)

    fmt.Println("result:", reciveText)
    fmt.Println("send over")
}

func main() {
    if !IsLittleEndian() {
        fmt.Println("System Incompatibility")
        os.Exit(1)
    }

    server := flag.String("server", "127.0.0.1:10051", "zabbix server")
    endpoint := flag.String("endpoint", "localhost", "report host name or ip")
    key := flag.String("key", "cloud.test", "metric name")
    value := flag.String("value", "0", "metric value")
    help := flag.Bool("help", false, "help")
    flag.Parse()

    if *help {
        usage()
        os.Exit(1)
    }
    if len(os.Args) != 5 {
        usage()
        os.Exit(1)
    }

    tcpAddr, err := net.ResolveTCPAddr("tcp4", *server)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s\n", err.Error())
        os.Exit(1)
    }

    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
        os.Exit(1)
    }

    defer conn.Close()
    fmt.Println("connect zabbix server success")
    sender(conn, *endpoint, *key, *value)
}

func usage() {
    fmt.Fprintf(os.Stderr, `gozbx-sender  version: gozbx-sender /1.0.0
Usage: gozbx-sender  [-server=server] [-endpoint=host] [-key=key] [-value=value]
Options:
`)
    flag.PrintDefaults()
}
