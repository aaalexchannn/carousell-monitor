import requests

url = "https://www.pns.hk/zh-hk/幫寶適一級幫拉拉褲大碼箱裝144片/p/BP_824705"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text

print("Length:", len(html))
print(html[:5000])
