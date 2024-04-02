def conjunction(p, q):
  return p and q
def implication(p, q):
  return not p or q
def disjunction(p, q):
    return p or q
def bi_implication(p, q):
  return p == q


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