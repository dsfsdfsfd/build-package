class Math:
    def __init__(self, value: int) -> None:
        self.value = value
    def factorial(self) -> int:
        if self.value == 0:
            return 1
        else:
            return self.value * Math(self.value - 1).factorial