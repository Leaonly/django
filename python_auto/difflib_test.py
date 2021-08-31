import difflib

text1 = """text1:
This module blablabla
v7.4
"""
text1_lines = text1.splitlines()
text2 = """text2:
This module blablabla
v7.5
"""

text2_lines = text2.splitlines()
d = difflib.HtmlDiff()
diff = d.make_file(text1_lines, text2_lines)
#print ('\n'.join(list(diff)))
print(diff)