from sqlalchemy import ForeignKey, creat_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

db = creat_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session

Base = declarative_base()

# Tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key = True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome
        self.email
        self.senha
        self.ativo


#Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key = True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtd_paginas, dono):
        self.titulo
        self.qtde_paginas
        self.dono

Base.metadata_create_all(bind=db)