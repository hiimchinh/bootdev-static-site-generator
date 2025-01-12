import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('p', 'This is a p tag', None, {
            'href': 'https://example.com',
            'target': '_blank'
        })
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank" ')

    def test_eq(self):
        node = HTMLNode('p', 'This is a p tag')
        self.assertEqual('This is a p tag', node.value)

    def test_empty_children(self):
        node = HTMLNode(
            'div',
            'This is a div with no children'
        )
        self.assertIsNone(node.children)

    def test_to_string(self):
        node = HTMLNode(
            'div',
            'Content',
            None,
            {
                'class': 'text-center',
                'onclick': 'alert("Hello World")'
            }
        )
        self.assertEqual(node.__repr__(), "HTMLNode(tag: div, value: Content, children: None, props: {'class': 'text-center', 'onclick': 'alert(\"Hello World\")'})")