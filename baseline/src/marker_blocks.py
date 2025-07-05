'''
    Each document consists of one or more pages. Pages contain blocks, which can themselves contain other blocks. It's possible to programmatically manipulate these blocks.
    Here's an example of extracting all forms from a document
'''
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.schema import BlockTypes

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
document = converter.build_document("FILEPATH")
forms = document.contained_blocks((BlockTypes.Form,))