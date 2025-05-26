import requests
from bs4 import BeautifulSoup
import pandas as pd

query = "인공지능"
url = f"https://search.naver.com/search.naver?where=news&query={query}"


headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    news_items = soup.select("span.sds-comps-text.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1")

    data = []
    for item in news_items:
        title = item.text.strip()
        data.append({"title": title})

    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # CSV 저장 (utf-8-sig 인코딩은 한글 깨짐 방지)
    df.to_csv("naver_news.csv", index=False, encoding="utf-8-sig")

    print("CSV 파일이 naver_news.csv 이름으로 저장되었습니다.")
else:
    print("네이버 요청 실패:", res.status_code)
