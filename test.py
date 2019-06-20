def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_inst
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
ik1 = Kls()
ik2 = Kls()
print iget_no_of_instance(ik1)


class Person:
    name = []

p1 = Person()
p2 = Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]

class A:
    def __init__(self):
        self.__hello = "__hello"
        self._hello="_hello"
        self.hello="hello"


    def foo_print(self):
        print self._hello
        print self.__hello



if __name__ =="__main__":
    a = A()
    # print a.__hello
    print a._hello
    print a.hello