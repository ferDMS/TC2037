#lang racket
; Ejemplo 1
(define (duplicate lst)
  (define (iter lst lst-dup)
    (cond
      [(empty? lst) (reverse lst-dup)]
      [else (iter (rest lst) (cons (first lst) (cons (first lst) lst-dup)))]))
  (iter lst empty)
)


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


; Ejemplo 4
(define (swapper a b lst)
  (define (swap elem lst-new)
    (cond
      [(= elem a) (cons b lst-new)]
      [(= elem b) (cons a lst-new)]
      [else (cons elem lst-new)]
    )
  )
  (define (iter lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter (rest lst) (swap (first lst) lst-new) )]
    )
  )
  (iter lst empty)
)


; Ejemplo 5
(define (replic n lst)
  (define (replic-elmnt elmnt n lst-elmnt)
    (cond
      [(= n 0) lst-elmnt]
      [else (replic-elmnt elmnt (- n 1) (cons elmnt lst-elmnt) )]
    )
  )
  (define (iter n lst lst-new)
    (cond
      [(empty? lst) (reverse lst-new)]
      [else (iter n (rest lst) (append (replic-elmnt (first lst) n empty) lst-new) )]
    )
  )
  (iter n lst empty)
)


; Ejemplo 6
(define (binary n)
  (define (iter n bnry-lst)
    (cond
      [(= n 0) bnry-lst]
      [else (iter (quotient n 2) (cons (modulo n 2) bnry-lst))]
    )
  )
  (iter n empty)
)


; Ejemplo 7
(define (prime-factors num)
  (define (is-prime? n)
    (define (is-divisible? divisor)
      (cond
        [(> (* divisor divisor) n) #t]
        [(= (modulo n divisor) 0) #f]
        [else (is-divisible? (+ divisor 1))]
      )
    )
    ; Check whether you can or can't divide exactly all nums from 2 to n-1.
    ; This works because we will get to a point at which either:
      ; A divisor^2 is greater than n, meaning no number below it was able to divide n exactly
      ; An n / divisor operation will have remainder 0, which means n is divisible and thus not a prime
    (is-divisible? 2) 
  )
  (define (next-prime n)
    (cond
      [(is-prime? (+ n 1)) (+ n 1)]
      [else (next-prime (+ n 1))]
    )
  )
  (define (iter n cur-prime lst-primes)
    (cond
      [(= n 1) (reverse lst-primes)]
      [(= (modulo n cur-prime) 0) (iter (/ n cur-prime) cur-prime (cons cur-prime lst-primes) )]
      [else (iter n (next-prime cur-prime) lst-primes )]
    )
  )
  (iter num 2 empty)
)


; Ejemplo 8
(define (rotate-left n lst)
  (define (iter i lst-new)
    (cond
      [(= i (length lst)) (reverse lst-new)]
      [else (iter (+ i 1) (cons (list-ref lst (modulo (+ n i) (length lst) ) ) lst-new) )]
    )
  )
  (iter 0 empty)
)


; Ejemplo 9
(define (there-exists-one? pred lst)
  (cond
    [(empty? lst) #f]
    [(pred (first lst)) #t]
    [else (there-exists-one? pred (rest lst) ) ]
  )
)


; Ejemplo 10
(define (linear-search lst x eq-fun)
  (define (iter lst idx)
    (cond
      [(empty? lst) #f]
      [(eq-fun x (first lst) ) idx]
      [else (iter (rest lst) (+ idx 1) )]
    )
  )
  (iter lst 0)
)


; Extra 1
(define (gcd a b)
  ; Función para obtener todos los divisores comúnes
  (define (common-div-lst a b cur-div lst)
    (cond
      [(or (> cur-div a) (> cur-div b) ) (reverse lst)]
      [(and (= (modulo a cur-div) 0) (= (modulo b cur-div) 0) ) (common-div-lst (/ a cur-div) (/ b cur-div) cur-div (cons cur-div lst) )]
      [else (common-div-lst a b (+ cur-div 1) lst)]
    )
  )
  ; Función para multiplicar todos los elementos en la lista
  (define (mult-lst lst)
    (define (iter lst res)
      (cond
        [(empty? lst) res]
        [else (iter (rest lst) (* (first lst) res) )]
      )
    )
    (cond
      [(empty? lst) #f]
      [else (iter lst 1)]
    )
  )
  ; Llamar a la función para obtener todos los divisores comunes
  ; Después con la lista multiplicar todos para obtener mcd
  (mult-lst (common-div-lst a b 2 '(1) ) )
)


#|
; Extra 2
La función pack toma una lista como entrada. Devuelve una lista de listas que agrupan los elementos iguales consecutivos.
(pack '(a a a b b c a a)) -> '((a a a) (b b) (c) (a a))

; Extra 3
(compress '(a b c d)) -> '(a b c d)
(compress '(a a a b b c c a)) -> '(a b c a)

; Extra 4
(encode '(a a a b c c)) -> '(3 a) (1 b) (2 c))
(encode '(1 2 3 4)) -> ((1 1) (1 2) (1 3) (1 4))
|#

(display "Ejemplo 1\n")
(displayln (duplicate '(1 2 3 4)))

(display "Ejemplo 2\n")
(displayln (enlist '('(1 2) 3 4)))

(display "Ejemplo 3\n")
(displayln (invert-pairs '(("1a" "1b") ("2a" "2b") ("3a" "3b") )))

(display "Ejemplo 4\n")
(displayln (swapper 1 2 '(1 4 2)) )

(display "Ejemplo 5\n")
(displayln (replic 2 '(1 2 3 4) ) )

(display "Ejemplo 6\n")
(displayln (binary 30) )

(display "Ejemplo 7\n")
(displayln (prime-factors 96) )

(display "Ejemplo 8\n")
(displayln (rotate-left 4 '(1 2 3 4 5 6 7 8) ) )

(display "Ejemplo 9\n")
(displayln (there-exists-one? negative? '(1 2 3 -4) ) )
(displayln (there-exists-one? negative? '(1 2 3 4) ) )

(display "Ejemplo 10\n")
(displayln (linear-search '(48 77 30 31 5 20 91 92 69 97 28 32 17 18 96) 18 =) )

(display "Extra 1\n")
(displayln (gcd 13 7919)) ; 1
(displayln (gcd 20 16))   ; 4
(displayln (gcd 72 54))   ; 18
(displayln (gcd 100 75))  ; 25