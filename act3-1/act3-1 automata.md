# 1

## 1

```
#states
s0
s1
s2
s3
s4
#initial
s0
#accepting
s0
s1
s2
s3
#alphabet
a
b
#transitions
s0:a>s0
s0:b>s1
s1:a>s2
s1:b>s1
s2:a>s0
s2:b>s3
s3:a>s4
s3:b>s1
s4:a,b>s4
```

## 2

```
#states
s0
s1
s2
s3
#initial
s0
#accepting
s0
s1
s2
#alphabet
a
b
#transitions
s0:a>s1
s0:b>s2
s1:a>s1
s1:b>s3
s2:a>s3
s2:b>s2
s3:a>s3
s3:b>s3
```

## 3

```
#states
s0
s1
s2
s3
#initial
s0
#accepting
s3
#alphabet
a
b
#transitions
s0:a>s1
s0:b>s2
s1:a>s1
s1:b>s3
s2:a>s3
s2:b>s2
s3:a>s3
s3:b>s3
```

## 4

```
#states
s0
s1
s2
s3
s4
s5
#initial
s0
#accepting
s5
#alphabet
a
b
#transitions
s0:a,b>s1
s1:a,b>s2
s2:a,b>s3
s3:a,b>s4
s4:a,b>s5
s5:a,b>s5
```

# 2

## 1

```
#states
s0
s1
s2
#initial
s0
#accepting
s2
#alphabet
0
1
#transitions
s0:0,1>s0
s0:0>s1
s1:0>s2

```

## 2

```
#states
s0
s1
s2
s3
s4
s5
#initial
s0
#accepting
s4
#alphabet
0
1
#transitions
s0:0,1>s0
s0:0>s1
s1:1>s2
s2:0>s3
s3:1>s4
```

## 3

Primera parte
```
#states
s0
s1
s2
#initial
s0
#accepting
s2
#alphabet
0
1
#transitions
s0:0>s1
s0:1>s0
s1:0>s2
s1:0>s0
s1:1>s1
s2:1>s2
```

Completo
```
#states
s0
a0
a1
b0
b1
b2
#initial
s0
#accepting
a0
b2
#alphabet
0
1
#transitions
s0:$>b0
s0:$>a0
a0:0>a1
a0:1>a0
a1:0>a0
a1:1>a1
b0:1>b1
b0:0>b0
b1:0>b1
b1:1>b2
b2:0>b2
```

## 4

# 3

## 1

DFA

```
#states
1
2
#initial
1
#accepting
1
#alphabet
a
b
#transitions
1:a>1
1:a,b>2
2:b>1
```

NFA

```

```
