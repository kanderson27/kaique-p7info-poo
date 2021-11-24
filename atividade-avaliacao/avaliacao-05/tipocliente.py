"""
    Modulo tipocliente -
    Classe TipoCliente - Enumeration de Tipos de Cliente
"""

import enum


class TipoClient(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2


if _name_ == '_main_':
    print("Os numeros enum sao: ")
    for tipo in (TipoClient):
        print(type(tipo))
        print(tipo)
    
  