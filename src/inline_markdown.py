from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_nodes = []
        section = node.text.split(delimiter)
        if len(section) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(section[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text:str) -> list:
    pattern = r"!\[([^\]]*)\]\(([^)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text:str) -> list:
    pattern = r"\[([^\]]*)\]\(([^)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        split_nodes = []
        start = 0
        
        for alt_text, url in images:
            start_idx = node.text.find(f"![{alt_text}]({url})", start)
            if start_idx != -1:
                split_nodes.append(TextNode(node.text[start:start_idx], TextType.NORMAL))
                split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                start = start_idx + len(f"![{alt_text}]({url})")
        split_nodes.append(TextNode(node.text[start:], TextType.NORMAL))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        split_nodes = []
        start = 0
        
        for link_text, url in links:
            start_idx = node.text.find(f"[{link_text}]({url})", start)
            if start_idx != -1:
                split_nodes.append(TextNode(node.text[start:start_idx], TextType.NORMAL))
                split_nodes.append(TextNode(link_text, TextType.LINK, url))
                start = start_idx + len(f"[{link_text}]({url})")
        split_nodes.append(TextNode(node.text[start:], TextType.NORMAL))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_text_nodes(text: str) -> list:
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes