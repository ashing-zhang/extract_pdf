import re

def detect_headings(blocks):
    # 简单规则：大字体或正则检测序号/标题
    headings = []
    for b in blocks:
        text = b.get('text', '')
        if re.match(r'^(第[一二三四五六七八九十]+章|[0-9]+[.][0-9.]*\s+)', text):
            headings.append({'type': 'heading', 'level': 1, 'text': text})
        else:
            headings.append({'type': 'paragraph', 'text': text})
    return headings

def merge_blocks(headings, tables, formulas):
    # 简单合并，后续可优化顺序
    merged = []
    merged.extend(headings)
    merged.extend(tables)
    merged.extend(formulas)
    return merged 