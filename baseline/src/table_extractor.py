import pandas as pd

def extract_tables(page):
    tables = []
    for table in page.extract_tables():
        df = pd.DataFrame(table[1:], columns=table[0]) if table and len(table) > 1 else pd.DataFrame(table)
        md = df.to_markdown(index=False)
        tables.append({'type': 'table', 'markdown': md})
    return tables 