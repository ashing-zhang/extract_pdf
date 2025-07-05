import re

def extract_formulas(page):
    formulas = []
    text = page.extract_text() or ''
    # 简单检测行内公式 $...$ 和块公式 $$...$$
    for m in re.finditer(r'\$\$(.+?)\$\$', text, re.DOTALL):
        formulas.append({'type': 'formula_block', 'latex': m.group(1).strip()})
    for m in re.finditer(r'\$(.+?)\$', text):
        formulas.append({'type': 'formula_inline', 'latex': m.group(1).strip()})
    return formulas 