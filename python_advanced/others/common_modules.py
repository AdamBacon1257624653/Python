import hashlib


def main():
    m5 = hashlib.md5()
    print(m5)
    bs = b'hello world'
    print(bs)
    m5.update(b'hello world')
    print(m5.hexdigest())


if __name__ == '__main__':
    main()
