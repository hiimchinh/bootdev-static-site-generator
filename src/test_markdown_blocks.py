import unittest
from markdown_blocks import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks_strip_whitespace(self):
        markdown = """hello,   

    my name is Peter, I am 26 years old    """
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                'hello,',
                'my name is Peter, I am 26 years old'
            ],
            blocks
        )
    def test_markdown_to_blocks_success(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                """* This is the first list item in a list block
* This is a list item
* This is another list item"""
            ],
            blocks
        )