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

def lines_start_with(lines, chars):
    matches = list(filter(lambda line: line.startswith(chars), lines))
    return len(matches) == len(lines)

def block_to_block_type(block):
    match_headings = re.findall(r"^#{1,6} [^\n]+$", block)
    if len(match_headings) > 0:
        return 'heading'

    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    lines = block.split('\n')
    if lines_start_with(lines, '>'):
        return 'quote'

    if lines_start_with(lines, '* ') or lines_start_with(lines, '- '):
        return 'unordered_list'
    
    is_ordered_list = True
    for i in range(len(lines)):
        start = i + 1
        if not lines[i].startswith(f"{start}. "):
            is_ordered_list = False

    if is_ordered_list:
        return 'ordered_list'
    

    return 'normal'