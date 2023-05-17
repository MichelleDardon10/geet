'''
[Module] Init command utils.
'''
import os
#import utils.data_structures
#from utils.data_structures.linked_list import Node, LinkedList
#from data_structures.linked_list import Node, LinkedList
#import sys
#current_dir = os.path.dirname(os.path.abspath(__file__))
#parent_dir = os.path.dirname(os.path.dirname(current_dir))
#sys.path.append(parent_dir)

from utils.data_structures import linked_list


def write_file(name: str, lines: list) -> None:

    with open(name, 'w') as writer:
        writer.write('\n'.join(lines))


def get_init_files() -> dict:

    initial_files = {
        '.geet/.geetignore': [".DS_Store\n"],
        '.geet/.hashdict.json': ["{\"README.md\": \"1ea4b01b49eae1fd044238ae5423222eac5495ce\"}\n"],
        'README.md': ["### Geet", "Fresh geet repository.\n"]
    }

    return initial_files


def file_exists(path: str, name: str) -> bool:

    return os.path.exists(path + name)


def create_branch(path: str) -> object:

    '''
    TODO no. 1: Linked List branch

    => We'll use a Linked List to represent the master branch. Each commit will be a node in the LL.

        - In geet/utils/data_structures/linked_list.py you'll find the boilerplate for a linked list class. Based on those docstrings, implement a linked list.

        - Once your data structure is ready, create an empty instance and make it the return of this method.

        Cada nodo de la LL es un commit

    ⬇ Your code starts here:
    '''
    instance = linked_list.LinkedList()

    return instance

    '''
    ⬆ Your code ends here.
    '''

'''
Testing area
'''

nuevo_nodo = linked_list.Node("H16", "ESO MAMONA")
nueva_lista = linked_list.LinkedList()

nueva_lista.insert_at_beginning(nuevo_nodo)

print(nueva_lista)


