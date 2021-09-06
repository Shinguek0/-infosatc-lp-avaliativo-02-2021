#Faça 4 listas:
#A. Filmes
#B. Jogos
#C. Livros
#D. Esporte

#a. Adicione no mínimo 2 itens em cada lista. V
#b. Crie uma lista das 4 listas criadas acima. V
#c. Acesse (mostrar) algum item da lista livros. V
#d. Remova um item da lista esporte. V
#e. Adicione uma lista chamada “disciplinas”, no item b. (sem criar uma lista separada).


ListaFilmes = ["baby driver", "star wars"]
ListaJogos = ["Adastra", "password"]
ListaLivros = ["O principe", "Leviata"]
ListaEsporte = ["volei", "Tenis"]

Lista = ListaFilmes + ListaJogos + ListaLivros + ListaEsporte

#print(Lista)   # Imprime a lsita o mas 4 listas
print("Item da lista livro:", ListaLivros[0])  #imprime um iten d alista livros

del ListaEsporte[1]  #deleta o esporte tenis
#print(ListaEsporte)  #printa a lista esporte sem tenis

ListaDisciplinas = ["Matematica","Quimica"]
Lista = Lista + ListaDisciplinas

print("Lista final ",Lista)