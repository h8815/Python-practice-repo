def gen():
    global i
    for i in range(1,6):
        yield i

# for i in gen():
g = gen()
print(next(g))
print(next(g))
for i in g:
    print(i)
