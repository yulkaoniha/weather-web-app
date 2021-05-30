class Cities:
    def accept(self, visitor):
        visitor.visit(self)

    def search(self, visitor):
        print(self, "searched by", visitor)

    def show(self, visitor):
        print(self, "seen by", visitor)

    def __str__(self):
        return self.__class__.__name__


class Konotop(Cities):
    pass


class Rome(Cities):
    pass


class Seoul(Cities):
    pass


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class Guest1(Visitor):
    def visit(self, crop):
        crop.search(self)


class Guest2(Visitor):
    def visit(self, crop):
        crop.show(self)


konotopV = Konotop()
romeV = Rome()
seoulV = Seoul()

visitor1 = Guest1()
visitor2 = Guest2()

konotopV.accept(visitor1)
konotopV.accept(visitor2)

romeV.accept(visitor1)
romeV.accept(visitor2)

seoulV.accept(visitor1)
seoulV.accept(visitor2)
