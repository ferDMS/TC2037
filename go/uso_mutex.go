package main

import (
	"fmt"
	"sync"
)

var mutex sync.Mutex

var recurso = [...]int{100, 200, 300, 400, 500, 600, 700, 800}

func leer_recurso(i int, c chan bool) {
	mutex.Lock()
	fmt.Println("El hilo ", i, " está en su región crítica")
	for j := 0; j < len(recurso); j++ {
		fmt.Printf("\t recurso[%d] = %d\n", j, recurso[j])
	}
	if i < len(recurso) {
		recurso[i] = i
	}
	fmt.Println("El hilo ", i, " sale de su región crítica y deja un regalito")
	mutex.Unlock()
	c <- true
}

func main() {
	c := make(chan bool)
	for i := 0; i < 10; i++ {
		go leer_recurso(i, c)
	}

	for i := 0; i < 10; i++ {
		r := <-c
		if r {
			fmt.Println("¡Un hilo ha acabado!")
		}
	}
}
