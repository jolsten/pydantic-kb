CHAR_TO_A5 = {
    i: c for i, c in enumerate('0123456789ABCDEFGHJKLMNPQRSTUVWXYZ')
}
A5_TO_CHAR = {c: i for i, c in CHAR_TO_A5}


def catalog_number_to_alpha5(v: int) -> str:
    

def alpha5_to_catalog_number(v: str) -> int:
    return v[0] * 10000 + int(v[1:5])

