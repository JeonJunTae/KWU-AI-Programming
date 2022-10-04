f = open('hw2.csv', 'r') # csv 파일 읽기
Info = f.read().splitlines() # 한줄 한줄 리스트에 저장 (\n 제거)
f.close()
    
dc={} 
for i in Info: # key : 선수명, value : 14가지 항목값의 리스트 딕셔너리 만들기
    player = i.split(',') # 문자열을 ',' 기준으로 잘라서 리스트로 반환
    item = []
    for n in range(1,15):
        item.append(player[n])
        dc[player[0]] = item # 빈 딕셔너리에 key = 선수명 , value = 특정항목 값 추가


def playerInfo(): # 선수의 모든 정보
    
    players = list(dc.keys()) # 선수명단 리스트
    del players[0] # 맨 앞의 key 값인 '선수명' 삭제
    
    print("선수목록 : {0}".format(players)) # 선수명 보여주기
    
    names = input("선수명을 입력하시오.(여러명 가능, 띄어쓰기로 구분): ")
    list1 = names.split(' ') # 입력받은 문자열을 리스트로 변환
    
    items = list(dc.values())[0] # 특정항목 목록 리스트
    
    for i in players:
        for k in list1: 
            if k == i: # 입력받은 선수이름이 선수목록에 있으면
                print("선수명 : {0}".format(k)) # 선수명 출력
                for n in range(0,14): # 특정항목 인덱스 찾기
                    print("{0} : {1}".format(items[n],dc[k][n])) # 특정항목과 값 출력
                print("\n")
            
            
def specificInfo(): # 선수의 특정항목 정보
    
    players = list(dc.keys()) # 선수명단 리스트
    del players[0] # 맨 앞의 key 값인 '선수명' 삭제
    
    items = list(dc.values())[0] # 특정항목 목록 리스트
    
    print("선수목록 : {0}".format(players)) # 선수명 보여주기
    print("특정항목 목록: {0}".format(items)) # 특정항목 목록 보여주기
    
    str = input("선수명과 특정항목(여러개 가능)을 입력하시오(띄어쓰기로 구분): ")
    list1 = str.split(' ') # 입력받은 문자열을 리스트로 변환
    
    for i in players:
        if list1[0] == i: # 입력받은 선수가 선수명단에 있으면
            for k in list1: 
                for n in range(0,14):
                    if k == items[n]: # 특정항목 찾기
                        print("{0} : {1}".format(k,dc[i][n])) # 선수명과 특정항목 값 출력


                            
def rankingInfo(): # 특정항목의 순위
    
    players = list(dc.keys()) # 선수명단 리스트
    del players[0] # 맨 앞의 key 값인 '선수명' 삭제
    
    items = list(dc.values())[0] # 특정항목 목록 리스트
    
    print("특정항목 목록: {0}".format(items)) # 특정항목 목록 보여주기
    
    list1 = input("특정항목을 입력하시오.(여러개 가능, 띄어쓰기로 구분): ") 
    itemlist = []
    itemlist = list1.split(' ') # 입력받은 문자열 리스트로 변환
    
    for j in itemlist:
        rank = {} 
        for n in range(0,14):
            if j == items[n]: # 입력받은 특정항목의 인덱스 n 찾기
                for name in players:
                    rank[name] = dc[name][n] # 빈 딕셔너리에 해당 특정항목 값 추가
                result = sorted(rank.items(), key=lambda x : x[1],reverse=True) # 내림차순으로 정렬
                print("{0} 순위".format(j))
                for k in range(len(players)):
                    print("{0}위 : {1} - {2}".format(k+1,result[k][0],result[k][1])) # 정렬된 리스트의 값 하나씩 출력
                print("\n")
                            


def main(): # main 함수
    
    while True: 
        print("1 : 선수의 모든 정보")
        print("2 : 선수의 특정항목 정보")
        print("3 : 특정항목의 순위")
        num = int(input("알고싶은 정보가 무엇입니까?(1 or 2 or 3):"))
    
        if num == 1:
            playerInfo()
        elif num == 2:
            specificInfo()
        else:
            rankingInfo()
        
        opinion = input("선수 정보를 더 보시겠습니까?(y/n): ")
        if opinion == 'y':
            pass
        else:
            break
            
main() # main 함수 실행
