class A:
    def m1(self):
        print("m1")


class B:
    def m2(self):
        print("m2")

class C(A,B):
    def m3(self):
        print("m3")



obj =C()

obj.m1()
obj.m2()
obj.m3()





