#네이버 평점 크롤링 => 데이터 베이스에 저장
#old_content > table > tbody > tr:nth-child(1)
from urlToStr import urlToStr
from bs4 import BeautifulSoup

def naverCraw(page) :
    data = urlToStr("https://movie.naver.com/movie/point/af/list.nhn?&page="+page)

    bs = BeautifulSoup(data,"html.parser")
    tit3s = bs.select("tbody > tr")
    cnt = 0
    datars = []
    for tit3 in tit3s:
        cnt = cnt + 1
        datars1 = []
        mvname = tit3.find("a").text
        star = int(tit3.find("em").text)
        writer = tit3.select_one(".author").text
        #old_content > table > tbody > tr:nth-child(3) > td.title > div
        content = tit3.find_all("td")[1].find_all("a")[1]["href"].split(",")[2].replace("'","")
        cdate = tit3.find_all("td")[2].text.split("****")[1]
        datars1.append(mvname)
        datars1.append(star)
        datars1.append(writer)
        datars1.append(cdate)
        datars1.append(content)
        #print(cnt , ":", mvname, star, writer, cdate, content)
        datars1 = tuple(datars1)
        datars.append(datars1)
        #print(datars1)
        #print("-"*30)    

    return datars 

if __name__ == "__main__" :
    totalData = []
    
    for i in range(1,11):
        datars = naverCraw(str(i))
        #print(datars)
        #print("-"*30)
        totalData = totalData + datars

    print(totalData)
