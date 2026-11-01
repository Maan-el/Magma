from dataclasses import dataclass


@dataclass
class Relacoes:
    pass

@dataclass
class Semantic(Relacoes):
    pass

@dataclass
class Temporal(Relacoes):
    pass

@dataclass
class Causal(Relacoes):
    pass

@dataclass
class Entity(Relacoes):
    pass