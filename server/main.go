package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"net"
	"sync"
)

var mutex = &sync.Mutex{}

func main() {
	//modePtr := flag.String("word", "fifo", "mode to run on (fifo, rr, spn, srt)")
	queue := make([]string, 0)
	queue = append(queue, "bees")
	queue = append(queue, "trees")

	portPtr := flag.String("port", "8081", "port number")
	flag.Parse()

	fmt.Println("Launching server...")

	// listen on all interfaces
	ln, err := net.Listen("tcp", ":"+*portPtr)
	if err != nil {
		log.Println("Error listening on port:", err)
	}
	defer ln.Close()

	for {
		// accept connection on port
		conn, err := ln.Accept()
		if err != nil {
			log.Println("Error accepting request:", err)
		}

		go handleRequest(conn, &queue)
	}
}

func handleRequest(conn net.Conn, queue *[]string) {
	// will listen for message to process ending in newline (\n)
	message, _ := bufio.NewReader(conn).ReadString('\n')
	// output message received
	fmt.Println("Message Received:", string(message))
	// sample process for string received
	newmessage := getNext(queue)
	fmt.Println(newmessage)
	// send new string back to client
	conn.Write([]byte(newmessage + "\n"))
}

func getNext(queue *[]string) string {
	mutex.Lock()
	result := (*queue)[0]
	*queue = (*queue)[1:]
	mutex.Unlock()
	return result
}
