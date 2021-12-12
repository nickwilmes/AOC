'''
+ sets
+ f-string =
+ clone list with [:]
+ append vs extend
+ python builtin functions (sum, sorted, map, filter, zip, isinstance, )
dataclasses
collections
'''

# li = [1, 2, 3, 3]
# s1 = set(li)
# s2 = {'a', 'b', 'c'}

# print(f"{li=}")
# print(f"{s1=}")
# print(f"s2={s2}")

# s3 = set([1,2,3])
# s4 = set([4,5,3])
# print(s4.difference(s3))

# li = [1,2,3,4]
# li2 = li[:]

# li[0] = 10

# print(f"{li=}")
# print(f"{li2=}")


# l1 = [1,2,3]
# l2 = [4,5,6]

# l1.extend(l2)

# print(f"{l1=}")
# print(f"{l2=}")

# print(sum(range(1,100,2)))

# l1 = [7,1,2,3]
# print(sorted(l1))
# print(l1)

# l1 = [7,1,2,3]
# print(list(map(str, l1)))

# l2 = []
# for i in l1:
#     l2.append(i*2)
# print(l2)

# print(list(filter(lambda i: i%2==1, l1)))

# l2 = []
# for i in l1:
#     if i%2==1:
#         l2.append(i)
# print(l2)

# ex = KeyError()
# if isinstance(ex, Exception):
#     print("hello")