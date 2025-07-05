from pathlib import Path
from typing import List, Dict
import logging
import pandas as pd
from tqdm import tqdm
from .pdf_parser import parse_pdf
from .markdown_writer import to_markdown


def process_pdfs(pdf_dir: Path, output_csv: Path) -> None:
    """Process all PDF files in directory and save structured data to CSV.
    
    For each PDF file:
    1. Parses the document structure
    2. Converts to markdown format
    3. Saves markdown output
    4. Collects results for CSV export
    
    Args:
        pdf_dir: Path to directory containing PDF files
        output_csv: Path where results CSV will be saved
    """
    # Create output directories if they don't exist
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    md_dir = output_csv.parent / 'md_output' 
    md_dir.mkdir(exist_ok=True)
    
    results: List[Dict[str, str]] = []
    
    # Process each PDF with progress bar
    pdf_files = list(pdf_dir.glob('*.pdf'))
    for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
        try:
            doc_struct = parse_pdf(pdf_file)
            md_content = to_markdown(doc_struct)
            
            # Save markdown output
            md_path = md_dir / f"{pdf_file.stem}.md"
            md_path.write_text(md_content, encoding='utf-8')
            
            results.append({
                'file_id': pdf_file.stem,
                'answer': md_content
            })
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {str(e)}")
            continue
    
    # Export results to CSV
    pd.DataFrame(results).to_csv(output_csv, index=False)
    print(f"Successfully processed {len(results)}/{len(pdf_files)} PDFs")
    print(f"Results saved to: {output_csv.absolute()}")


def main() -> None:
    """Main entry point for PDF processing script.
    
    Configures:
    - Input PDF directory path
    - Output CSV path
    - Logging configuration
    
    Then initiates the PDF processing pipeline.
    """
    pdf_dir = Path('../pdfs/dataset_A')
    output_dir = Path('results')
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    output_csv = output_dir / 'result.csv'
    
    # Configure logging
    log_file = output_dir / 'processing.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    process_pdfs(pdf_dir, output_csv)


if __name__ == '__main__':
    main()
