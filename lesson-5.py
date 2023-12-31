"""
int a = 25;
a = "Hello world!"; // ошибка
string a = "Hello world!";


int func(list ages) {

}

"""

l = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

p = {}

p = p.fromkeys(l, "a")

print(p)

keys=['a', 'b', 'c']
values = [1, 2, 3]

new = {i: j for (i, j) in zip (keys, values) }

print(new)

