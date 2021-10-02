import requests
import esprima
import sys

class MyVisitor(esprima.NodeVisitor):
    def visit_ExpressionStatement(self, node):
        global bootCount
        if hasattr(node,'expression') and type(node.expression) == esprima.nodes.AssignmentExpression :
            if hasattr(node.expression,'left'):
                if hasattr(node.expression.left,'name'):
                    if node.expression.left.name == "boot" and node.expression.operator == "+=":
                        # print(node.expression)
                        bootCount +=1
        self.generic_visit(node)

r = requests.get("https://raw.githubusercontent.com/espruino/BangleApps/master/apps/boot/bootupdate.js")
# print(r.text)

updateFile = r.text
# syntaxTree = syntaxTree.body
bootCount = 0

visitor = MyVisitor()
syntaxTree = esprima.parseScript(updateFile,delegate=visitor)
visitedTree = visitor.visit(syntaxTree)
print(visitedTree)

print(f"boot count is {bootCount}")
