from sqlalchemy import creat_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

db = creat_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session

Base = declarative_base()

# Tabelas
class Usuario(Base):
    id = Column("id", Integer)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

#Livros
class Livro(Base):
    id = Column("id", Integer)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", String)