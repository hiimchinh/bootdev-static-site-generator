import unittest

from leafnode import *
from textnode import *
from utils import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode('This is a bold text node', TextType.BOLD)
        node2 = TextNode('This is a bold text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode('This is a text node', TextType.TEXT)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode('This is a text node', TextType.TEXT)
        node2 = TextNode('This is a different text node', TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode('This is a text node with no url', TextType.TEXT)
        self.assertIsNone(node.url)

    def test_normal_text_type_to_html(self):
        text = 'This is a normal text'
        node = TextNode(text, TextType.TEXT)
        htmlNode = LeafNode(None, text)
        self.assertEqual(htmlNode.to_html(), text_node_to_html_node(node).to_html())

    def test_bold_node(self):
        text = 'This is a bold node'
        bold_node = LeafNode('b', text)
        node = TextNode(text, TextType.BOLD)
        self.assertEqual(bold_node.to_html(), text_node_to_html_node(node).to_html())

    def test_italic_node(self):
        text = 'This is an italic node text'
        text_node = TextNode(text, TextType.ITALIC)
        italic_node = LeafNode('i', text)
        self.assertEqual(italic_node.to_html(), text_node_to_html_node(text_node).to_html())

    def test_a_tag(self):
        anchor_text = 'This is a link'
        href = 'https://google.com'
        a_node = LeafNode('a', anchor_text, {'href': href})
        text_node = TextNode(anchor_text, TextType.LINK, href)
        self.assertEqual(a_node.to_html(), text_node_to_html_node(text_node).to_html())

    def test_img_tag(self):
        src = 'https://www.gardensillustrated.com/plants/pink-flowers'
        alt = 'Flower'
        img_node = LeafNode('img', '', {'src': src, 'alt': alt})
        text_node = TextNode(alt, TextType.IMAGE, src)
        self.assertEqual(img_node.to_html(), text_node_to_html_node(text_node).to_html())
        

if __name__ == "__main__":
    unittest.main()
