#!bin/env/python3

from LIBS.manager import end_app_execution
from LIBS.ijdev_helper import special_chars
import math


# --------------------------------------------------

# CHALLENGE 1 : BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO
def bracket_balancing(exp: str) -> None:
    """#### BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO
        Data uma string de expressao exp, escreva um programa para examinar se os pares e as ordens de "{" , "}", "(", ")", "[", "]" estao corretos na expressao dada .

    #### Exemplos de entradas: 
        - 2*(3+4+5*[2+3)] --> ERRADO  
        - 2*(3+4+5*[2+3]) --> CORRETO
        - [2*(3+4+5*[2+3]/(2+(3+(7+5)*9)*6)*[5+8]+17)+2] --> CORRETO
       
    #### SOLUCAO: 
        Estrutura de dados: uso de pilhas
        
        1 - empilhar caracteres de abertura
         
        2 - ao identificar caractere de fechamento:
        
            --> desempilhar e verificar se coincide com abertura 
          
        3 - ao final a pilha deve estar vazia 
    Args:
        exp (str): entering expression
    """
    
    print(" BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO")
    OPEN_CHARACTERS = ("(", "[", "{")
    CLOSE_CHARACTERS = (")", "]", "}")
    
    pill_array = list()
    
    
    # for c in exp:
    #     if c in OPEN_CHARACTERS:
    #         pill_array.append(c)
    
    return

    
def revert_first_k_elements(k: int, elements: list[int]) -> None:
    """### Revert firt k elements
    
    Dado um inteiro k e uma fila de inteiros, a tarefa é inverter a ordem dos primeiros k elemetos da fila, deixand os demais elementos na mesma ordem relativa .

    #### Exemplos:
        -  [1, 2, 3, 4, 5] -> k=2 --> [2, 1, 3, 4, 5] 
        -  [1, 2, 3, 4, 5] -> k=4 --> [4, 3, 2, 1, 5] 

    Args:
        k (int): quantity of first elements of list to shift
        elements (list[int]): list of real elements
    """
    
    keep_index_elem = elements[k:]
    current_lenght = len(elements) - k
    result_list = list()
    
    for i in range(current_lenght + 1, len(elements) + 1):
        result_list.append(elements[-i])

    result_list.extend(keep_index_elem)
    
    print(f"\n K: {k}\n ELEMENTS: {elements}\n THE FINAL RESULT IS:  {result_list}")
    
    print("\n\n")    
    return


# CHALLENGE 3 - Maior valor em cada nível de uma arvore binária
def greatest_value_in_each_tree_level(tree_elements: list[list]) -> list[int]:
    """### Maior valor em cada nível de uma arvore binária

    Args:
        tree_elements (list[list]): real values of the binary tree 

    Returns:
        list[int]: a list of greatest value of each level 
    """
    
    result = []
    for level_values in tree_elements:
        level_values.sort()
        result.append(level_values[-1])
    
    return result


# CHALLENGE 3 - Maior valor em cada nível de uma arvore binária
def binary_tree_properties(tree_elements: list[list], tree_hight: int) -> list[int]:
    
    # 1 - altura arvore N + 1
    # 2 - elements by leVel
    # 3 - 2**N
    # 4 - total elemetos: (2**N+1) - 1

    elements_by_level = dict()
    total_elements = math.pow(2, tree_hight) - 1
    
    for N in range(tree_hight):
        elements_by_level[f'level_{N + 1}'] = f"{int(math.pow(2, N))} elements"
    
    greatest_result = []
    for level_values in tree_elements:
        level_values.sort()
        greatest_result.append(level_values[-1])
    
        
    final_result = [total_elements, elements_by_level, greatest_result]
    
    return final_result 


def run_bracket_balancing():
    return


def run_revert_first_k_elements_v2():
    k = int(input("ENTER THE number (k) of elements to swap out in ARRAY :>> ").strip())

    elements = list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split()))
    revert_first_k_elements(k, elements)


def run_revert_first_k_elements():
    
    revert_first_k_elements(
        k=2, elements=[1, 2, 3, 4, 5]) # [2, 1, 3, 4, 5]
    
    revert_first_k_elements(
        k=7, elements=[1,8,9,3,66,77,0,9,7,2,13,4,58]) # [0,77,66,3,9,8,1,9,7,2,13,4,58]
    
    revert_first_k_elements(
        k=4, elements=[1, 2, 3, 4, 5, 6, 7, 8]) # [4,3,2,1,5,6,7,8]


