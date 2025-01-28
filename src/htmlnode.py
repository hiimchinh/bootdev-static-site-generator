class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        str = ''
        if self.props:
            for key in self.props:
                value = self.props[key]
                str += f' {key}="{value}"'
        return str
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"