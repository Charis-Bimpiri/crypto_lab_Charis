# Ιχνηλάτηση: `mod_inverse(3, 11)`

Στόχος: να βρούμε το x ώστε `3 · x ≡ 1 (mod 11)`.  
Απάντηση που περιμένουμε: `x = 4` (γιατί 3 × 4 = 12 = 11 + 1).

---

## Βήμα 1: Καλείται η `mod_inverse(3, 11)`

```python
def mod_inverse(a, n):        # a=3, n=11
    gcd, x, _ = extended_gcd(a, n)
    if gcd != 1:
        raise ValueError(...)
    return x % n
```

Η πρώτη γραμμή καλεί την `extended_gcd(3, 11)`.  
Πάμε μέσα σε αυτή.

---

## Βήμα 2: `extended_gcd(3, 11)` — κατεβαίνουμε

```python
def extended_gcd(a, b):       # a=3, b=11
    if b == 0: ...            # 11 != 0, συνεχίζουμε
    gcd, x1, y1 = extended_gcd(b, a % b)
    #              extended_gcd(11, 3%11)
    #              extended_gcd(11, 3)
```

Το `3 % 11 = 3` (γιατί 3 < 11, άρα το υπόλοιπο είναι ο ίδιος ο 3).  
Καλείται η `extended_gcd(11, 3)`. Πάμε μέσα.

---

## Βήμα 3: `extended_gcd(11, 3)` — κατεβαίνουμε

```python
def extended_gcd(a, b):       # a=11, b=3
    if b == 0: ...            # 3 != 0, συνεχίζουμε
    gcd, x1, y1 = extended_gcd(b, a % b)
    #              extended_gcd(3, 11%3)
    #              extended_gcd(3, 2)
```

Το `11 % 3 = 2` (γιατί 11 = 3×3 + 2).  
Καλείται η `extended_gcd(3, 2)`. Πάμε μέσα.

---

## Βήμα 4: `extended_gcd(3, 2)` — κατεβαίνουμε

```python
def extended_gcd(a, b):       # a=3, b=2
    if b == 0: ...            # 2 != 0, συνεχίζουμε
    gcd, x1, y1 = extended_gcd(b, a % b)
    #              extended_gcd(2, 3%2)
    #              extended_gcd(2, 1)
```

Το `3 % 2 = 1` (γιατί 3 = 2×1 + 1).  
Καλείται η `extended_gcd(2, 1)`. Πάμε μέσα.

---

## Βήμα 5: `extended_gcd(2, 1)` — κατεβαίνουμε

```python
def extended_gcd(a, b):       # a=2, b=1
    if b == 0: ...            # 1 != 0, συνεχίζουμε
    gcd, x1, y1 = extended_gcd(b, a % b)
    #              extended_gcd(1, 2%1)
    #              extended_gcd(1, 0)
```

Το `2 % 1 = 0`.  
Καλείται η `extended_gcd(1, 0)`. Πάμε μέσα.

---

## Βήμα 6: `extended_gcd(1, 0)` — βάση αναδρομής, ανεβαίνουμε!

```python
def extended_gcd(a, b):       # a=1, b=0
    if b == 0:
        return a, 1, 0        # return (1, 1, 0)
```

`b == 0`! Σταματάμε και επιστρέφουμε `(1, 1, 0)`.  
Δηλαδή: `gcd=1, x=1, y=0`.  
Επαλήθευση Bezout: `1·1 + 0·0 = 1` ✓

Τώρα **ανεβαίνουμε** πίσω στις κλήσεις που περίμεναν.

---

## Βήμα 7: Επιστροφή στη `extended_gcd(2, 1)`

Έλαβε `(gcd=1, x1=1, y1=0)` από την `extended_gcd(1, 0)`.

```python
# a=2, b=1
gcd, x1, y1 = (1, 1, 0)
x = y1                      # x = 0
y = x1 - (a // b) * y1     # y = 1 - (2//1) * 0 = 1 - 2*0 = 1
return (1, 0, 1)
```

Επαλήθευση Bezout: `2·0 + 1·1 = 1` ✓

---

## Βήμα 8: Επιστροφή στη `extended_gcd(3, 2)`

Έλαβε `(gcd=1, x1=0, y1=1)` από την `extended_gcd(2, 1)`.

```python
# a=3, b=2
gcd, x1, y1 = (1, 0, 1)
x = y1                      # x = 1
y = x1 - (a // b) * y1     # y = 0 - (3//2) * 1 = 0 - 1*1 = -1
return (1, 1, -1)
```

Επαλήθευση Bezout: `3·1 + 2·(-1) = 3 - 2 = 1` ✓

---

## Βήμα 9: Επιστροφή στη `extended_gcd(11, 3)`

Έλαβε `(gcd=1, x1=1, y1=-1)` από την `extended_gcd(3, 2)`.

```python
# a=11, b=3
gcd, x1, y1 = (1, 1, -1)
x = y1                      # x = -1
y = x1 - (a // b) * y1     # y = 1 - (11//3) * (-1) = 1 - 3*(-1) = 1 + 3 = 4
return (1, -1, 4)
```

Επαλήθευση Bezout: `11·(-1) + 3·4 = -11 + 12 = 1` ✓

---

## Βήμα 10: Επιστροφή στη `extended_gcd(3, 11)`

Έλαβε `(gcd=1, x1=-1, y1=4)` από την `extended_gcd(11, 3)`.

```python
# a=3, b=11
gcd, x1, y1 = (1, -1, 4)
x = y1                      # x = 4
y = x1 - (a // b) * y1     # y = -1 - (3//11) * 4 = -1 - 0*4 = -1
return (1, 4, -1)
```

Επαλήθευση Bezout: `3·4 + 11·(-1) = 12 - 11 = 1` ✓

---

## Βήμα 11: Επιστροφή στη `mod_inverse(3, 11)`

Έλαβε `(gcd=1, x=4, _=-1)` από την `extended_gcd(3, 11)`.

```python
# a=3, n=11
gcd, x, _ = (1, 4, -1)
if gcd != 1: ...            # gcd == 1, δεν πετάμε error
return x % n                # 4 % 11 = 4
```

---

## Αποτέλεσμα: `4` ✓

`3 × 4 = 12 = 11 + 1 ≡ 1 (mod 11)` ✓

---

## Σύνοψη των κλήσεων

```
mod_inverse(3, 11)
  └── extended_gcd(3, 11)
        └── extended_gcd(11, 3)
              └── extended_gcd(3, 2)
                    └── extended_gcd(2, 1)
                          └── extended_gcd(1, 0) → (1, 1, 0)  ← βάση
                    ← (1, 0, 1)
              ← (1, 1, -1)
        ← (1, -1, 4)
  ← (1, 4, -1)
→ return 4
```
