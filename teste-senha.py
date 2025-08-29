import bcrypt

senha_clara = b"minhasenhasegura123" # A senha deve ser em bytes
senha_hash = bcrypt.hashpw(senha_clara, bcrypt.gensalt())
print(senha_hash)

senha_fornecida = b"minhasenhasegura123"
if bcrypt.checkpw(senha_fornecida, senha_hash):
    print("Senha correta!")
else:
    print("Senha incorreta.")