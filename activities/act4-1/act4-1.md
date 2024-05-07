# Actividad 3.3 Practicando las máquinas de Turing

## Fernando Daniel Monroy Sánchez

## A01750536

---

![](assets/Pasted%20image%2020240505131516.png)

![](assets/Pasted%20image%2020240505131536.png)

Donde $h$ equivale al símbolo $\#$.

Para realizar pruebas de esta máquina de Turing se puede evaluar en:

https://turingmachine.io/

Con el siguiente código:

```
input: 'hh01h0101h0100'
blank: ' '
start state: q1
table:
  q1:
    h: {write: H, R: q2}
  q2:
    0: R
    1: R
    h: {write: E, R: q3}
  q3:
    X: R
    Y: R
    0: {write: X, L: q20}
    1: {write: Y, L: q21}
    h: {L: q22}
  q4:
    0: L
    1: L
    h: L
    ' ': {R: q6}
    H: {R: q6}
    X: {R: q6}
    Y: {R: q6}
  q5:
    0: L
    1: L
    h: L
    ' ': {R: q7}
    H: {R: q7}
    X: {R: q7}
    Y: {R: q7}
  q6:
    0: {write: X, R: q9}
    1: {L: q8}
    h: {L: q8}
    E: {write: h, R: q15}
  q7:
    1: {write: Y, R: q9}
    0: {L: q8}
    h: {L: q8}
    E: {write: h, R: q15}
  q8:
    X: {write: 0, L}
    Y: {write: 1, L}
    H: {R: q10}
    E: L
  q9:
    0: {R: q14}
    1: {R: q14}
    h: {R: q14}
    E: {R: q18}
  q10:
    0: R
    1: R
    h: {write: H, R: q11}
    E: {write: h, R: q15}
  q11:
    0: R
    1: R
    h: R
    E: {R: q12}
  q12:
    X: {write: 0, R}
    Y: {write: 1, R}
    0: {L: q13}
    1: {L: q13}
    h: {L: q13}
    ' ': {L: q13}
  q13:
    0: L
    1: L
    E: {R: q3}
  q14:
    0: R
    1: R
    h: R
    E: {R: q3}
  q15:
    X: {write: 0, R}
    Y: {write: 1, R}
    0: R
    1: R
    ' ': {L: qaccept}
    h: {write: E, L: q16}
  q16:
    0: L
    1: L
    H: {write: h, L}
    h: L
    ' ': {R: q19}
  q17:
    0: R
    1: R
    h: R
    E: {R: q3}
  q18:
    X: R
    Y: R
    h: {L: qrej}
    ' ': {L: qrej}
    0: {L: q8}
    1: {L: q8}
  q19:
    h: {write: H, R: q17}
  q20:
    X: L
    Y: L
    E: {L: q4}
  q21:
    X: L
    Y: L
    E: {L: q5}
  q22:
    E: {L: q23}
    H: {R: q24}
  q23:
    0: L
    1: L
    h: {L: q25}
    H: {L: qrej}
  q24:
    h: {write: H, R: q11}
  q25:
    0: {L: q23}
    1: {L: q23}
    h: {R: qrej}
    H: {L: qrej}
  qaccept:
  qrej:
```

![](assets/Pasted%20image%2020240505132805.png)

![](assets/Pasted%20image%2020240505140627.png)

https://turingmachine.io/

```
input: 'aaabbbccc'
blank: ' '
start state: q1
table:
  q1:
    a: {write: X, R: q2}
    Y: {R: q5}
  q2:
    a: R
    Y: R
    b: {write: Y, R: q3}
  q3:
    b: R
    Z: R
    c: {write: Z, L: q4}
  q4:
    c: L
    Z: L
    b: L
    Y: L
    a: L
    X: {R: q1}
  q5:
    Y: R
    Z: {R: q6}
  q6:
    Z: R
    ' ': {L: qaccept}
  qaccept:
```

![](assets/Pasted%20image%2020240505141032.png)

![](assets/Pasted%20image%2020240505170002.png)

https://turingmachine.io/

```
input: '001100'
blank: ' '
start state: qaccept
table:
  qaccept:
    0: {write: X, R: q2}
    1: {write: X, R: q3}
  q1:
    0: {write: X, R: q2}
    1: {write: X, R: q3}
    Y: {R: q7}
  q2:
    0: R
    1: R
    Y: {L: q4}
    ' ': {L: q4}
  q3:
    0: R
    1: R
    Y: {L: q5}
    ' ': {L: q5}
  q4:
    0: {write: Y, L: q6}
    1: {L: qrej}
    X: {R: qrej}
  q5:
    1: {write: Y, L: q6}
    0: {L: qrej}
    X: {R: qrej}
  q6:
    0: L
    1: L
    X: {R: q1}
  q7:
    Y: R
    ' ': {L: qaccept}
  qrej:
```