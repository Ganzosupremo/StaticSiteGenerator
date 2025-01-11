import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_initialization(self):
        node = HTMLNode(tag='div', value='Hello', children=[], attributes={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, [])
        self.assertEqual(node.attributes, {'class': 'container'})

    def test_htmlnode_repr(self):
        node = HTMLNode(tag='p', value='Test')
        node2 = HTMLNode(tag='p', value='Test')
        self.assertEqual(repr(node), repr(node2))
  
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parentnode_no_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("p", "Hello")]).to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_parentnode_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_parentnode_single_child(self):
        parent = ParentNode("div", [LeafNode("p", "Hello")])
        self.assertEqual(parent.to_html(), '<div><p>Hello</p></div>')

    def test_parentnode_multiple_children(self):
        parent = ParentNode("div", [LeafNode("p", "Hello"), LeafNode("span", "World")])
        self.assertEqual(parent.to_html(), '<div><p>Hello</p><span>World</span></div>')

    def test_parentnode_nested_children(self):
        child = ParentNode("div", [LeafNode("p", "Nested")])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><div><p>Nested</p></div></div>')

    def test_parentnode_with_attributes(self):
        parent = ParentNode("div", [LeafNode("p", "Hello")], attributes={'class': 'container'})
        self.assertEqual(parent.to_html(), '<div class="container"><p>Hello</p></div>')

if __name__ == "__main__":
    unittest.main()