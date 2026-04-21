

---

# 🔷 1. Class & Object

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Narendar", 22)
s1.display()
```

---

# 🔷 2. Constructor Types

## ✅ Default Constructor

```python
class Demo:
    def __init__(self):
        print("Constructor called")

obj = Demo()
```

## ✅ Parameterized Constructor

```python
class Demo:
    def __init__(self, x):
        self.x = x

obj = Demo(10)
print(obj.x)
```

---

# 🔷 3. Types of Variables

## ✅ Instance Variable

```python
class Test:
    def __init__(self):
        self.a = 10

t = Test()
print(t.a)
```

## ✅ Class (Static) Variable

```python
class Test:
    x = 100

print(Test.x)
```

---

# 🔷 4. Types of Methods

## ✅ Instance Method

```python
class Test:
    def show(self):
        print("Instance Method")

t = Test()
t.show()
```

## ✅ Class Method

```python
class Test:
    x = 10

    @classmethod
    def display(cls):
        print(cls.x)

Test.display()
```

## ✅ Static Method

```python
class Test:
    @staticmethod
    def add(a, b):
        return a + b

print(Test.add(2, 3))
```

---

# 🔷 5. Inheritance Types

## ✅ Single Inheritance

```python
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()
```

---

## ✅ Multilevel Inheritance

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()
```

---

## ✅ Multiple Inheritance

```python
class A:
    def showA(self):
        print("A")

class B:
    def showB(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.showA()
obj.showB()
```

---

## ✅ Hierarchical Inheritance

```python
class A:
    def show(self):
        print("Parent")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

b.show()
c.show()
```

---

# 🔷 6. Encapsulation

## ✅ Public

```python
class Demo:
    def __init__(self):
        self.x = 10

obj = Demo()
print(obj.x)
```

## ✅ Protected (_)

```python
class Demo:
    def __init__(self):
        self._x = 20

obj = Demo()
print(obj._x)
```

## ✅ Private (__)

```python
class Demo:
    def __init__(self):
        self.__x = 30

    def get_x(self):
        return self.__x

obj = Demo()
print(obj.get_x())
```

---

# 🔷 7. Abstraction

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of circle")

c = Circle()
c.area()
```

---

# 🔷 8. Polymorphism

## ✅ Method Overriding

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

obj = B()
obj.show()
```

---

## ✅ Method Overloading (Python way)

```python
class Demo:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Demo()
print(obj.add(2))
print(obj.add(2, 3))
print(obj.add(2, 3, 4))
```

---

# 🔷 9. Operator Overloading

```python
class Demo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

a = Demo(10)
b = Demo(20)

print(a + b)
```

---

# 🔷 10. Method Resolution Order (MRO)

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

---

# 🔷 11. Destructor

```python
class Demo:
    def __del__(self):
        print("Object destroyed")

obj = Demo()
del obj
```

---

# 🔷 12. Real-Time Example (Important 🔥)

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount("Narendar", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
```

---

