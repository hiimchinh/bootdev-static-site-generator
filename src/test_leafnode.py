import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_raise_err(self):
        node = LeafNode('p', None)

        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(None, 'this has no tag. It returns as is')
        self.assertEqual(node.to_html(), 'this has no tag. It returns as is')

    def test_eq_to_html(self):
        node = LeafNode(
            'p',
            'This leads to something',
            {
                'onclick': "alert('wassup')",
                'class': 'text-right'
            }
        )
        self.assertEqual(node.to_html(), '<p onclick="alert(\'wassup\')" class="text-right">This leads to something</p>')