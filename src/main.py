from textnode import *
from utils import split_nodes_delimeter



def main():
    bold_node = TextNode('bold right `code here`?', TextType.BOLD, 'https://url.com')
    new_nodes = split_nodes_delimeter([bold_node], '`', TextType.CODE)
    print(new_nodes)
    

main()