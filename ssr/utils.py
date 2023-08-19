CHAR_TO_A5 = {
    i: c for i, c in enumerate('0123456789ABCDEFGHJKLMNPQRSTUVWXYZ')
}
A5_TO_CHAR = {c: i for i, c in CHAR_TO_A5.items()}


def catalog_number_to_alpha5(v: int) -> str:
    lower4 = v % 10_000
    digit1 = int( (v - lower4) / 10_000 )
    char1 = CHAR_TO_A5[digit1]
    return f'{char1}{lower4:04}'

def alpha5_to_catalog_number(v: str) -> int:
    return A5_TO_CHAR[v[0]] * 10_000 + int(v[1:5])
