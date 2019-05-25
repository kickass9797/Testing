def prim_root(m):
    teiler = divisors(phi(m))
    for i in range(1, phi(m) + 1):
        for e in teiler:
            if (i ** e % m == 1):
                print(f"ord({i}) = {e}")
                break

def divisors(m):
    return [x for x in range(1, m + 1) if m % x == 0]

def phi(m):
    return len([x for x in range(1, m) if euklid(x, m) == 1])

def euklid(a,b):
    while b != 0:
        a, b = b, a % b
    return a

prim_root(11)
prim_root(13)



