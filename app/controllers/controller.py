from models import Player


def add_player():
    """Add a new player in the db"""
    first_name = input("First name:")
    last_name = input("Last name :")
    birth = input("Birthday (dd/mm/yyyy format):")
    while birth != r"\d{2}\/\d{2}\/\d{4}":
        birth = input("Format not valid.\nBirthday (dd/mm/yyyy format):")
    sex = input("Sex (f/m/o):").upper()
    while birth != r"[fmo]":
        birth = input("Answer must be f, m or o.\nSex (f/m/o):")
    rank = input("Rank: ")
    return Player(first_name, last_name, birth, sex, rank)
