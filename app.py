import pymongo
from pymongo import MongoClient
client = MongoClient()
 
client = pymongo.MongoClient('mongodb+srv://padeiro:pao@cluster-gabe.eakkboc.mongodb.net/')
 
db = client['contatos']
contatos_collection = db.contatos

escolha = int(input('------ Menu ----- \n1.Criar contato \n2.Ver contatos \n3.Atualizar contatos \n4.Deletar contatos \nEscolha: '))


if escolha == 1:
    contatos = {
    'nome' : input('nome: '),
    'telefone' : int(input('Telefone: '))
    }
    resultado = contatos_collection.insert_one(contatos)
elif escolha == 2:
    for contato in contatos_collection.find():
        print(contato)

elif escolha == 3:
    query = {
        'nome' : (input('Qual nome deseja modificar: '))      
    }
    new_name = {
        '$set' : {'nome': (input('Novo nome: '))}
        }
    contatos_collection.update_one(query,new_name)  
elif escolha == 4:
    delete_contatos_collection = contatos_collection.delete_one({ 'nome' : (input('Qual nome deseja modificar: '))})
    print(delete_contatos_collection.deleted_count,'Contato deletado')
   
    



