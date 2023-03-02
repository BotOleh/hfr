#import urllib.request
#opener = urllib.request.build_opener()
#response = opener.open ("https://httpbin.org/get")
#print(response.read())

# import urllib.request
# import requests
# opener = urllib.request.build_opener()
# response = opener.open ("https://httpbin.org/")
# print(response.read())
# response = requests.get("https://httpbin.org/")
# print(response.content)

import requests
res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
#print(response.text)
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        # print(parse_elem_1)
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

bitcoin_exchange_rate = res_parse_list[0]
print(bitcoin_exchange_rate)