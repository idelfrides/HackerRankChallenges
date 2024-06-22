#!bin/env/python3

from LIBS.manager import end_app_execution


# CHALLENGE 1 : BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO
# Data uma string de expressao exp, escreva um programa para examinar se os pares e as ordens de "{" , "}", "(", ")", "[", "]" estao corretos na expressao dada .

# Exemplos de entradas: 
#  2*(3+4+5*[2+3)] --> ERRADO  |  2*(3+4+5*[2+3]) --> CORRETO
#  [2*(3+4+5*[2+3]/(2+(3+(7+5)*9)*6)*[5+8]+17)+2] --> CORRETO

# SOLUCAO: uso de pilhas
# 1 - empilhar caracteres de abertura 
# 2 - ao identificar caractere de fechamento:
    # * desempilhar e verificar se coincide com abertura 
# 3 - ao final a pilha deve estar vazia 

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
    
    print(' BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO')
    OPEN_CHARACTERS = ('(', '[', '{')
    CLOSE_CHARACTERS = (')', ']', '}')
    
    pill_array = list()
    
    
    # for c in exp:
    #     if c in OPEN_CHARACTERS:
    #         pill_array.append(c)
    
    
    return


# -------------------------------------------------------------------------------

#  CHALLENGE 2 -  Revertendo os primeiros k elementos de uma fila

# Dado um inteiro k e uma fila de inteiros, a tarefa é inverter a ordem dos primeiros k elemetos da fila, deixand os demais elementos na mesma ordem relativa .

# Exemplos:
    #  [1, 2, 3, 4, 5] -> k=2 --> [2, 1, 3, 4, 5] 
    #  [1, 2, 3, 4, 5] -> k=4 --> [4, 3, 2, 1, 5] 
    
def revert_first_k_elements(k: int, elements: list[int]) -> None:
    keep_index_elem = elements[k:]
    current_lenght = len(elements) - k
    result_list = list()
    
    for i in range(current_lenght + 1, len(elements) + 1):
        result_list.append(elements[-i])

    result_list.extend(keep_index_elem)
    
    print(f"\n K: {k}\n ELEMENTS: {elements}\n THE FINAL RESULT IS:  {result_list}")
    
    print('\n\n')    
    return


def greatest_value_in_each_tree_level(tree_elements: list[list]):
    result = []
    for level_values in tree_elements:
        level_values.sort()
        result.append(level_values[-1])
    
    return result


def run_bracket_balancing():
    return



def run_revert_first_k_elements_v2():
    k = int(input("ENTER THE numer (k) of elemnts to switch up in ARRAY ::>  ").strip())

    elements = list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split()))
    revert_first_k_elements(k, elements)


def run_revert_first_k_elements():
    
    revert_first_k_elements(
        k=2, elements=[1, 2, 3, 4, 5]) # [2, 1, 3, 4, 5]
    
    revert_first_k_elements(
        k=7, elements=[1,8,9,3,66,77,0,9,7,2,13,4,58]) # [0,77,66,3,9,8,1,9,7,2,13,4,58]
    
    revert_first_k_elements(
        k=4, elements=[1, 2, 3, 4, 5, 6, 7, 8]) # [4,3,2,1,5,6,7,8]

    
def run_greatest_value_in_each_tree_level():
    print('\n\n\n ENTER THE HIGHT OF YOUR BINARY TREE  \n\n')
    
    tree_hight = int(input("ENTER A VALUE HERE :::>  ").strip())
    btree = []
    
    for N in range(tree_hight):
        print(f'\n ------- VALUES FOR LEVEL {N} --------\n')
        btree.append(list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split())))

    print(btree)
    result = greatest_value_in_each_tree_level(btree)
    
    print(f' \n\n THE RESULT IS >>>>>>  {result}')  
    print('\n\n RESULT DETAIL \n\n')
    for n, g in enumerate(result):
        print(f'LEVEL {n}  |  GREATEST {g}')
        
    return


def run_ada_challenges():
    menu_options = [
        'BALANCEAMNTO DE COLCHETES EM UMA EXPRESSÃO',
        'Revertendo os primeiros k elementos de uma fila',
        'maior valor de cada nivel de uma arvore binaria'
    ]
    print('\n\n')
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
        case 0:
            end_app_execution()
    
    return run_ada_challenges()

