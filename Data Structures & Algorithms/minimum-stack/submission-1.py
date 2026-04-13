class MinStack2:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val
        else:
            if val >= self.min:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.min)
                self.min = val
        
    def pop(self) -> None:
        top = self.stack.pop()
        if top >= self.min:
            return self.top
        actual_top = self.min
        prev_min = 2 * actual_top - top
        self.min = prev_min
        return top

    def top(self) -> int:
        cur_top = self.stack[-1]
        return cur_top if cur_top >= self.min else self.min
        
    def getMin(self) -> int:
        return self.min


class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
