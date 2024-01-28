def solution(n):
    def fac(n):
        if n == 1:
            return 1
        return n * fac(n - 1)
    return fac(2*n) // (fac(n+1)*fac(n))