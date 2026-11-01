from typing import Optional

from data.entities.Personagem import Personagem, Fulano, Fulana


def escolher_personagem(nome: str) -> Optional[Personagem]:
    match nome:
        case "Fulano":
            return Fulano()
        case "Fulana":
            return Fulana()
        case _:
            return None