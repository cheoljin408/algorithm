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