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

    def test_parent_inside_parent(self):
        child = ParentNode(
            'th',
            [
                LeafNode('p', 'row 1'),
                LeafNode('p', 'row 2')
            ]
        )
        parent = ParentNode(
            'td',
            [child]
        )
        self.assertEqual(parent.to_html(), '<td><th><p>row 1</p><p>row 2</p></th></td>')

    def test_empty_children(self):
        node = ParentNode(
            'table',
            []
        )
        self.assertRaises(ValueError)