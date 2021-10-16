import collections


counter = collections.Counter('hello world')

print(counter)

for i in range(len(counter)):
    print(counter.keys())