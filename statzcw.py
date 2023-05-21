from math import sqrt


def zcount(l: list) -> float:
    return float(len(l))


def zmean(l: list) -> float:
    return float(sum(l) / zcount(l))


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
        return l[length // 2]
    else:
        return zmean([l[length // 2], l[(length // 2) - 1]])


def zvariance(l: list) -> float:
    mean = zmean(l)
    deviations = []
    for n in l:
        deviations.append((mean - n) ** 2)
    return sum(deviations) / (len(l) - 1)


def zstddev(l: list) -> float:
    return sqrt(zvariance(l))


def zstderr(l: list) -> float:
    return zstddev(l) / sqrt(zcount(l))


def cov(lx: list, ly: list):  # covariance
    add_it_up = 0
    if lx != ly:
        for i in range(0, len(lx)):
            add_it_up += ((lx[i] - zmean(lx)) * (ly[i] - zmean(ly)))
        return add_it_up / (len(lx) - 1)


def zcorr(lx: list, ly: list) -> float:
    return cov(lx, ly) / (zstddev(lx) * zstddev(ly))

