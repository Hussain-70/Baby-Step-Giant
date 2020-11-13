from math import ceil, sqrt


def bsg(g, h, p):
    N = ceil(sqrt(p - 1))

    # the next two lines will generate the list for the congruences
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)

    # Looking for matches in the two sets created
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    return None

if __name__ == '__main__':
    alpha = int(input("Enter the base: "));
    beta = int(input("Enter the beta value: "));
    prime = int(input("Enter the prime number: "));
    print(bsg(alpha, beta, prime))