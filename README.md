# 📰 Naver 뉴스 크롤러 (Python)

인공지능 관련 네이버 뉴스를 검색하여 뉴스 제목을 수집하고 CSV 파일로 저장하는 간단한 파이썬 크롤러입니다.

## 📌 주요 기능

- 네이버 뉴스에서 특정 키워드 검색 (`인공지능`)
- 뉴스 제목 추출
- CSV 파일(`naver_news.csv`)로 저장

---

## 🔧 사용 기술

- Python 3.x
- `requests` - 웹 페이지 요청
- `BeautifulSoup` - HTML 파싱
- `pandas` - 데이터 처리 및 CSV 저장

---

## 🛠 설치 및 실행 방법

### 1. 패키지 설치

```bash
pip install requests beautifulsoup4 pandas
```

### 2. 실행

```
py news_crawler.py
```
