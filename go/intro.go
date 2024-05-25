// Let's gooo

/*
Este
es un 
comentario
largo
*/

/*
float32
float64
int
uint
int8
uint8
int16
int32
uin32
int64
uint64
string
*/

package main
import "fmt"

import (
	"math/rand"
)

// func nombreFuncion (params) (tipoRetorno1, ..., tipoRetornoN)
// func nombreFuncion (params) tipoRetornoUnico

func mi_suma(a, b int) int {
	return a + b
}

func main() {
	fmt.Println("Hola mundo!")
	fmt.Print("Hola")
	fmt.Printf("Cruz Azul %v - %v America", 1, 1)
	fmt.Println()

	const a = 3
	var b = 3
	var (
		c = 4
		d = 5
	)

	var f, g = 7, 8
	e := a + b + c + d + f + g

	fmt.Println(e)

	// 
	var verdad = true
	var falso_como_tu_ex = false

	var la_verdad_de_amlo = verdad && falso_como_tu_ex
	fmt.Println(la_verdad_de_amlo)


	// Condicion
	if la_verdad_de_amlo {
		fmt.Println("La ley de Dios")
	} else if falso_como_tu_ex {
		fmt.Println("Chochitl")
	} else {
		fmt.Println("Movimiento Naranja")
	}

	// Switch
	var opcode = 5
	switch opcode {
	case 1:
		fmt.Println("codigo 1")
	case 2:
		fmt.Println("codigo 2")
	default:
		fmt.Println("defecto")
	}

	b++

	fmt.Println("Dame el codigon")

	// Para input
	fmt.Scan(&opcode)

	switch {
	case opcode == 4:
		fmt.Println("codigo wow")
	case opcode == 5:
		fmt.Println("codigo wowow")
	}

	// For
	// No hay while, se simula con el for
	for b < 10 {
		b++
	}
	for {
		if b == 20 {
			break
		}
		b++
	}
	for cont := 0; cont < 10; cont++ {
		fmt.Println("Derivadass hola aloh")
	}

	if num := rand.Intn(10); num == 5 {
		fmt.Println("Medio un 5")
	} else {
		fmt.Printf("No me dio un 5 me dio %v", num)
		fmt.Println()
	}

	// Llamar a la función
	var sumando1 int
	var sumando2 int
	fmt.Scan(&sumando1)
	fmt.Scan(&sumando2)
	esoo := mi_suma(sumando1, sumando2)
	fmt.Println(esoo)

	// Arrays
	var planetas [4]string
	planetas[0] = "mercurio"
	planetas[1] = "venus"
	planetas[2] = "tierra"
	planetas[3] = "marte"

	for i := 0; i < len(planetas); i++ {
		fmt.Println(planetas[i])
	}

	edades2 := [...]int{1,2,3,4,5,6,7,8}
	for i, val := range edades2 {
		fmt.Printf("edades[%d] = %d", i, val)
	}

}