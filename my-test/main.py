from time import sleep


class MyClass:

    def __init__(self, name, password) -> None:
        self.name= name
        self.password= password

    def get(self):
        print(self.name, self.password)


if __name__ == '__main__':
    arr=[]
    for _ in range(5000000):
        obj= MyClass("123", 30)
        arr.append(obj)

    print("\033[32mSuccess: 循环结束 (^_^)\033[0m", len(arr))
    sleep(100)