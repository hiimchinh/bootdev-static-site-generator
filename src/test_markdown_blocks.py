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

    
    def test_heading_block_success(self):
        text = '###### This is a heading'
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, 'heading')

    def test_heading_block_wrong_syntax(self):
        text = '###this try to be heading'
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, 'normal')

    def test_heading_block_with_new_line_is_normal(self):
        text = '# this try to have new line stuff \n okay'
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, 'normal')

    def test_heading_block_extra_line(self):
        text = '''### This is a heading
and this extra line'''
        self.assertEqual(block_to_block_type(text), 'normal')

    def test_code_block_is_correct(self):
        test_cases = [
            '```var name = "Chinh HM"```',
            """```const iframe = document.getElementById("iframe")

console.log('iframe is', iframe)```"""

        ]
        for case in test_cases:
            self.assertEqual(block_to_block_type(case), 'code')
        

    def test_quote_block_correct(self):
        test_cases = [
            """>This is a quote
> and another quote"""
        ]
        for case in test_cases:
            self.assertEqual(block_to_block_type(case), 'quote')

    def test_incorrect_quote_block(self):
        fail_cases = [
            """> This is first line
            the second line does not start with >""",
            """ > Missing one first line
> second is correct
>third is also correct"""
        ]
        for case in fail_cases:
            self.assertEqual(block_to_block_type(case), 'normal')

    def test_correct_unordered_list(self):
        correct_cases = [
            """* First to do list
* Second todo, go to the mall or something
* Third one, you should also check this""",
"""- item 1
- item 2
- item 3"""
        ]
        for case in correct_cases:
            self.assertEqual(block_to_block_type(case), 'unordered_list')

    def test_incorrect_unordered_list(self):
        incorrect_cases  = [
            """* First line correct
*Second line missing space
* Third line is correct"""
        ]
        for case in incorrect_cases:
            self.assertEqual(block_to_block_type(case), 'normal')

    def test_correct_ordered_list(self):
        correct_cases = [
            """1. First item
2. Second item on the list
3. here's another one"""
        ]
        for case in correct_cases:
            self.assertEqual(block_to_block_type(case), 'ordered_list')

    def test_incorrect_ordered_list(self):
        incorrect_cases = [
            """1. First item is correct
2.Second one is missing a space
3. Third one is correct""",
            """1 item 1 missing colon
2. item two correct
3. there is also correct"""
        ]
        for case in incorrect_cases:
            self.assertEqual(block_to_block_type(case), 'normal')