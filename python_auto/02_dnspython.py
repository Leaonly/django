import dns.resolver
import dns

# A记录
#domain = input('Please input an domain: ')
A = dns.resolver.resolve('www.baidu.com', 'A')

for i in A.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            print(j)

# CNAME
cname = dns.resolver.resolve('www.baidu.com', 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print(j.to_text())
