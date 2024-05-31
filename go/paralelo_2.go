import "fmt"

func busqueda_hilo(x []int, low, high, value int, id_thread int, c chan int) {
	for i := low; i < high; i++ {
		if x[i] == value {
			c <- id_thread
		}
	}
	c <- -1
}

func main() {
	fmt.Println("Inicio del programa")
	x := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	y := []int{11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
	fmt.Println("Dame el número que deseas buscar")

	var value int
	var num_hilos int
	var size int

	n := len(x)
	fmt.Println("Dame el número de hilos")
	fmt.Scan(&num_hilos)
	size = n / num_hilos
	c := make(chan int) // Add channel declaration and initialization
	for i := 0; i < len(x); i++ {
		go busqueda_hilo(x, i*size, (i+1)*size, value, i, c) // Move channel outside of the goroutine
	}

	for i := 0; i < num_hilos; i++ {
		select {
		case r := <-c:
			if r != -1 {
				fmt.Printf("El hilo %d encontró el valor\n", r)
			}
		}
	}
