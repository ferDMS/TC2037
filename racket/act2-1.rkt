#lang racket

; Actividad 2.1
; Fernando Daniel Monroy Sánchez
; A01750536

; Ejercicio 1
(define (pow a b)
  (define (iter b_i res)
    (cond
      [(= b_i 0)
        (cond
          [(positive? b) res]
          [else (/ 1 res)]
        )
      ]
      [else (iter (- b_i 1) (* a res) )]
    )
  )
  (iter (abs b) 1)
)

;(displayln "\nEjercicio 1:")
;(displayln (pow 5 0))
;(displayln (pow -5 3))
;(displayln (pow 2 10))


; Ejercicio 2
(define (fib n)
  (define (iter n i-1 i-2)
    (cond
      [(= n 0) (+ i-1 i-2)]
      [else (iter (- n 1) (+ i-1 i-2) i-1)]
    )
  )
  (cond
    [(<= n 1) n]
    [else (iter (- n 2) 1 0)]
  )
)

;(displayln "\nEjercicio 2:")
;(displayln (fib 0))
;(displayln (fib 1))
;(displayln (fib 2))
;(displayln (fib 6))
;(displayln (fib 42))


; Ejercicio 3
(define (positives lst)
  (define (iter lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [(positive? (first lst)) (iter (rest lst) (cons (first lst) lst-new) )]
      [else (iter (rest lst) lst-new )]
    )
  )
  (iter lst empty)
)

;(displayln "\nEjercicio 3:")
;(displayln (positives '()) )
;(displayln (positives '(12 -4 3 -1 -10 -13 6 -5)) )
;(displayln (positives (list -4 -1 -10 -13 -5)) )


; Ejercicio 4
(define (add-list lst)
  (define (iter lst res)
    (cond
      [(empty? lst) res]
      [else (iter (rest lst) (+ res (first lst)) )]
    )
  )
  (iter lst 0)
)

;(displayln "\nEjercicio 4:")
;(displayln (add-list '()) )
;(displayln (add-list '(2 4 1 3)) )
;(displayln (add-list '(1 2 3 4 5 6 7 8 9 10)) )


; Ejercicio 5
(define (list-of-symbols? lst)
  (define (iter lst)
    (cond
      [(empty? lst) #t]
      [(not (symbol? (first lst)) ) #f ]
      [else (iter (rest lst) )]
    )
  )
  (iter lst)
)

;(displayln "\nEjercicio 5:")
;(displayln (list-of-symbols? '() ))
;(displayln (list-of-symbols? '(a b c d e) ))
;(displayln (list-of-symbols? '(a b c d 42 e) ))


; Ejercicio 6
(define (dot-product lst1 lst2)
  (define (iter lst1 lst2 res)
    (cond
      [(empty? lst1) (cond [(empty? lst2) res] [else #f] )]
      [else (iter (rest lst1) (rest lst2) (+ (* (first lst1) (first lst2) ) res) )]
    )
  )
  (iter lst1 lst2 0)
)

;(displayln "\nEjercicio 6:")
;(displayln (dot-product '() '() ))
;(displayln (dot-product '(1 2 3) '(4 5 6) ))
;(displayln (dot-product '(1.3 3.4 5.7 9.5 10.4) '(-4.5 3.0 1.5 0.9 0.0) ))


; Ejercicio 7
(define (average lst)
  (define (sum-all lst sum)
    (cond
      [(empty? lst) sum]
      [else (sum-all (rest lst) (+ (first lst) sum) )]
    )
  )
  (cond
    [(empty? lst) 0]
    [else (/ (sum-all lst 0) (length lst) )]
  )
)

;(displayln "\nEjercicio 7:")
;(displayln (average '() ))
;(displayln (average '(4) ))
;(displayln (average '(5 6 1 6 0 1 2) ))


; Ejercicio 8
(define (expand lst)
  (define (repeat-in-lst elmnt n)
    (define (iter elmnt n lst-new)
      (cond
        [(= n 0) lst-new]
        [else (iter elmnt (- n 1) (cons elmnt lst-new) )]
      )
    )
    (iter elmnt n empty)
  )
  (define (iter lst lst-new n)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter (rest lst) (append (repeat-in-lst (first lst) n) lst-new) (+ n 1) )]
    )
  )
  (iter lst empty 1)
)

;(displayln "\nEjercicio 8:")
;(displayln (expand '() ))
;(displayln (expand '(a) ))
;(displayln (expand '(1 2 3 4) ))
;(displayln (expand '(a b c d e) ))