class Number(float):
    ADD_counter = 0
    SUB_counter = 0
    MUL_counter = 0
    DIV_counter = 0

    def __new__(cls, value):
        return super().__new__(cls, value)
    
    def __radd__(self, other):
        Number.ADD_counter += 1
        return Number(super().__radd__(other))

    def __add__(self, other):
        Number.ADD_counter += 1
        return Number(super().__add__(other))
    
    def __rsub__(self, other):
        Number.SUB_counter += 1
        return Number(super().__rsub__(other))

    def __sub__(self, other):
        Number.SUB_counter += 1
        return Number(super().__sub__(other))
    
    def __mul__ (self, other):
        Number.MUL_counter += 1
        return Number(super().__mul__(other))
    
    def __rmul__ (self, other):
        Number.MUL_counter += 1
        return Number(super().__rmul__(other))
    
    def __truediv__(self, other):
        Number.DIV_counter += 1
        return Number(super().__truediv__(other))
    
    def __rtruediv__(self, other):
        Number.DIV_counter += 1
        return Number(super().__rtruediv__(other))
    
    def reset_counters():
        Number.ADD_counter = 0
        Number.SUB_counter = 0
        Number.MUL_counter = 0
        Number.DIV_counter = 0
    
if __name__ == "__main__":
    a = Number(1)
    b = Number(2)
    print(Number.ADD_counter)
    a+b
    a+b
    print(Number.ADD_counter)
    Number.reset_counters()
    print(Number.ADD_counter)



