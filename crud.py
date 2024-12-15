from main import *

# CRUD

# C - Create
usuario = Usuario(nome="Felipe", email="teste@email.com", senha="123456")
session.add(Usuario)
session.commit()

usuario_felipe = session.query(Usuario).filter_by(email="teste@email.com").first()
livro = Livro(nome="O Hobbit", qtd_paginas=227, dono=usuario_felipe.id)
session.add(livro)
session.commit()

# R - Read
lista_usuarios = session.query(Usuario).all()

# U - Update
usuario_felipe.nome = "Felipe Silva"
session.add(Usuario)
session.commit()

# D - Delete
usuario_felipe2 = session.query(Usuario).filter_by(email="teste@email.com").first()
session.delete(usuario_felipe2)
session.commit()