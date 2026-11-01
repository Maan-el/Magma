from dataclasses import dataclass


@dataclass
class Personagem:
    nome: str = ""
    descricao: str = ""
    personalidade: str = ""
    cenario: str = ""

@dataclass
class Fulana(Personagem):
    nome: str = "Fulana"
    descricao: str = "Uma pessoa aleatória"

@dataclass
class Fulano(Personagem):
    nome: str = "Fulano"
    descricao: str = "Um cara aleatório"