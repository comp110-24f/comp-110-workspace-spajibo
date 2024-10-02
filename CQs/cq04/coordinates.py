"Doc string/ idk what to say yet"
__author__ = 730671372


def get_coords(xs: str, ys: str) -> None:

    i1 = 0
    i2 = 0
    es = ""

    while i1 < len(xs):
        while i2 < len(ys):
            es += f"({xs[i1]},{ys[i2]})"
            print(es)
            i2 += 1
            es = ""
        i1 += 1
        i2 = 0
