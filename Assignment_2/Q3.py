def Throwhankercheif(n, k):
    if n == 1:
        return 0
    return (Throwhankercheif(n - 1, k) + k) % n


print(Throwhankercheif(6, 2))
