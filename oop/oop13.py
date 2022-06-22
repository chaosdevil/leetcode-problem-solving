from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, new_value):
        self.value2 = new_value

obj = ImmutableClass()
print(obj.value1)

# obj.value1 = "Another value"
# print(obj.value1)

obj.some_func(20)