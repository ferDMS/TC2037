
# Actividad Extra
#### Fernando Daniel Monroy Sánchez
#### A01750536

#### Eugenio Mejía

#### A01412143

---

$L_4=\{a^ib^jc^{ij}|ij\geq1\}$
![](assets/Pasted%20image%2020240428210809.png)

Profe, puede hacer la simulación de este ejercicio con el siguiente código en la siguiente liga: https://turingmachine.io/

```
input: 'aabbcccc'
blank: ' '
start state: q0
table:
  q0:
    a: R
    b: {L: q1}
    c: {L: rej}
    ' ': {L: rej}
  q1:
    a: {write: X, R: q2}
    ' ': {L: rej}
  q2:
    X: R
    b: R
    c: {L: q3}
  q3:
    b: {write: Y, R: q4}
  q4:
    Y: R
    c: R
    ' ': {L: q5}
    Z: {L: q5}
  q5:
    c: {write: Z, L: q6}
    Y: {L: rej}
  q6:
    Y: L
    c: L
    b: {write: Y, R: q4}
    X: {R: q7}
  q7:
    Y: {write: b, R}
    c: {L: q8}
    Z: {L: q9}
  q8:
    b: L
    X: L
    a: {write: X, R: q2}
  q9:
    b: L
    X: L
    ' ': {R: done}
    a: {R: rej}
  rej:
  done:
```

Diseñar una máquina de Turing que realice la suma de dos números binarios sin acarreos.

![](assets/Pasted%20image%2020240428210736.png)