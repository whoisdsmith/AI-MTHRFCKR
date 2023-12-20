import pandas as pd
import os

# Function to convert each row of the dataframe into the specified markdown format
def convert_to_markdown(row):
    markdown_block = ""

    # Checking and adding each field if it exists
    if 'boldtitle' in row and pd.notna(row['boldtitle']):
        markdown_block += f"{row['boldtitle']}\n\n"
    if 'cover' in row and pd.notna(row['cover']):
        markdown_block += f"![]({row['cover']})\n\n"
    if 'title' in row and 'url' in row and pd.notna(row['title']) and pd.notna(row['url']):
        markdown_block += f"[{row['title']}]({row['url']})"
    if 'excerpt' in row and pd.notna(row['excerpt']):
        markdown_block += f" - {row['excerpt']}\n\n"
    if 'created' in row and pd.notna(row['created']):
        markdown_block += f"**Date:** {row['created']}\n"
    if 'tags' in row and pd.notna(row['tags']):
        markdown_block += f"**Tags:** {row['tags']}\n"

    markdown_block += "\n---\n"
    return markdown_block

def convert_csv_to_markdown(csv_file_path, output_markdown_path):
    try:
        # Load the CSV file
        bookmarks_df = pd.read_csv(csv_file_path)

        # Apply the function to each row
        markdown_content = bookmarks_df.apply(convert_to_markdown, axis=1).str.cat()

        # Save the markdown content to a file with UTF-8 encoding
        with open(output_markdown_path, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
    except Exception as e:
        print(f"Error processing file {csv_file_path}: {e}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(directory, filename)
            output_markdown_path = os.path.splitext(csv_file_path)[0] + '.md'
            convert_csv_to_markdown(csv_file_path, output_markdown_path)
            print(f"Converted {filename} to Markdown")

# Directory containing the CSV files
directory = r'C:\Users\whois\Documents\GITHUB\AI-MTHRFCKR\CSVs'
process_directory(directory)
