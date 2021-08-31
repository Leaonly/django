import dns.resolver
import requests

# ddns = 'www.baidu.com'
# A = dns.resolver.query(ddns, 'A')
# for i in A.response.answer:
#     for j in i.items:
#         print(j.address)


r = requests.get('http://www.baidu.com')
print(r.status_code)
print(r.encoding)
r.encoding='utf-8'
print(r.text)