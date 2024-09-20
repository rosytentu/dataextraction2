import pdfplumber
import os

input_folder = ""
output_file = ""

with open(output_file, 'w', encoding='utf-8') as f:
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(input_folder, filename)
            f.write(f"File: {filename}\n")
            with pdfplumber.open(pdf_file) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    for table_num, table in enumerate(tables):
                        f.write(f"Page {page_num+1}, Table {table_num+1}\n")
                        for row in table:
                            # Replace None values with empty strings
                            row = [cell if cell is not None else "" for cell in row]
                            f.write("\t".join(row) + "\n")
                        f.write("\n\n")
            f.write("\n")

