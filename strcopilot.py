class MyString:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"MyString({self.value!r})"

    def __len__(self):
        return len(self.value)

    def __getitem__(self, index):
        return self.value[index]

    def __contains__(self, item):
        return item in self.value

    def __add__(self, other):
        return MyString(self.value + str(other))

    def __mul__(self, times):
        return MyString(self.value * times)

    def __mod__(self, other):
        return MyString(self.value % other)

    def __eq__(self, other):
        return self.value == str(other)

    def __ne__(self, other):
        return self.value != str(other)

    def __lt__(self, other):
        return self.value < str(other)

    def __le__(self, other):
        return self.value <= str(other)

    def __gt__(self, other):
        return self.value > str(other)

    def __ge__(self, other):
        return self.value >= str(other)

    def show_all_methods(self):
        print("🔍 Dunder & String Method Showcase:")
        print("capitalize:", self.value.capitalize())
        print("casefold:", self.value.casefold())
        print("center:", self.value.center(30, '*'))
        print("count:", self.value.count('a'))
        print("encode:", self.value.encode())
        print("endswith:", self.value.endswith('!'))
        print("expandtabs:", "Hello\tWorld".expandtabs(4))
        print("find:", self.value.find('a'))
        print("format:", "Hi {}, welcome!".format("Dhazz"))
        print("format_map:", "{name} is epic".format_map({'name': 'Dhazz'}))
        print("index:", self.value.index('a') if 'a' in self.value else 'N/A')
        print("isalnum:", self.value.isalnum())
        print("isalpha:", self.value.isalpha())
        print("isascii:", self.value.isascii())
        print("isdecimal:", self.value.isdecimal())
        print("isdigit:", self.value.isdigit())
        print("isidentifier:", self.value.isidentifier())
        print("islower:", self.value.islower())
        print("isnumeric:", self.value.isnumeric())
        print("isprintable:", self.value.isprintable())
        print("isspace:", self.value.isspace())
        print("istitle:", self.value.istitle())
        print("isupper:", self.value.isupper())
        print("join:", "-".join(['Python', 'Rocks']))
        print("ljust:", self.value.ljust(20, '.'))
        print("lower:", self.value.lower())
        print("lstrip:", "   hello".lstrip())
        print("maketrans + translate:", self.value.translate(str.maketrans("aeiou", "12345")))
        print("partition:", self.value.partition('a'))
        print("removeprefix:", self.value.removeprefix("My"))
        print("removesuffix:", self.value.removesuffix("!"))
        print("replace:", self.value.replace('a', '@'))
        print("rfind:", self.value.rfind('a'))
        print("rindex:", self.value.rindex('a') if 'a' in self.value else 'N/A')
        print("rjust:", self.value.rjust(20, '.'))
        print("rpartition:", self.value.rpartition('a'))
        print("rsplit:", self.value.rsplit(' '))
        print("rstrip:", "hello   ".rstrip())
        print("split:", self.value.split(' '))
        print("splitlines:", "Line1\nLine2".splitlines())
        print("startswith:", self.value.startswith('M'))
        print("strip:", "   hello   ".strip())
        print("swapcase:", self.value.swapcase())
        print("title:", self.value.title())
        print("upper:", self.value.upper())
        print("zfill:", self.value.zfill(20))
        print("__class__:", self.__class__)
        print("__dir__:", dir(self))
        print("__doc__:", self.__doc__)
        print("__getattribute__:", self.__getattribute__('value'))
        print("__getnewargs__:", self.__getnewargs__() if hasattr(self, '__getnewargs__') else 'N/A')
        print("__getstate__:", self.__getstate__() if hasattr(self, '__getstate__') else 'N/A')
        print("__hash__:", hash(self.value))
        print("__init_subclass__:", self.__init_subclass__())
        print("__reduce__:", self.__reduce__())
        print("__reduce_ex__:", self.__reduce_ex__(4))
        print("__setattr__:", setattr(self, 'new_attr', '🔥'))
        print("__sizeof__:", self.__sizeof__())
        print("__subclasshook__:", self.__subclasshook__(str))
        print("🧪 Iteration:", [char for char in self])
        print("✅ All done!")

    def __iter__(self):
        return iter(self.value)

# 🔥 Ritual begins
s = MyString("My amazing string!")
s.show_all_methods()