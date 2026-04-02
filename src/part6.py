#Tokenzation
import tokenize
import io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)
    

print()
print()

#AST - Abstract Syntax Tree
import ast
tree = ast.parse("x = 10")
print(ast.dump(tree, indent=2))


# dis Module
import dis
dis.dis("x = 10")