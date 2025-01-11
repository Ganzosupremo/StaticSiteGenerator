import os
import shutil
from markdown_blocks import markdown_to_html_node

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {dst_path}")

def extract_title(markdown: str) -> str:
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No h1 header found")

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, 'r') as file:
        markdown_content = file.read()

    # Read the template file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    full_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the full HTML to the destination file
    with open(dest_path, 'w') as file:
        file.write(full_html)


def main():
    source_dir = 'static'
    dest_dir = 'public'
    copy_directory(source_dir, dest_dir)
    
    index_src = 'content/index.md'
    template_path = 'template.html'
    dest_html = 'public/index.html'
    generate_page(index_src, template_path, dest_html)


if __name__ == "__main__":
    main()