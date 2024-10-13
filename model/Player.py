from dataclasses import dataclass


@dataclass
class Player:
    """Class for keeping track of a player"""
    mar: float
    tak: float
    tec: float
    pas: float
    cro: float
    fin: float
    hea: float
    lon: float
    pos: float
    sta: float
    pac: float

    """Gk specific"""
    han: float
    one: float
    ref: float
    aer: float
    ele: float
    jum: float
    kic: float
    thr: float

    """non-skill attributes"""
    name: str
    no: int
    form: float
    routine: float
    rating: int
