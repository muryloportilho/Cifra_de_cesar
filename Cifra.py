# ==============================================================================
# =                                VARIAVEIS                                   =  
# ==============================================================================

# Essa é a veriavel de rotações no alfabeto.
# É iniciada como -1, pois 0 é a letra a.
seed = -1

# ==============================================================================
# =                                FUNÇÕES                                     =
# ==============================================================================

#--------------------------------------------MOSTRAR O MENU--------------------------------------------
# Função responsavel por mostrar o cabeçalho.
def mostrar_menu():
    print("""
          
\t ██████╗██╗███████╗██████╗  █████╗     ██████╗ ███████╗     ██████╗███████╗███████╗ █████╗ ██████╗ 
\t██╔════╝██║██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
\t██║     ██║█████╗  ██████╔╝███████║    ██║  ██║█████╗      ██║     █████╗  ███████╗███████║██████╔╝
\t██║     ██║██╔══╝  ██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗
\t╚██████╗██║██║     ██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗███████╗███████║██║  ██║██║  ██║
\t ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    """)

    print("""            
\t\t.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
\t\t|                                                                   |
\t\t|    Aviso: Você precisa definir o número de seed primeiro!         |       
\t\t|                                                                   |
\t\t|    1. Criptografar                                                |
\t\t|    2. Descriptografar                                             |
\t\t|    3. Definir Número de Seed                                      |
\t\t|    4. Instrução                                                   |
\t\t|    5. Sair                                                        |
\t\t:                                                                   :
\t\t`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-----'
          
    """)

#--------------------------------------------MENSAGEM BOX--------------------------------------------
# Função responsavel por mostrar mensagens com modelo editado.

def mensagem_box(mensagem):
    print(f"""            
\t.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
           
\t{mensagem}
   
\t.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
    """)

#--------------------------------------------MENSAGEM INSTRUÇÃO--------------------------------------------
# Função responsavel por mostrar o box de instruções do aplicativo.

def mensagem_instrucao():
    print("""               
\t\t.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
\t\t|                                                                                   |
\t\t|    1. Criptografar   - É usado para ocultar sua mensagem                          |
\t\t|    2. Descriptografar - É usado para transformar sua mensagem na original         |
\t\t|    3. Numero de seed  - É usado para definir o numero de voltas no alfabeto       |
\t\t|    4. Instrução  - É usado para aparecer as informações de como usar o programa   |
\t\t|    5. Sair  - É usado para finalizar o programa                                   |
\t\t:                                                                                   :
\t\t|    Obs: Quando for copiar a mensagem criptografada ou descriptografada, não       |
\t\t|     Utilizar o atalho "CTRL + C", se não o programa é finalizado.                 |
\t\t:     Você pode utilizar o atalho "CTRL + SHIFT + C"                                :
\t\t|                                                                                   |
\t\t`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-='
    """)

#--------------------------------------------SISTEMA DE CIFRA--------------------------------------------
# Função responsavel por criptografar ou descriptografar a mensagem.

def funcao_cifra(Operacao, mensagem):

    # Inicializa a variável mensagemcripto que vai receber a mensagem do usuario.
    mensagemcripto = input(f"\tEscreva a frase para {mensagem}: ")

    # A variavel resultado é setada como vazia para não carregar mensagens antigas.
    resultado = ""

    # Inicializa um loop das letras dentro da mensagem do usuario.
    for caracteres in mensagemcripto:

        # Verifica se é uma mensagem e não um numero.
        if caracteres.isalpha():

            # Foi utilizado um opérador ternario (Que é um if / else), a variavel inicioalfabeto recebe o numero 65 se for maiuscula ou se não for, 97.
            # Foram usados parametros da tabela ASCII - https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm
            inicioalfabeto = 65 if caracteres.isupper() else 97

            # Verifica se o parametro "Operacao" passado pela função é "+" ou "-", para o sistema saber se precisa somar ou subtrair as letras do alfabeto
            if Operacao == "+":

                # Inicializa a variável cifra que vai guardar o resultado da operação.
                # inicioalfabeto armazena o valor ASCII do primeiro caractere do alfabeto.
                # Utiliza a função ord() para pegar o valor ASCII do caractere atual.
                # Subtrai inicioalfabeto para zerar o valor do caractere para começar de 0.
                # Adiciona seed para aplicar um deslocamento ao valor do caractere, realizando a criptografia ou descriptografia.
                # Usa o operador % 26 para garantir que o valor criptografado esteja dentro do limite do alfabeto.
                # Se o valor passar de "z", ele vai voltar para o início do alfabeto.
                cifra = inicioalfabeto + ((ord(caracteres) - inicioalfabeto + seed) % 26)
            elif Operacao == "-":
                cifra = inicioalfabeto + ((ord(caracteres) - inicioalfabeto - seed) % 26)

            # Utiliza a função chr() que é a contraparte do ord(), enquanto ord() transforma em inteiro, chr() transforma em string.
            # Adiciona na variavel "resultado" o resultado da ordem criptografada ou descriptografada.
            resultado += chr(cifra)

        # Se a mensagem do usuario for um numero.
        else:

            # Apenas adiciona o numero na variavel resultado.
            resultado += caracteres

    # Aqui printa o resultado chamando a função mensagem_box
    mensagem_box(f"Mensagem {mensagem}: {resultado}")

