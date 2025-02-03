from leafnode import LeafNode
from textnode import TextType, TextNode
import re


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {'href': text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
    raise TypeError('text type is not supported')

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_parts = node.text.split(delimeter)
        len_text_parts = len(text_parts)
        if len_text_parts % 2 != 1:
            raise ValueError(f'Your string has invalid markdown syntax')

        for i in range(len_text_parts):
            text = text_parts[i]
            # odd is delimeter text type
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
        
    return new_nodes



def split_nodes(old_nodes, extract_func, text_type, split_func):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matches = extract_func(node.text)
        if len(matches) == 0:
            return old_nodes
        original_text = node.text
        for match in matches:
            sections = split_func(original_text, match)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            if len(sections) == 2:
                original_text = sections[1]
            new_nodes.append(TextNode(match[0], text_type, match[1]))
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes(old_nodes, extract_markdown_images, TextType.IMAGE, split_markdown_image)

def split_nodes_link(old_nodes):
    return split_nodes(old_nodes, extract_markdown_links, TextType.LINK, split_markdown_link)

def split_markdown_image(text, match):
    return text.split(f'![{match[0]}]({match[1]})', 1)

def split_markdown_link(text, match):
    return text.split(f'[{match[0]}]({match[1]})', 1)

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches