def to_markdown(doc_struct):
    md_lines = []
    for block in doc_struct['blocks']:
        if block['type'] == 'heading':
            md_lines.append('#' * block['level'] + ' ' + block['text'])
        elif block['type'] == 'paragraph':
            md_lines.append(block['text'])
        elif block['type'] == 'table':
            md_lines.append(block['markdown'])
        elif block['type'] == 'formula_inline':
            md_lines.append(f"${block['latex']}$")
        elif block['type'] == 'formula_block':
            md_lines.append(f"$$\n{block['latex']}\n$$")
    return '\n\n'.join(md_lines) 