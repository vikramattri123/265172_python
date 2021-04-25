class delete:
    def __init__(self):
        self.stacks = []

    def push(self, val):
        self.stacks.append(val)

    def pop(self):
        val = self.stacks[-1]
        del self.stacks[-1]
        return val

stack_object = delete()
stack_object.push(4)
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())