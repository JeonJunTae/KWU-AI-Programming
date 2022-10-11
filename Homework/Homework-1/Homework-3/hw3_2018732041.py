import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter

browser = webdriver.Chrome("/Users/jeonjuntae/Documents/python/chromedriver") # 크롬드라이버 파일 경로
url = 'https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8' # 접속페이지 url
browser.get(url) # 페이지 접속

str = browser.find_element(By.XPATH, '//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div/div/div/div/div[1]').text # text 가져오기
# 제가 다운받은 selenium version 4에서는 find_element_by_xpath 가 위의 코드처럼 변경되어서 By.XPATH 를 이용했습니다.

newstr = str.split(' ') 
kbo = [n for n in newstr if len(n)>1 ] # 단어의 길이가 1인 것은 제외
dc = Counter(kbo) # 단어별 빈도수 형태의 딕셔너리 구성
for key in list(dc.keys()):
    if dc[key] <= 2: # 빈도수가 2 이하이면
        del dc[key] # 딕셔너리에서 삭제

keylist = list(dc.keys()) # 단어만 리스트로 반환
str2 = ' '.join(keylist) # 문자열로 반환

s_words = wordcloud.STOPWORDS.union({'없다','것을','않을','따라','없다고','아닌','있을','오히려','있다','없는','않았다','한다','또한','것이라고','만큼','그런','하고','참고로','있는데','모든','있다는'})
image = wordcloud.WordCloud(font_path = 'AppleGothic',width = 1000, height = 700, stopwords = s_words).generate(str2)
# 제가 맥을 사용하기 때문에 폰트경로를 위와같이 설정했습니다.

plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()

browser.quit
browser.close()