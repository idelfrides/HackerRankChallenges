import os

def order_string(string_content: str, order: str = 'asc'):
    if order.lower() == 'asc':
        return sorted(string_content)    
    if order.lower() == 'desc':
        return sorted(string_content, reverse=True)
    
    
def verify_column_letters(col_letters: str):
    col_letters_sorted_list = sorted(col_letters)
    col_letters_sorted = ''.join(col_letters_sorted_list)
    return col_letters_sorted


def end_app_execution():
    print("#" * 50)
    print("\n YOU CHOOSE TO END UP THE APP. \n\n SEE YOU LATER!\n")
    print("#" * 50)
    print("\n\n\n")
           
    exit(0)
    
def get_stage_location():
    root_ = os.path.dirname(os.path.abspath(__name__))
    stage_dir = root_ + '/STAGE'
    return stage_dir


def build_file_full_path(filename: str):
    file_full_path = '/'.join([get_stage_location(), filename])
    return file_full_path

def read_files(file_fullpath: str, op_mode: str):
    with open(file=file_fullpath, mode=op_mode) as file_:
        data = file_.read()
            
    return data


def some_personal_verifications():
    # cwd = os.getcwd()    
    cwd = os.getcwd()
    root_ = os.path.dirname(os.path.abspath(__name__))
    print(f'CWD --> {cwd}')
    print(f'ROOT --> {root_}')
    # stage_dir = root_ + '/STAGE'
    # return stage_dir
