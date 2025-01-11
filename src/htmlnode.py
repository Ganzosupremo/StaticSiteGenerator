class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, attributes: dict = None) -> None:
        self.tag = tag
        self.attributes = attributes
        self.children = children
        self.value = value

    def to_html(self):
        pass

    def _attributes_to_html(self):
        if self.attributes is None:
            return ""
        return " ".join([f' {key}="{value}"' for key, value in self.attributes.items()])

    def _children_to_html(self):
        return " ".join([child.to_html() for child in self.children])

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, attributes={self.attributes!r})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        super().__init__(tag, value, None, attributes)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self._attributes_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.attributes})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        super().__init__(tag, None, children, attributes)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self._attributes_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.attributes})"