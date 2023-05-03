def solution(phone_book):
        answer = True
        hash = {}
        
        for i in phone_book:
            hash[i] = 0

        for i in phone_book:
            print(i)
            temp = ''
            for j in i:
                temp += j
                if temp in hash and temp != i:
                    answer = False
        return answer

print(solution(["34", "3456", "789"]))