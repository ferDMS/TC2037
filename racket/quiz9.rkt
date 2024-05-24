#lang racket

; Quiz 9
; Fernando Daniel Monroy Sánchez
; A01750536

; Ejercicio 1
(define (func x)
  (cond
    [(>= x 5) (sqrt x)]
    [(>= x -2) (- x 5)]
    [else (* x x x)]
  )
)

; Ejercicio 2
(define (vector-sum lst1 lst2)
  (define (iter lst1 lst2 lst-new)
    (cond
      [(and (empty? lst1) (empty? lst2) ) (reverse lst-new)]
      [(or (empty? lst1) (empty? lst2) ) #f]
      [else (iter (rest lst1) (rest lst2) (cons (+ (first lst1) (first lst2) ) lst-new) ) ]
    )
  )
  (iter lst1 lst2 empty)
)


; Ejercicio 1
(displayln(func 9))
(displayln(func 0))
(displayln(func -9))

; Ejercicio 2
(displayln(vector-sum '(1 2 3) '(4 5 6) ))
(displayln(vector-sum '(0 1 -4) '(1 -5 4) ))