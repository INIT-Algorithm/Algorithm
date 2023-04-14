#2023-04-13-Week2
#프로그래머스 Level 2 전화번호 목록.py

#hash <- dict : key, value

'''
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
'''

#key value 동일하게 초기화

'''
문자열에 원하는 문자가 있는지 확인하는 방법 in 문자열

text = "hello joonhee"

if "joon" in text : 
    print("T")
else :
    print("F")
'''


def solution(phone_book):
    answer = True
    hash = {}

    for i in phone_book : 
        hash[i] = 0

    print(hash)
    print("--------")

    for i in phone_book : 
        print(i)
        print("--------")

        temp =''
        for j in i :
            temp+=j
        if temp in hash and temp != i :
            answer = False
    return answer

#print(solution(["12","3456","789"]))
solution(["12","3456","789"])

