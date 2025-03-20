a = '</title>'
b = '</html>'
c = '<head>'
d = '</body>'
e = '<html>'
f = '</head>'
g = '<title>'
h = '<body>'

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

# ✅ ↓ start coding below here ↓ ✅
# etiqueta titulo
title = g + a
# etiqueta head
header = c + title + f
# etiqueta body
body = h + d
# etiqueta html completo
html_document = e + header + body + b
print(html_document)