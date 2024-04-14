def escolher_wordlist():
    wordlists = {1: 'BRASIL', 2:'INGLES', 3:'PESSOAL'}
    print('Escolha uma wordlist: ')
    print(wordlists)    
    opcao = input('OPCAO: ')
    
    print(f'Voce escolheu a wordlist {wordlists[opcao]}')
    return wordlists[opcao]

def escolher_palavras():
    print('Escolhendo Palavras Manualmente')
    senha = []
    while True:
        print('Digite "q" para sair:')
        palavra = input('Palavra: ')
        senha.append(palavra)
        print(senha)
        
        if palavra == 'q':
            return senha

def iniciar():
    print('''-------------------------
1- Sequencia de Palavras:
2- Sequencia de Letras:''')
    
    opcao = int(input('Opção: '))
    
    if opcao == 1:
        print('Opção Escolhida 1')
        print('1: Escolher Wordlist')
        print('2: Palavras Manualmente')
        
        if opcao == 1:
            escolher_wordlist()
        elif opcao == 2:
            senha = escolher_palavras()
    
    elif opcao == 2:
        print('Opcao escolhida 2')
        print('Metodos de Inclusão')
        
        print('Adicionar Simbolos? ')
        print('Adicionar Numeros? ')
        print('Adicionar Letras?')
        
    else:
        print('Porfavor escolha uma alternativa')
    
def main():
    iniciar()
    
if __name__ == '__main__':
    main()