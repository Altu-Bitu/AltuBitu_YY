#java로 변환
def tojava(text):
    #첫번째 or 마지막 문자가 _일때 __가 있을때
    if text[0] == "_" or text[-1] == "_" or "__" in text: #처음이나 끝이 _이거나 _가 연속으로 나오는 경우 에러
        return "Error!"
    ans="" #정답으로 내보낼 문자열
    flag=False    #_체크해주는 Flag

    for i in text: #모든 텍스트 내의 문자 하나하나에 대하여
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90: #아스키코드로 변환해서 대문자인지 아닌지 판별
            return "Error!"  #대문자이면 무조건 에러 (java형이므로)

        if i == "_":
            flag = True
            continue

        if flag == True:
            ans += i.upper() #_ 다음에 등장한 소문자를 대문자로 만들어줌
            flag=False
            continue

        ans+=i

    return ans
        
#c++로 변환
def toc(text):
    #첫 문자가 대문자 일때
    if ord(text[0])>=65 and ord(text[0])<=90:
        return "Error!"

    ans="" #정답으로 내보낼 문자열

    for i in text:
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90:
            ans+="_"+i.lower() #_를 붙이고 소문자로 변환
        else:
            ans+=i #대문자 아닐때는 그냥 붙임

    return ans


text = input()

if "_" in text:
    print(tojava(text))
else:
    print(toc(text))