# Funcion para obtener conjunto potencia
def getSubsets(arr, right_idx):
    # Caso base: conjunto de conjunto vacio
    if right_idx < 0: return [[]]
    # Obtener conjunto potencia de conjunto {x en Z | x < right_idx}
    subsets = getSubsets(arr, right_idx-1)
    # Por cada subconjunto, agregar el elemento en arr[right_idx]
    # Duplica el tamano de subsets de 2^{right_idx+1} a 2^{right_idx+2}
    subsets_w_idx = [subset+[arr[right_idx]] for subset in subsets]
    subsets = subsets + subsets_w_idx
    return subsets

# Definir A
A = list(range(1,8))
print(f"\nA = {A}\n")

# Subconjuntos de A
A_subsets = getSubsets(A, len(A)-1)
print(f"a) {len(A_subsets)}:\n{A_subsets}\n")

# Subconjuntos no vacios de A
# No incluir {}
A_b = [subset for subset in A_subsets if subset != []]
print(f"b) {len(A_b)}:\n{A_b}\n")

# Subconjuntos de A que contienen tres elementos
A_c = [subset for subset in A_subsets if len(subset) == 3]
print(f"c) {len(A_c)}:\n{A_c}\n")

# Subconjuntos propios no vacios de A
# No incluir {} o el propio subconjunto
A_d = [subset for subset in A_b if subset != A]
print(f"d) {len(A_d)}:\n{A_d}\n")

print(f"e) {len(A_c)}:\n{A_c}\n")

# Subconjuntos de A que contienen los elementos 1 y 2
A_f = [subset for subset in A_subsets if 1 in subset or 2 in subset]
print(f"f) {len(A_f)}:\n{A_f}\n")

# Subconjuntos de A que contienen cinco elementos, incluyendo a los elementos 1 y 2
A_g = [subset for subset in A_f if len(subset)==5]
print(f"g) {len(A_g)}:\n{A_g}\n")

# Subconjuntos propios de A que contienen los elementos 1 y 2
A_h = [subset for subset in A_f if subset != A]
print(f"h) {len(A_h)}:\n{A_h}\n") # 64 (del 1) + 32 (del 2) - 1 (del no propio)

# Subconjuntos de A con un numero par de elementos
A_i = [subset for subset in A_subsets if len(subset) % 2 == 0]
print(f"i) {len(A_i)}:\n{A_i}\n")

# Subconjuntos de A con un numero impar de elementos
A_j = [subset for subset in A_subsets if not subset in A_i]
print(f"j) {len(A_j)}:\n{A_j}\n")

# Subconjuntos de A con un numero impar de elementos y que incluyen el numero 3
A_k = [subset for subset in A_j if 3 in subset]
print(f"k) {len(A_k)}:\n{A_k}\n")