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