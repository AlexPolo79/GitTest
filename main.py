print("Hello word")
for i in "Hello word":
    print(i)

print('___________________________')

def main():
    yield from (i for i in range(10) if i%2 == 0)