from content_generation import copy_directory, generate_pages_recursive

def main():
    source_dir = 'static'
    dest_dir = 'public'
    copy_directory(source_dir, dest_dir)
    
    content_src = "content"
    template_path = 'template.html'
    dest_html = "public"
    generate_pages_recursive(content_src, template_path, dest_html)


if __name__ == "__main__":
    main()