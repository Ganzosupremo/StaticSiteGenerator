import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_initialization(self):
        node = LeafNode(tag='div', value='Hello', attributes={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, None)
        self.assertEqual(node.attributes, {'class': 'container'})

    def test_leafnode_repr(self):
        node = LeafNode(tag='p', value='Test')
        node2 = LeafNode(tag='p', value='Test')
        self.assertEqual(repr(node), repr(node2))
    
    def test_leafnode_to_html(self):
        node = LeafNode(tag='p', value='Test')
        self.assertEqual(node.to_html(), '<p>Test</p>')
        
    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(tag=None, value='Test')
        self.assertEqual(node.to_html(), 'Test')
        
    def test_leafnode_to_html_no_value(self):
        node = LeafNode(tag='p', value=None)
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()