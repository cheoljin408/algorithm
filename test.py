from functools import reduce

data1 = [ ["고구마",25000],
         ["바나나",123232],
         ["파인애플",4500],
         ["감자",3000],
         ["금귤",6000] ]
print(data1)

data1.sort(key=lambda x: x[0])
print(data1)

data1.sort(key=lambda x: x[1])
print(data1)

data2 = ["나라","가구","봄","가을","도토리","낫","혹","가을 아침","나는 밥을 먹고 있다."]
print(data2)

data2.sort(key=lambda x: len(x))
print(data2)

data2.sort(key=lambda x: (len(x), x))
print(data2)

str = 'abcde'
list_abcde = ['a', 'b', 'c', 'd', 'e']

print(str)
print(str[::-1])
print(str[2:])

print(list_abcde)
print(list_abcde[::-1])
print(list_abcde[2:])

print((lambda x,y: x+y)(1, 5))

nums = [1, 2, 3, 4, 5]
# 각 원소에 제곱을 한다.
new_nums = list(map(lambda x: x**2, nums))

# 1, 4, 9, 16, 25
print(new_nums)

# reduce
sum = reduce(lambda acc, cur: acc+cur, nums, 0)

print(sum)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums 중에 짝수만 반환
even = list(filter(lambda x: x % 2 == 0, nums))

print(even)

product = [
    ['신라면', 1200],
    ['너구리', 1500],
    ['진라면', 1100],
    ['불닭볶음면', 1600],
    ['삼양라면', 1100],
    ['안성탕면', 1200]
]

print(sorted(product, key=lambda x: x[1]))
print(sorted(product, key=lambda x: (x[1], x[0])))