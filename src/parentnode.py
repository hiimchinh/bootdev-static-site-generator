from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode tag cannot be None')
        if self.children is None:
            raise ValueError('ParentNode children cannot be None')
        child_tag = ''
        for child in self.children:
            child_tag += child.to_html()    
        return f"<{self.tag}{self.props_to_html()}>{child_tag}</{self.tag}>"