# ==============================================================================
# =                                LOOP DO PROGRAMA                            =
# ==============================================================================

# Aqui se inicia o loop responsavel pelo programa.
while True:
    # Chamada da função de printar o menu.
    mostrar_menu()

    # Inicializa a variavel escolha, que irá receber o numero das opções do menu.
    escolha = input("\tEscolha uma opção: ")

    # Se escolher o numero 1:
    if escolha == '1':
        
        # Se o numero de voltas for igual a -1 (Não coloquei 0, porque o 0 conta como "A").
        if seed == -1:

            # Printa erro por não ter escolhido a seed antes de escolher essa opção.
            mensagem_box("ERRO: Você precisa escolher o numero de seeds primeiro")

        # Se for diferente de -1:
        else:

            # Chama a função de criptografar ou descriptografar.
            # Foi passado o parametro "+", para somar os caracteres, e a mensagem "criptografada" para ser printada na mensagem.
            funcao_cifra("+", "criptografada")

    # Se escolher o numero 2:
    elif escolha == '2':

        # Se o numero de voltas for igual a -1 (Não coloquei 0, porque o 0 conta como "A")
        if seed == -1:

            # Printa erro por não ter escolhido a seed antes de escolher essa opção.
            mensagem_box("ERRO: Você precisa escolher o numero de seeds primeiro")

        # Se for diferente de -1:
        else:

            # Chama a função de criptografar ou descriptografar.
            # Foi passado o parametro "-", para subtrair os caracteres, e a mensagem "descriptografada" para ser printada na mensagem.
            funcao_cifra("-", "descriptografada")

    # Se escolher o numero 3:     
    elif escolha == '3':

        # Verifica se o usuario utiliza um numero inteiro.
        try:
            # A variavel seed recebe o numero de voltas do usuario.
            seed = int(input("\tDigite o número de seed: "))

            # Chama a função mensagem_box, printando a mensagem do numero de seed do usuario.
            mensagem_box(f"Você escolheu o numero de seed igual a {seed}")

        # Se o usuario tiver utilizado uma letra.
        except ValueError:

            # Chama a função mensagem_box, printando erro por ter escolhido uma letra.
            mensagem_box("ERRO: Você digitou uma letra")

    # Se escolher o numero 4:
    elif escolha == '4':

        # Chama a função mensagem_instrucao, mostrando o menu de instruções.
        mensagem_instrucao()

    # Se escolher o numero 5:
    elif escolha == '5':

        # Printa a mensagem que está finalizando o programa.
        mensagem_box(f"Você finalizou o programa, Muito Obrigado por participar!")

        # Finaliza o loop, fazendo o programa finalizar.
        break

    # Se não for nenhuma das alternativas do menu.
    else:

        #Chama a função mensagem_box, printando que é uma opção invalida e volta o programa para o começo.
        mensagem_box("Opção inválida, tente novamente")

    # Sempre que é escolhido uma opção, o programa espera alguma tecla para continuar, usado para o usuario ver o resultado da resposta.
    input("\tPressione ALGUMA TECLA para continuar...")

    # 033c é uma sequência ANSI que faz com que o terminal limpe, e end no print é usado para que o print não adicione uma nova linha. 
    print("\033c", end="")

#--------------------------------------------FINAL DO CODIGO--------------------------------------------
