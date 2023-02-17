class Carta:

    CORAZON: str = 'Corazon'
    TREBOL: str = 'Trebol'
    PICAS: str = 'Picas'
    DIAMANTES: str = 'Diamantes'

    def __init__(self, valor: str, pinta: str):
        
        self.valor: str = valor
        self.pinta: str = pinta