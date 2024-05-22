#lang racket

; Funciones anónimas
; (lambda (<id>*) <expr>+)

(define (terminator s t func)
  (func s t)
)

(define (terminator2 s func)
  (func s)
)

(terminator2 "hola" (lambda (s) (string-append s "!")))

(terminator2 "hola" (lambda (s) (string-append s s)))

((lambda (x) (+ x 1) ) 1)
; vs
(define (mi-add x) (+ x 1) )
(mi-add 1)

; Ejemplo 1
(define (sum-fuc x n func)
  (define (iter n_i res)
    (cond
      [(= n_i 0) res]
      [else (iter (- n_i 1) (+ res (func x) ) ) ]
    )
  )
  (iter n 0)
)
(sum-fuc 2 10 (lambda (x) (sin x)) )


; Let
; Para la regla de Simpson
(let ([x (random 4)]
      [y (random 4)])
(cond
  [(> x y) "x gana"]
  [(< x y) "y gana"]
  [else "empate"]
))

; Let *
; Bindings
(let* ([x (random 4)]
       [y (random 4)]
       [diff (number->string (abs (- x y)) ) ]
)
(cond
  [(> x y) (string-append "Claudia gana por: " diff)]
  [(< x y) (string-append "Chochi gana por: " diff)]
  [else "El monito"]
))