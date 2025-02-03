import unittest
from utils import *
from textnode import *

class TestUtils(unittest.TestCase):

    def test_split_bold_node(self):
        node = TextNode('This is a normal text with **bold text** here', TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode('This is a normal text with ', TextType.TEXT),
                TextNode('bold text', TextType.BOLD),
                TextNode(' here', TextType.TEXT),
            ],
            new_nodes
        )

    def test_multiple_old_node(self):
        node_1 = TextNode('This is **an important** note', TextType.TEXT)
        node_2 = TextNode('This also is **a very important** note', TextType.TEXT)
        new_nodes = split_nodes_delimeter([node_1, node_2], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('an important', TextType.BOLD),
                TextNode(' note', TextType.TEXT),
                TextNode('This also is ', TextType.TEXT),
                TextNode('a very important', TextType.BOLD),
                TextNode(' note', TextType.TEXT)
            ],
            new_nodes
        )

    def test_convert_two_times(self):
        node = TextNode('This contain a **bold word** and *also italic* word', TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode('This contain a ', TextType.TEXT),
                TextNode('bold word', TextType.BOLD),
                TextNode(' and *also italic* word', TextType.TEXT),
            ],
            new_nodes
        )
        removed_italic_nodes = split_nodes_delimeter(new_nodes, '*', TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode('This contain a ', TextType.TEXT),
                TextNode('bold word', TextType.BOLD),
                TextNode(' and ', TextType.TEXT),
                TextNode('also italic', TextType.ITALIC),
                TextNode(' word', TextType.TEXT)
            ],
            removed_italic_nodes
        )

    def test_contains_two_bold_word(self):
        multiple_bold_node = TextNode('This contains **one bold** and **two bold** text', TextType.TEXT)
        new_nodes = split_nodes_delimeter([multiple_bold_node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode('This contains ', TextType.TEXT),
                TextNode('one bold', TextType.BOLD),
                TextNode(' and ', TextType.TEXT),
                TextNode('two bold', TextType.BOLD),
                TextNode(' text', TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_first_part_is_code_part(self):
        node = TextNode('`var a = 1` This is a javascript code', TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], '`', TextType.CODE)
        self.assertListEqual(
            [
                TextNode('', TextType.TEXT),
                TextNode('var a = 1', TextType.CODE),
                TextNode(' This is a javascript code', TextType.TEXT)
            ],
            new_nodes
        )

    def test_extract_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        extract_list = extract_markdown_images(text)
        self.assertListEqual(
            [
                ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
                ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'),
            ],
            extract_list
        )

    def test_extract_links(self):
        text = 'This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)'
        extract_list = extract_markdown_links(text)
        self.assertListEqual(
            [
                ('to boot dev', 'https://www.boot.dev'),
                ('to youtube', 'https://www.youtube.com/@bootdotdev')
            ],
            extract_list
        )

    def test_extract_images_matches_none(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif'
        extract_list = extract_markdown_images(text)
        self.assertEqual([], extract_list)

    def test_split_nodes_image_found_none(self):
        node = TextNode('This is a node with ![rick roll] but no link to image', TextType.TEXT)
        extracted_list = split_nodes_image([node])
        self.assertEqual([node], extracted_list)

    def test_split_nodes_image_found_one(self):
        node = TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)', TextType.TEXT)
        extracted_list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode('This is text with a ', TextType.TEXT),
                TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif')
            ],
            extracted_list
        )

    def test_split_nodes_image_found_two_in_one_node(self):
        node = TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.TEXT)
        extract_list = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode('This is text with a ', TextType.TEXT),
                TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
                TextNode(' and ', TextType.TEXT),
                TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
            ],
            extract_list
        )

    def test_split_nodes_link_found_none(self):
        node = TextNode('This is text with a link [to boot dev](https://www.boot.dev', TextType.TEXT)
        extract_list = split_nodes_link([node])
        self.assertListEqual([node], extract_list)

    def test_split_nodes_link_found_one(self):
        node = TextNode('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
        extract_list = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
            ],
            extract_list
        )