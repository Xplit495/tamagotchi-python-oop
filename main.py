from utils.argument_parser import argument_parser
from utils.load_save_file import load_save_file

if __name__ == '__main__':
    save_file = argument_parser()
    if save_file:
        load_save_file(save_file)
    else:
        ...