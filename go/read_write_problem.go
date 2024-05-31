package main

import (
	"fmt"
	"sync"
)

var mutex sync.Mutex
var db sync.Mutex
var rc = 0

func leer_base_datos() {
	fmt.Println("Leyendo base de datos...")
}

func usar_datos_leidos() {
	fmt.Println("Usando datos leídos...")
}

func inventar_datos() {
	fmt.Println("Inventando datos...")
}

func escribir_base_datos() {
	fmt.Println("Escribiendo base de datos...")
}

func lector(c chan bool) {
	for i := 0; i < 10; i++ {
		// Protejer la escritura de rc
		mutex.Lock()
		rc++
		if rc == 1 {
			db.Lock()
		}
		mutex.Unlock()

		leer_base_datos()

		// Regresar a la región crítica de rc para actualizarla
		mutex.Lock()
		rc--
		if rc == 0 {
			db.Unlock()
		}
		mutex.Unlock()
		usar_datos_leidos()
	}
	c <- true
}

func escritor(c chan bool) {
	for i := 0; i < 10; i++ {
		inventar_datos()
		
		db.Lock()
		escribir_base_datos()
		db.Unlock()
	}
	c <- true
}

func main() {
	c := make(chan bool)
	go lector(c)
	go escritor(c)
	
	for i := 0; i < 2; i++ {
		r := <-c
		fmt.Println(r)
	}
}