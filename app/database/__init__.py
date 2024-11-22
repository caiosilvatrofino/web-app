from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase


# database - pasta para separar tudo que é sobre conexão com banco de dados.

class Base(DeclarativeBase):
    """

    Classe que representa toda estrutura de um banco de dados

    """
    ...

    
engine = create_engine('sqlite:///users.db')  

session = Session(engine) 



