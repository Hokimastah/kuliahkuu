#1.1 nomor 37
def conjunction(p, q):
  return p and q
def implication(p, q):
  return not p or q
def disjunction(p, q):
    return p or q
def bi_implication(p, q):
  return p == q


# a) p → (¬q ∨ r)
print("p       q       r    ¬q ∨ r    p → (¬q ∨ r) ")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            qr = disjunction(not q,r)
            a = implication(p,qr)
            print(f"{p}   {q}   {r}    {qr}       {a}")

# b) ¬p → (q → r)
print("¬p       q       r     q → r   ¬p → (q → r) ")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            qr = implication(q,r)
            a = implication(not p,qr)
            print(f"{p}   {q}   {r}    {qr}       {a}")

# c) (p → q) ∨ (¬p → r)
print("p       q       r     p → q   ¬p → r   (p → q) ∨ (¬p → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p,q)
            pr = implication(not p,r)
            a = disjunction(pq,pr)
            print(f"{p}   {q}   {r}    {pq}       {pr}         {a}")

# d) (p → q) ∧ (¬p → r)
print("p       q       r     p → q   ¬p → r   (p → q) ∨ (¬p → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p,q)
            pr = implication(not p,r)
            a = conjunction(pq,pr)
            print(f"{p}   {q}   {r}    {pq}       {pr}         {a}")

# e) (p ↔ q) ∨ (¬q ↔ r)
print("p       q       r     p <=> q   ¬q <=> r   (p ↔ q) ∨ (¬q ↔ r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = bi_implication(p,q)
            qr = bi_implication(not q,r)
            a = disjunction(pq,qr)
            print(f"{p}   {q}   {r}    {pq}       {qr}         {a}")
            
# f) (¬p ↔ ¬q) ↔ (q ↔ r)
print("p       q       r     ¬p <=> ¬q   q <=> r   (¬p↔¬q)↔(q↔r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = bi_implication(not p,not q)
            qr = bi_implication(q,r)
            a = bi_implication(pq,qr)
            print(f"{p}   {q}   {r}    {pq}       {qr}         {a}")



#1.1 nomor 42 
# what is the value of x after each of these statements is
# encounter Wed in a computer program, if x = 1 before the
# statement is reached?
# a) if x + 2 = 3 then x := x + 1

# b) if (x + 1 = 3) OR (2x + 2 = 3) then x := x + 1
       
# c) if (2x + 3 = 5) AND (3x + 4 = 7) then x := x + 1
      
# d) if (x + 1 = 2) XOR (x + 2 = 3) then x := x + 1
      
# e) if x < 2 then x := x + 1
      

#1.3 nomor 10
"""Show that each of these conditional statements is a tautology by using truth tables."""
# a) [¬p ∧ (p ∨ q)] → q
print('  p       q      (p ∨ q)   ¬p ∧ (p ∨ q)   [¬p ∧ (p ∨ q)] → q')
for p in [True,False]:
    for q in [True,False]:
        pq = disjunction(p, q)
        a = conjunction(not p, pq)
        b = implication(a, q)
        print(F'{p}    {q}      {pq}           {a}             {b}')

    
# b) [(p → q) ∧ (q → r)] → (p → r)
print('  p       q       r    (p → q)    (q → r)    [(p → q) ∧ (q → r)]     (p → r)      [(p → q) ∧ (q → r)] → (p → r)')
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = implication(p, q)
            qr = implication(q, r)
            a = conjunction(pq, qr)
            pr = implication(p, r)
            b = implication (a, pr)
            print(F"{p}    {q}    {r}     {pq}      {qr}            {a}             {pr}                 {b}")

# c) [p ∧ (p → q)] → q
print('  p     q   (p → q)   p ∧ (p → q)   [p ∧ (p → q)] → q')
for p in [True,False]:
    for q in [True,False]:
        pq = implication(p, q)
        a = conjunction(p, pq)
        b = implication(a, q)
        print(F"{p}   {q}     {pq}       {a}       {b}")

# d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r
print('  p     q     r     (p ∨ q)   (p → r)   (q → r)  [(p ∨ q) ∧ (p → r) ∧ (q → r)]  [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r')
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = disjunction(p, q)
            pr = implication(p, r)
            qr = implication(q, r)
            a = conjunction(pq, pr)
            c = conjunction(a, qr)
            b = implication(a, r)
            print(F"{p}   {q}   {r}   {pq}     {pr}      {qr}              {c}                        {b}")

#1.3 nomor 32
"""Show that (p ∧ q) → r and (p → r) ∧ (q → r) are not
logically equivalent.
"""
print("p        q       r    (p ∧ q)  (p ∧ q) → r    (p → r)    (q → r)     (p → r) ∧ (q → r)")
for p in [True,False]:
    for q in [True,False]:
        for r in [True,False]:
            pq = conjunction(p,q)
            a = implication(pq,r)
            pr = implication(p,r)
            qr = implication(q,r)
            b = conjunction(pr,qr)
            print(f"{p}   {q}   {r}  {pq}       {a}         {pr}        {qr}         {b}")
print(F"dapat di lihat pada tabel di atas bahwa kedua pernyataan tidak equivalent")