# Mostra propriedades de uma arvora binaria perfeita
def run_binary_tree_properties():
    print("\n\n\n ENTER THE HIGHT OF YOUR PERFECT BINARY TREE  \n\n")
    
    tree_hight = int(input("ENTER A VALUE HERE :::>  ").strip())
    btree = []
    
    for N in range(tree_hight):
        print(f"\n ------- VALUES FOR LEVEL {N} --------\n")
        btree.append(list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split())))

    print(btree)
    result = binary_tree_properties(tree_elements=btree, tree_hight=tree_hight)
    
    print(f"\n\n THE RESULT IS >>>>>>  {result}")  
    print("\n\n RESULT DETAIL \n\n")
    print(f"\t HIGHT OF TREE: {tree_hight}")
    print(f"\t TREE LEVEL: GOES FROM 0 to {tree_hight-1}")
    print(f"\t TOTAL ELEMENTS: {int(result.pop(0))}")
    print(f"\t TOTAL ELEMENTS BY LEVEL: {result.pop(0)}")
    
    for n, g in enumerate(result.pop(0)):
        print(f"\t LEVEL {n}  |  GREATEST {g}")
        
    return
 
def run_greatest_value_in_each_tree_level():
    print("\n\n\n ENTER THE HIGHT OF YOUR BINARY TREE  \n\n")
    
    tree_hight = int(input("ENTER A VALUE HERE :::>  ").strip())
    btree = []
    
    for N in range(tree_hight):
        print(f"\n ------- VALUES FOR LEVEL {N} --------\n")
        btree.append(list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split())))

    print(btree)
    result = greatest_value_in_each_tree_level(tree_elements=btree)
    
    print(f" \n\n THE RESULT IS >>>>>>  {result}")  
    print("\n\n RESULT DETAIL \n\n")
    for n, g in enumerate(result):
        print(f"LEVEL {n}  |  GREATEST {g}")
        
    return

def run_verifica_senha():
    
    # pwd = "senhateste#57@9"  # [2, 3]
    pwd_in = input("ENTER THE PASSWORD ::>>  ").strip()  
    print("[qtd caracteres especiais, qtd numeros]") 
    print(verifica_senha(pwd_in)) 
    
    return
    

# CHALLENGE 4 - Verifica caracteres especiais e números presentes em senha
def verifica_senha(senha: str) -> list[int]:
    """### Verifica caracteres especiais e números presentes em senha
    
    Ao desenvolver um produto de segurança de senha em uma empresa, criou-se uma regra que as senhas devem possuir números e caracteres especiais. Após um ataque cibernético, decidiram fazer um estudo para verificar se aumentar a segurança da senha, de forma que existisse mais de um número e caracter especial seria efetivo para aumentar a segurança. Pensando nisso, implemente uma função que realize a contagem de quantos caracteres especiais e números existem na senha.

    Utilize o corpo de função definido abaixo e retorne uma lista de dois elementos, em que o primeiro elemento é a quantidade de caracteres especiais e o seguindo elemento é a quantidade de números existentes na senha.

    def verifica_senha(string senha):

    Args:
        senha (str): real password string

    Returns:
        list[int]: a list of quantity of special chars and numbers
    """
    
    result = []
    special_char_count = 0
    numeric_count = 0
    
    for c in senha:
        if str(c).isnumeric():
            numeric_count += 1
        elif c in special_chars:
            special_char_count += 1
    
    result.append(special_char_count)
    result.append(numeric_count)
    
    return result


def run_ada_challenges():
    menu_options = [
        "BALANCEAMENTO DE COLCHETES EM UMA EXPRESSÃO MATEMETICA",
        "Revertendo os primeiros k elementos de uma fila",
        "maior valor de cada nivel de uma arvore binaria",
        "verificar senha",
        "propriedades de uma arvore binaria perfeita"
    ]
    print("\n\n")
    print(f"------------ MENU OF OPTIOS ------------\n")
    for i, op in enumerate(menu_options, start=1):
        print(f"{i} -> {op.upper()}")
    print(f"0 -> SAIR")
    print()
    
    while True:
        try:
            option = int(input("ENTER YOUR CHOICE ::>>  "))
        except Exception as exc:
            print("INVALID OPTION ... ")
        else:
            if option <= len(menu_options):
                break
            else:
                print("\n INVALID OPTION ... \n")
                
    match option:
        case 1:
            run_bracket_balancing()
        case 2:
            run_revert_first_k_elements_v2()
        case 3:
            run_greatest_value_in_each_tree_level()
        case 4:
            run_verifica_senha()
        case 5:
            run_binary_tree_properties()
        case 0:
            end_app_execution()
    
    return run_ada_challenges()

