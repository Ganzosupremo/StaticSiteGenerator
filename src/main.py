from textnode import TextNode
from textnode import TextType

def main():
    node: TextNode = TextNode("Whatever", TextType.CODE, "www.uno.com")
    
    print(node)


if __name__ == "__main__":
    main()