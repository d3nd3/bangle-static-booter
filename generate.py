import requests
import esprima
import sys

def diveIntoTreeClass(branch):
    global bootCount
    for obj in branch:
        if type(obj) == esprima.nodes.ExpressionStatement:
            if hasattr(obj,'expression'):
                if hasattr(obj.expression,'left'):
                    if hasattr(obj.expression.left,'name'):
                        if obj.expression.left.name == "boot":
                            print("found a boot!!")
                            bootCount +=1
                            break
                

def diveIntoTreeBodyList(branch):
    # initially a list
    for obj in syntaxTree:
        if type(obj) == esprima.nodes.BlockStatement:
            diveIntoTreeBodyList(obj.body)
        else:
            diveIntoTreeClass(branch)


r = requests.get("https://raw.githubusercontent.com/espruino/BangleApps/master/apps/boot/bootupdate.js")
# print(r.text)

updateFile = r.text

syntaxTree = esprima.parseScript(updateFile)

syntaxTree = syntaxTree.body
bootCount = 0

diveIntoTreeBodyList(syntaxTree)

print(f"boot count is {bootCount}")
