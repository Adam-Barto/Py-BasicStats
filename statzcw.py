# - zvariance(list: List[]) -> float
# - zstddev(list: List[]) -> float
# - zstderr(list: List[]) -> float
# - zcorr(listx: List[], listy: List[]) -> float
#
# - python builtin `sum()`
# - python builtin `max()`
# - python builtin `min()`
# - python Math function `Math.sqrt()`
# - python normal operators on floats (*, /, +, -, etc)

def zcount(l: list) -> float:
    return float(len(l))

def zmean(l: list) -> float:
    return float(sum(l)/zcount(l))

def zmode(l: list) -> float:
    c = ['', 0]
    for n in l:
        if c[1] < l.count(n):
            c = [n, l.count(n)]
    return float(c[0])

def zmedian(l: list) -> float:
    l.sort()
    length = len(l)
    if length % 2 == 1:
        return l[length//2]
    else:
        return zmean([l[length//2], l[(length//2)-1]])






