def solution(numbers):
    text = numbers  # 원래 문자열을 저장
    result = ""     # 숫자를 이어 붙일 빈 문자열 만들기
    if "zero" in text:
        text = text.replace("zero", "0")
    if "one" in text:
        text = text.replace("one", "1")
    if "two" in text:
        text = text.replace("two", "2")
    if "three" in text:
        text = text.replace("three", "3")
    if "four" in text:
        text = text.replace("four", "4")
    if "five" in text:
        text = text.replace("five", "5")
    if "six" in text:
        text = text.replace("six", "6")
    if "seven" in text:
        text = text.replace("seven", "7")
    if "eight" in text:
        text = text.replace("eight", "8")
    if "nine" in text:
        text = text.replace("nine", "9")
    result = int(text)  # 문자열을 정수로 바꾸기
    return result

print(solution("onetwothreefourfivesixseveneightnine")) # 출력: 123456789
print(solution("onefourzerosixseven")) # 출력: 14067