
class LookingGlass:

    def __enter__(self):  # <1>
        import sys
        self.f = open('log.txt', 'w+')
        self.original_write = sys.stdout.write  # <2>
        sys.stdout.write = self.reverse_write  # <3>
        # self.f.write(self.original_write)
        return 'JABBERWOCKY'  # <4>

    # def reverse_write(self, text):  # <5>
    #     self.f.write(text[::-1])

    def reverse_write(self, text):  # <5>
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # <6>
        import sys  # <7>
        self.f.close()
        sys.stdout.write = self.original_write  # <8>
        if exc_type is ZeroDivisionError:  # <9>
            print('Please DO NOT divide by zero!')
            return True  # <10>


if __name__ == '__main__':
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print('end')
    print(what)
