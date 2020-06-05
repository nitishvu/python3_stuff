import re

fd = open('httpd.log','r')
log_content = fd.read()
pattern = re.compile(r'(.*[.]*[.]*[.]*) (.*.com) .*')
matches = re.finditer(pattern,log_content)
for match in matches:
    print (match.group(1))
    print (match.group(2))