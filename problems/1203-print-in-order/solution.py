from threading import Lock

class Foo:
    def __init__(self):
        self.a = Lock()
        self.b = Lock()
        self.a.acquire()
        self.b.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.a.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.a:
            printSecond()
            self.b.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.b:
            printThird()
