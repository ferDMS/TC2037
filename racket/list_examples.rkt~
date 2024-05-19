#lang racket
; Ejemplo 1
(define (duplicate lst)
  (define (iter lst lst-dup)
    (cond
      [(empty? lst) (reverse lst-dup)]
      [else (iter (rest lst) (cons (first lst) (cons (first lst) lst-dup)))]))
  (iter lst empty))

; (displayln (duplicate '(1 2 3 4))) ; Uso


; Ejemplo 2
(define (enlist lst)
  (define (iter lst enlsted)
    (cond
      [(empty? lst) (reverse enlsted)] ; Caso base
      [else (iter (rest lst) (cons (cons (first lst) empty) enlsted))])
      ; [else (iter (rest lst) (cons (list (first lst)) enlsted))])
  )
  (iter lst empty)
)

; (displayln (enlist '('(1 2) 3 4))) ; Uso


; Ejemplo 3
(define (invert-pairs lst)
  (define (invert pair-lst)
    (list (list-ref pair-lst 1) (list-ref pair-lst 0))
  )
  (define (iter lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter (rest lst) (cons (invert (first lst)) lst-new) ) ]
    )
  )
  (iter lst empty)
)

; (displayln (invert-pairs '(("1a" "1b") ("2a" "2b") ("3a" "3b") ))) ; Uso


; Ejemplo 4
(define (swapper a b lst)
  (define (iter a b lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter (rest lst) () )]
    )
  )
  (iter a b lst lst-new)
)