import re

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = list(
        map(
            lambda block: block.strip(),
            filter(
                lambda block: block != '',
                blocks
            )
        )
    )
    return blocks

def block_to_block_type(block):
    match_headings = re.findall(r"^#{1,6} [^\n]+$", block)
    if len(match_headings) > 0:
        return 'heading'

    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    
    return 'normal'