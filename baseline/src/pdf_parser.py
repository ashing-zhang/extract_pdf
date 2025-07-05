
from pathlib import Path
from typing import Dict, List
import pdfplumber
from .utils import detect_headings, merge_blocks
from .table_extractor import extract_tables
from .formula_extractor import extract_formulas

def parse_pdf(pdf_path: Path) -> Dict[str, List[Dict]]:
    """Parse PDF using marker-pdf to extract structured content.
    
    Args:
        pdf_path: Path to PDF file
    Returns:
        Dictionary containing structured document blocks
        Example: {'blocks': [{'type': 'text', 'text': '...'}, ...]}
    """
    doc_struct = {'blocks': []}
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            # 1. 提取文本块
            blocks = page.extract_words(x_tolerance=2, y_tolerance=2, keep_blank_chars=False, use_text_flow=True)
            # 先保留所有原始文本块
            for b in blocks:
                doc_struct['blocks'].append({'type': 'paragraph', 'text': b.get('text', '')})
            # 2. 标题检测
            heading_blocks = detect_headings(blocks)
            # 3. 表格提取
            tables = extract_tables(page)
            # 4. 公式提取
            formulas = extract_formulas(page)
            # 5. 合并所有结构块
            merged = merge_blocks(heading_blocks, tables, formulas)
            doc_struct['blocks'].extend(merged)
    return doc_struct
