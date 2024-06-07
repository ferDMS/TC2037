// Actividad 5.2: Programación paralela y concurrente
// Fernando Daniel Monroy Sánchez
// A01750536

package main
import "fmt"
import "math/rand"
import "time"
import "sync"


// Función para transponer matriz
// La función no se usó al final
/*
func transpose(mtrx [][]int) [][]int {
	t := make([][]int, len(mtrx[0]))
	for i := range t {
		t[i] = make([]int, len(mtrx))
		for j := range mtrx {
			t[i][j] = mtrx[j][i]
		}
	}
	return t
}
*/


// Función para multiplicación matricial concurrente
// En vez de usar un canal para esperar todos los resultados se usa un waitgroup que al final de la función espera a que todos los hilos hayan acabado su ejecución
func mult_matrix_conc(A [][]int, B [][]int, C [][]int) {
    var wg sync.WaitGroup

    for i := 0; i < len(A); i++ {
        for j := 0; j < len(B[0]); j++ {
            wg.Add(1)
            go func(i, j int) {
                defer wg.Done()
                for k := 0; k < len(A[0]); k++ {
                    C[i][j] += A[i][k] * B[k][j]
                }
            }(i, j)
        }
    }

    wg.Wait()
}


// Función para multiplicación matricial secuencial
func mult_matrix_sec(A [][]int, B [][]int, C [][]int) {

	// Calcular producto punto de cada fila de A con cada columna de B
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B[0]); j++ {
			for k := 0; k < len(A[0]); k++ {
				C[i][j] += A[i][k] * B[k][j]
			}
		}
	}
}


// Función para imprimir una matriz
func print_mtrx(mtrx [][]int) {
	for i := 0; i < len(mtrx); i++ {
		for j := 0; j < len(mtrx[i]); j++ {
			fmt.Printf("%3d ", mtrx[i][j])
		}
		fmt.Println()
	}
}


func main() {

	// Generar nueva semilla random para cómputos aleatorios
	rand.Seed(time.Now().UnixNano())

	// Definir dimensiones de matrices
	p := rand.Intn(1000) + 1
	q := rand.Intn(1000) + 1
	r := rand.Intn(1000) + 1

	// Imprimir dimensiones
	fmt.Printf("\nDimensiones: p=%d,  q=%d, r=%d\n\n", p, q, r)

	// Definir matrices con números aleatorios según dimensiones
	
	// Matriz A de p x q
	A := make([][]int, p)
	for i := 0; i < p; i++ {
		A[i] = make([]int, q)
		for j := 0; j < q; j++ {
			A[i][j] = rand.Intn(10)
		}
	}

	// Matriz B de q x r
	B := make([][]int, q)
	for i := 0; i < q; i++ {
		B[i] = make([]int, r)
		for j := 0; j < r; j++ {
			B[i][j] = rand.Intn(10)
		}
	}

	// Imprimir ambas matrices
	fmt.Printf("\nMatriz A (%d x %d)\n", p, q)
	// print_mtrx(A)

	fmt.Printf("\nMatriz B (%d x %d)\n", q, r)
	// print_mtrx(B)

	// Crear la matriz C de p x r con 0s
	C1 := make([][]int, p)
	for i := 0; i < p; i++ {
		C1[i] = make([]int, r)
	}

	C2 := make([][]int, p)
	for i := 0; i < p; i++ {
		C2[i] = make([]int, r)
	}

	fmt.Printf("\nMatriz C inicial (%d x %d)\n", p, r)
	// print_mtrx(C1)

	// Ejecutar multiplicación matricial concurrente y medir tiempo
	start := time.Now()
	mult_matrix_conc(A, B, C1)
	elapsed_conc := time.Since(start)
	fmt.Printf("\nTiempo de ejecución concurrente: %s\n", elapsed_conc)

	// Ejecutar multiplicación matricial secuencial y medir tiempo
	start = time.Now()
	mult_matrix_sec(A, B, C2)
	elapsed_sec := time.Since(start)
	fmt.Printf("Tiempo de ejecución secuencial: %s\n\n", elapsed_sec)

	// Imprimir diferencia porcentual entre ambos
	fmt.Printf("Diferencia porcentual: %.2f%%\n\n", 100*(float64(elapsed_sec-elapsed_conc)/float64(elapsed_sec)))

	// Imprimir matriz C final
	fmt.Printf("\nMatriz C final (%d x %d)\n", p, r)
	// print_mtrx(C2)
	fmt.Println()

	/*
	Conclusión:

	El manejo de computación concurrente de multiplicación de matrices puede ser beneficiosa cuando se tiene una gran cantidad de cómputos. Debido al overhead del manejo de hilos de golang, al tener matrices muy pequeñas esta ventaja puede no apreciarse.

	Por ello, para simular de mejor manera las ventajas de la concurrencia, se puede aumentar el tamaño de las matrices en la línea 80, 81 y 82 para tener mayores dimensiones y probar cómo estas tienen un efecto directo sobre el tiempo de ejecución.

	*/

}