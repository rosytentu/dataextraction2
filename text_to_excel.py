import re
import pandas as pd

# Provide the path to your text file
text_file_path = ""


# Read the content of the text file
with open(text_file_path, 'r') as file:
    extracted_text = file.read()

# Extract the filename from the text (e.g., "File: Feb 2022ST.pdf")
file_name_match = re.search(r'File:\s*(.+\.pdf)', extracted_text)
file_name = file_name_match.group(1) if file_name_match else "Unknown_File"

# Extract the tag number
tag_no_match = re.search(r'Tag No:\s*(\d+)', extracted_text)
tag_no = tag_no_match.group(1) if tag_no_match else None

# Regex pattern to extract date, time, and amount
pattern = re.compile(r'(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2}:\d{2})\s+\S+\s+\d+\s+(\d+\.\d{2})')

# Finding all matches for date, time, and amount
matches = pattern.findall(extracted_text)

# Creating a list of dictionaries for each match
data = [{
    "file_name": file_name,  # Use the extracted file name
    "tag_no": tag_no,
    "date": match[0],
    "time": match[1],
    "amount": match[2]
} for match in matches]

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_excel_path = "toll_data_parsed2.xlsx"
df.to_excel(output_excel_path, index=False)

print(f"Data has been saved to {output_excel_path}")
