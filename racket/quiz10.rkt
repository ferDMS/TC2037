#lang racket

; Quiz 10
; Fernando Daniel Monroy Sánchez
; A01750536

; Definición de función de preprocesamiento
(define (pre-processing x f)
  (define (iter lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter (rest lst) (cons (f (first lst) ) lst-new) ) ]
    )
  )
  (iter x empty)
)


; Ejercicio a)
(displayln
  (pre-processing '(0.3 1.85 1.87 1.53 1.65 2)
    (lambda (x)
      (cond
        [(>= x 1.87) #t]
        [else #f]))))

(displayln
  (pre-processing '(0.3 1.2)
    (lambda (x)
      (cond
        [(>= x 1.87) #t]
        [else #f]))))


; Ejercicio b)
(displayln
  (pre-processing '(-3 -4 0 3 4)
    (lambda (x) (* x x))))

(displayln
  (pre-processing '(0 1 2 3)
    (lambda (x) (* x x))))


; Ejercicio c)
(displayln
  (pre-processing '("Alejandro" "Natalia" "Goku" "Kakaroto" "Goku" "Diana" "Zelda")
    (lambda (x)
      (cond
        [(or (string=? "Zelda" x) (string=? "Goku" x) ) x]
        [else "NA"]))))