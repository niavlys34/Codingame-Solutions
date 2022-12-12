
class Plaque:
    """ Plaque d'immatriculation française
    Représentation numérique et au format AA-001-AA
    """
    _iplaque: int = 0

    def increment(self, i: int) -> None:
        self._iplaque += i
    
    def _itos(self) -> str:
        i = self._iplaque

        n = i % 999
        i //= 999
        d = i % 26
        i //= 26
        c = i % 26
        i //= 26
        b = i % 26
        a = i // 26

        aa = chr(a + 65)
        bb = chr(b + 65)
        cc = chr(c + 65)
        dd = chr(d + 65)
        nn = str(n + 1).zfill(3)

        return f'{aa}{bb}-{nn}-{cc}{dd}'

    def _stoi(self, s: str) -> int:
        a = ord(s[0]) - 65 # int representation of Za-001-aa
        b = ord(s[1]) - 65 # etc.
        c = ord(s[-2]) - 65 # etc.
        d = ord(s[-1]) - 65 # int representation of aa-001-aZ
        n = int(s[3:6]) - 1

        return (((a * 26 + b) * 26 + c) * 26 + d) * 999 + n

    def __init__(self, s) -> None:
        self._iplaque = self._stoi(s)

    def __str__(self) -> str:
        return self._itos()

