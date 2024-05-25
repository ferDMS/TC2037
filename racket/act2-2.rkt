#lang racket

; Actividad 2.2
; Fernando Daniel Monroy Sánchez
; A01750536

; Ejercicio 1
(define (insert n lst)
  (define (iter lst lst-new)
    (cond
      [(empty? lst) (reverse (cons n lst-new))]
      [(<= n (first lst)) (append (reverse (cons n lst-new) ) lst) ]
      [else (iter (rest lst) (cons (first lst) lst-new) ) ]
    )
  )
  (if (empty? lst) (list n) (iter lst empty) )
)

;(displayln(insert 14 '()))
;(displayln(insert 4 '(5 6 7 8) ))
;(displayln(insert 5 '(1 3 6 7 9 16) ))


; Ejercicio 2
(define (insertion-sort lst)
  (define (iter lst lst-new)
    (cond
      [(empty? lst) lst-new]
      [else (iter (rest lst) (insert (first lst) lst-new) ) ]
    )
  )
  (iter lst empty)
)

;(displayln(insertion-sort '()))
;(displayln(insertion-sort '(4 3 6 8 3 0 9 1 7)))
;(displayln(insertion-sort '(1 2 3 4 5 6)))


; Ejercicio 3
(define (deep-reverse lst)
  (define (iter lst lst-new)
    (cond
      [(empty? lst) lst-new]
      [(list? (first lst)) (iter (rest lst) (cons (iter (first lst) empty) lst-new) ) ]
      [else (iter (rest lst) (cons (first lst) lst-new ) )]
    )
  )
  (iter lst empty)
)

;(displayln(deep-reverse '()))
;(displayln(deep-reverse '(a (b c d) 3)))
;(displayln(deep-reverse '((1 2) 3 (4 (5 6)))))
;(displayln(deep-reverse '(a (b (c (d (e (f (g (h i j))))))))))


; Ejercicio 4
(define (insert-anywhere x lst)
  ; Usando un prefijo y sufijo
  (define (iter pre suf lst-new)
    (cond
      [(empty? suf) (reverse (cons (append (reverse pre) (list x) suf) lst-new) )]
      [else (iter (cons (first suf) pre) (rest suf) (cons (append (reverse pre) (list x) suf) lst-new) )]
    )
  )
  (iter empty lst empty)
)

;(displayln(insert-anywhere 1 '()))
;(displayln(insert-anywhere 1 '(a)))
;(displayln(insert-anywhere 1 '(a b c)))


; Ejercicio 5
(define (integral a b n f)
  (if (= n 0) #f
    (let ([h (/ (- b a) n)])
      ; Función recursive para sumatoria
      (define (iter k sum)
        (cond
          [(= k n) (+ (f b) sum)]
          [(= (modulo k 2) 1) (iter (+ k 1) (+ (* (f (+ a (* k h) ) ) 4) sum) )]
          [else (iter (+ k 1) (+ (* (f (+ a (* k h) ) ) 2) sum) )]
          )
        )
      (/ (* h (iter 1 (f a) ) ) 3)
    )
  )
)

#|
(displayln(integral 0 1 10 (lambda (x) (* x x x))))
(displayln
 (integral 1 2 10
   (lambda (x)
     (integral 3 4 10
       (lambda (y)
         (* x y))))))
(displayln (integral 0 3.141592653589793 10 (lambda (x) (sin x))))
(displayln (integral 0 10 10 (lambda (x) 5)))
|#