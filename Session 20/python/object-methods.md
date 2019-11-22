# Python Object Oriented Programming

## Instance method, Static method, Class method

```python
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

### Instance Method
The first method on MyClass, called method, is a regular instance method. Through the self parameter, instance methods can freely access attributes and other methods on the same object.

Not only can they modify object state, instance methods can also access the class itself through the `self.__class__` attribute. This means instance methods can also modify class state.

### Class Method
Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.

Instead of accepting a `self` parameter, class methods take a `cls` parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

### Static Method
The third method, MyClass.staticmethod was marked with a `@staticmethod` decorator to flag it as a static method.

This type of method takes neither a `self` nor a `cls` parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

### Let’s See Them In Action!

```python
>>> obj = MyClass()
>>> obj.method()
('instance method called', <MyClass instance at 0x101a2f4c8>)
```

When the method is called, Python replaces the self argument with the instance object, obj. We could ignore the syntactic sugar of the dot-call syntax (`obj.method()`) and pass the instance object manually to get the same result:

```python
>>> MyClass.method(obj)
('instance method called', <MyClass instance at 0x101a2f4c8>)
```

By the way, instance methods can also access the class itself through the `self.__class__` attribute. This makes instance methods powerful in terms of access restrictions - they can modify state on the object instance and on the class itself.


Let’s try out the **class method **next:

```python
>>> obj.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
```

Notice how Python automatically passes the class as the first argument to the function when we call `MyClass.classmethod()`. Calling a method in Python through the dot syntax triggers this behavior. The self parameter on instance methods works the same way.

Please note that naming these parameters self and cls is just a convention. You could just as easily name them the_object and the_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.


Time to call the **static method** now:

```python
>>> obj.staticmethod()
'static method called'
```

Did you see how we called `staticmethod()` on the object and were able to do so successfully? Behind the scenes Python simply enforces the access restrictions by not passing in the `self` or the `cls` argument when a static method gets called using the dot syntax.

This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s (and every instance’s) namespace.

Now, let’s take a look at what happens when we attempt to call these methods on the class itself - without creating an object instance beforehand:

```python
>>> MyClass.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)

>>> MyClass.staticmethod()
'static method called'

>>> MyClass.method()
TypeError: unbound method method() must be called with MyClass instance as first argument (got nothing instead)
```

We were able to call `classmethod() `and `staticmethod()` just fine, but attempting to call the instance method `method()` failed with a `TypeError`.

And this is to be expected — this time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the `self` argument and therefore the call fails.


### Why use `static` methods
Using static methods and class methods are ways to communicate developer intent while enforcing that intent enough to avoid most slip of the mind mistakes and bugs that would break the design.

Static methods also have benefits when it comes to writing test code.

Because the `staticmethod()` method is completely independent from the rest of the class it’s much easier to test.

## References
- https://realpython.com/instance-class-and-static-methods-demystified/