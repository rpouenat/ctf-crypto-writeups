# filename: solver.sage

a = 1234577
b = 3213242
M = 7654319

E = EllipticCurve(GF(M), [0, 0, 0, a, b])

base = E([5234568, 2287747])
pub = E([2366653, 1424308])

c1 = E([5081741, 6744615])
c2 = E([610619, 6218])

X = base

for i in range(1, M):
    if X == pub:
        secret = i
        print "[+] secret:", i
        break
    else:
        X = X + base
        print i

#secret  = 1584718

m = c2 - (c1 * secret)

print "[+] x:", m[0]
print "[+] y:", m[1]
print "[+] x+y:", m[0] + m[1]

# [+] x+y: 5720914
