import pymongo as pyM
from pprint import pprint

# Conectando ao MongoDB / Conecta ao cluster
client = pyM.MongoClient("mongodb connection string") # string retirada do mongodb atlas

# Buscando coleções
db = client.clientes # cria o db chaamado 'clientes'
collection = db.bank # cria a coleção chamada bank


# Inserindo dados na coleção bank
posts = [{
    "nome" : "Antonio Silva",
    "cpf": "123456",
    "endereço": "Rua 16A, 102",
    "conta": "001",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Valdir Lopes",
    "cpf": "654321",
    "endereço": "Rua 15A, 101",
    "conta": "002",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Bruno Sales",
    "cpf": "456123",
    "endereço": "Rua 12A, 51",
    "conta": "003",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Tayanne Cardoso",
    "cpf": "321654",
    "endereço": "Rua 11A, 131",
    "conta": "004",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}]

# postando = collection.insert_many(posts)

post = {
    "nome" : "Milton Fernandes",
    "cpf": "564231",
    "endereço": "Rua 5A, 12",
    "conta": "005",
    "agencia": "0002",
    "tipo" : "corrente",
    "saldo": 0
}
# postando = collection.insert_one(post)


# Recuperando dados da collection bank

pprint(collection.find())
find = collection.find()
for post in find:
    pprint(post)

print(collection.count_documents({}))

print(collection.count_documents({"agencia": "0001"}))

for post in collection.find({}).sort("nome"): # sort("campo a ser ordenado")
    pprint(post)


# Exclui a coleção bank
# db['bank'].drop()


