package main
import "fmt"

func suma_hilo(x, y, z []int, id_thread int, c chan int) {
	// Suma los elementos de las listas x e y y los guarda en z
	z[id_thread] = x[id_thread] + y[id_thread]
	// Envía el identificador del hilo al canal
	c <- id_thread
}

func main() {
	fmt.Println("Inicio del programa")
	x := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	y := []int{11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
	z := make([]int, len(x))

	c := make(chan int)

	// Lanza un hilo por cada elemento de la lista
	for i := 0; i < len(x); i++ {
		go suma_hilo(x[:], y[:], z[:], i, c)
	}

	// El identificador de cada hilo es el mismo que el índice de la lista
	for i := 0; i < len(x); i++ {
		select {
		case r := <-c:
			fmt.Println("El hilo %d ya terminó", r)
		}
	}

	// Comprobación de que la suma se realizó correctamente
	for i := 0; i < len(x); i++ {
		fmt.Printf("Z[%d] = %d\n", i, z[i])
	}
}