import requests

url = "https://www.carousell.com.hk/search/%E7%9A%87%E5%AE%B6%E7%BE%8E%E7%B4%A0%201?sort_by=time_created%2Cdescending&t-search_query_source=saved_search&tab=marketplace"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

print("Length:", len(html))
print(html[:3000])
