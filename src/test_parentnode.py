import unittest
from parentnode import ParentNode
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_empty_tag_parent(self):
        node = ParentNode(
            None,
            [
                TextNode('this is a text node', TextType.BOLD)
            ]
        )
        self.assertRaises(TypeError)

    def test_has_child(self):
        node = ParentNode(
            'td',
            [
                LeafNode('p', 'This is a test')
            ]
        )
        self.assertEqual(node.to_html(), '<td><p>This is a test</p></td>')