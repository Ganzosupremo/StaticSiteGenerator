from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            new_nodes.extend([TextNode(text, text_type) for text in node.text.split(delimiter)])
        else:
            new_nodes.append(node)
    return new_nodes
    