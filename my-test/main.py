from example.class_a import A, B

if __name__ == '__main__':
    a1 = A()
    a2 = A()
    print(a1 is a2)
    a1 = B()
    a2 = B()
    print(a1 is a2)