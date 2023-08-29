print('--Game questions python--')
print('-------------------------')
player = input('Qual o seu nome? ')

def game(name):
    acertos = 0
    print(f'Olá {name}\n ')

    if question_1() == 'C':
        acertos += 1
    
    if question_2() == 'B':
        acertos += 1

    if question_3() == 'D':
        acertos += 1


    verifica_pontuacao(acertos, name)
    print('-------------------------------------------------------')
        
def question_1():
    print('Quem criou a linguagem Python? ')
    print('A - Yukihiro Matsumoto')
    print('B - Brendan Eich')
    print('C - Guido van Rossum')
    print('D - Rasmus Lerdorf')
    resposta = input('Digite a letra correspondente a resposta: ').upper()
    print(" ")

    return resposta

def question_2():
    print('Em qual ano foi criado a linguagem Python? ')
    print('A - 1975')
    print('B - 1989')
    print('C - 1991')
    print('D - 2000')
    resposta = input('Digite a letra correspondente a resposta: ').upper()
    print(" ")

    return resposta

def question_3():
    print('Como é declarada uma variavel em Python? ')
    print('A - $name = ""; ')
    print('B - let name = ""; ')
    print('C - char name;')
    print('D - name = "" ')
    resposta = input('Digite a letra correspondente a resposta: ').upper()
    print(" ")

    return resposta

def verifica_pontuacao(acertos, name): 
    if acertos >= 2: 
        print(f'Parabéns {name}, você acertou {acertos} questões...')
    elif acertos < 2:
        print(f'Você precisa estudar mais {name}, você acertou {acertos}...')


game(player)




