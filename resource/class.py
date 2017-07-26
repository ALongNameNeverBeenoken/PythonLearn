#coding=gbk
#python class 的简单介绍， 每个小节后面都带有测试log打印。 现在全都注释了，需要的，可以打开。

#面向对象的简单介绍
#---------------------------------------------------------------------------------------------------------
#类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#           类比成C，就是typedef 一个结构体（class）， 再用这个结构体定义的变量就是对象。
#          （这个类比是极不成熟的，但是如果对对象没有半点认知，也可以这么初步的认为）
#类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
#       类是有namespace的，对比c就是，类内的相当于类里的全局变量
#
#方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
#          这是一个非常重要的概念，类提供的一大便捷服务。
#
#继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
#      例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
#      类的继承关系，虽然写法上可以随便的，例如用Animal类继承Dog类。但是这样是逻辑上不通的，代码的逻辑性会遭到破坏
#      所以继承的时候，牢记两个点： is-a， has-a
#
#---------------------------------------------------------------------------------------------------------


#1.类的创建
#---------------说明--------------
#a. 使用class语句来创建一个新类，class之后为类的名称并以冒号结尾
#b. self说明
#---------------说明--------------

#1.a.类的创建 start
#例子：
#empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
#第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法。用过C++之类的，这个就是构造函数
#self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
class Employee:
    'this is a base class'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

#boss = Employee("peter", 100000)
#print(boss.displayCount())
#print(boss.displayEmployee())
#me = Employee("mk", 5)
#print(me.displayCount()) #这里的计数就是2了
#print(me.displayEmployee())
#1.a.类的创建 end

#1.b. 类内的self说明 start
#
#self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
#
#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
#
#self代表类的实例，而非类
#
#self 不是 python 关键字，可以换成任意字
#
#因为每一行都是关键的，所以隔开了。

#self指向的是什么
class Test:
    def prt(self):
        print(self)             #输出的是类的实例
        print(self.__class__)   #输出的是类的定义
 
#t = Test()
#t.prt()

#self不是关键字，可以是其他字符
class Test2:
    def prt(justaramdonstring):
        print(justaramdonstring)
        print(justaramdonstring.__class__)

#t2 = Test2()
#t2.prt()

#1.b. 类内的self说明 end

#2.创建实例对象
#---------------说明--------------
#实例化类其他编程语言中一般用关键字 new，但是在 Python 中并没有这个关键字，类的实例化类似函数调用方式。
#
#---------------说明--------------
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

#3.类内属性的访问
#---------------说明--------------
#a. 可以通过.来访问
#b. 可以通过特殊函数来访问,修改属性
#---------------说明--------------

#3.a. 通过.来访问 start

#emp1.displayEmployee()
#emp2.displayEmployee()
#print("Total Employee %d" % Employee.empCount)

#3.a 通过.来访问 end

#3.b 通过特殊函数来访问,修改属性 start
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
#print(emp1.age)
del emp1.age  # 删除 'age' 属性

#可以使用以下函数的方式来访问属性
#getattr(obj, name[, default]) : 访问对象的属性。
#hasattr(obj,name) : 检查是否存在一个属性。
#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#delattr(obj, name) : 删除属性。

#print(hasattr(emp1, 'age'))        # 如果存在 'age' 属性返回 True。
#print(getattr(emp1, 'age'))        # 返回 'age' 属性的值, 这会报错。通过下面的方法给出默认值，就不会报错
#print(getattr(emp1, 'age', 18))    # 返回 'age' 属性的值, 当age没有的时候，18是默认值，对比上一条
#print(setattr(emp1, 'age', 8))     # 添加属性 'age' 值为 8
#delattr(emp1, 'age')               # 删除属性 'age'， 不能删除一个不存在属性，不然会报错

#3.b 通过特殊函数来访问,修改属性  end

#3.类内属性的访问 end

#4.类的内置属性start
#---------------说明--------------
#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#__doc__ :类的文档字符串
#__name__: 类名
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
#---------------说明--------------

#print("Employee.__doc__:", Employee.__doc__)
#print("Employee.__name__:", Employee.__name__)
#print("Employee.__module__:", Employee.__module__)
#print("Employee.__bases__:", Employee.__bases__)
#print("Employee.__dict__:", Employee.__dict__)

#4.类的内置属性end

#5.对象的销毁，也即使垃圾回收 start
#---------------说明--------------
#Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
#在 Python 内部记录着所有使用中的对象各有多少引用。
#一个内部跟踪变量，称为一个引用计数器。
#当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
#垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
#循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。
#Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
#作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。
#在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
#---------------说明--------------

class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

#pt1 = Point()
#pt2 = pt1
#pt3 = pt1
#print(id(pt1), id(pt2), id(pt3)) # 打印对象的id
#del pt1
#del pt2
#del pt3 #这里执行完之后，Point就会被等待回收

#5.对象的销毁，也即使垃圾回收 end

#6.类的继承 start
#---------------说明--------------
#面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
#需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。
#在python中继承中的一些特点：
#  a.在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
#  b.在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
#  c.Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
#
#issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
#isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
#---------------说明--------------

#派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
#class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite

class Parent:        # 定义父类
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法 child method')

#c = Child()          # 实例化子类
#c.childMethod()      # 调用子类的方法
#c.parentMethod()     # 调用父类方法
#c.setAttr(200)       # 再次调用父类的方法
#c.getAttr()          # 再次调用父类的方法



#6.类的继承 end

#7.类方法的重写 start
#---------------说明--------------
#如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
#---------------说明--------------

class Parent_cover:        # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child_cover(Parent_cover): # 定义子类
    def myMethod(self):
        print('调用子类方法')

#c_cover = Child_cover()          # 子类实例
#c_cover.myMethod()         # 子类调用重写方法

#7.类方法的重写 end

#8.运算符重载 start
#---------------说明--------------
#这里只举例了str 跟 add ，其他，需要自行百度。。现在太晚了。没去百度出来
#---------------说明--------------

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
#print(v1 + v2)

#8.运算符重载 end

#9.类的私有属性以及方法 start
#---------------说明--------------
#a.类的私有属性:  两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
#b.两个下划线开头: 声明该方法为私有方法，不能在类地外部调用。在类的内部调用,需要以self.开头
#c.头尾双下划线:  定义的是特列方法，类似 __init__() 之类的。
#d.以单下划线开头:  表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#e.双下划线开头:  表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
#---------------说明--------------

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def __secretfunc(self):
        print("__secretfunc") 
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print ("__secretCount =", self.__secretCount)
        self.__secretfunc()
    
 
#counter = JustCounter()
#counter.count()
#counter.count()
#print("publicCount", counter.publicCount)

#print(counter.__secretCount)  # 报错，实例不能访问私有变量
#counter.__secretfunc() #报错，没有这个方法

#9.类的私有属性以及方法 end
