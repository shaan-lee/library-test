from collections import Counter
import re

# Sample unknown language text (replace with your text)
text = """
[ 너를 만나다 ] 148(+153)화가 업로드되었습니다🥰
항상 잊지 않고 챙겨봐 주셔서 감사합니다 ॱ ᗜ ॱ ღ

무료회차에 단체사진 풀려서 올리고갑니다 ㅎㅎ
원본 스토리에도 올려놓을게요
늦어서 죄송합니다!

#너를만나다 #偶然出会った君 #카카오웹툰 #카카오페이지 #ピッコマ #piccoma  #순정만화 #웹툰 
#kakaowebtoon #kakaopage #webtoon #illust #illustration 
#drawing #manhwa #romance #artwork

모든 게 처음이라 부끄러운 연하공과
그런 동생을 놀려먹는 형아😆

🔎미스터블루 검색창에
💓드롭아웃💓을 검색해 보세요!

#bl #bl추천 #webtoon #blwebtoon
#BL #연예계 #사랑꾼공 #잔망수
#무료웹툰 #웹툰추천 #웹툰보는곳 #BL보는곳

플러팅 장인이 작정하고 꼬시면 일어나는 일.. 지창욱 치명적인 FOX 모먼트.zip #수상한파트너 #모았캐치 #SBSCatch #kkuljaem #SBS수상한파트너 #드라마다시보기 #드라마요약 #드라마추천 #드라마키스 #수상한파트너1회 #수상한파트너명장면 #수상한파트너몰아보기 #수상한파트너요약 #수상한파트너지창욱 #수상한파트너지창욱남지현 #스브스캐치 #스브스캐치드라마 #지창욱드라마 #지창욱연기

메이저┃Hello(구 ON) 토지노 주소 scs33.com 코드 HH22 , 첫가입 30%, 스포츠 매일 10%, 카지노 매일 5% 포인트 지급

주소 http://scs33.com 코드 HH22

#Hello(헬로) #토토사이트 #메이저놀이터 #안전놀이터 #메이저사이트 #카지노 #바카라 #슬롯 #미니게임 #블랙툰


"""
# Tokenization (simple whitespace-based)
tokens = re.findall(r"\b\w+\b", text.lower())

# Calculate token frequencies
token_counts = Counter(tokens)

# Example: Filter common English stop words (you may need a list for your specific use case)
stop_words = set(["the", "and", "is", "in", "it", "to", "of", "for", "on", "with"])

# Filter out stop words
filtered_tokens = [token for token in tokens if token not in stop_words]

# Rank tokens by frequency
token_ranking = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)

# Choose the top N tokens as keywords (adjust N as needed)
top_keywords = [token for token, count in token_ranking[:10]]

# Print the extracted keywords
print(top_keywords)
