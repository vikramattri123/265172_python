class store:
    def __init__(self):
        self.stack = []
    def push(self,val):
            self.stack.append(val)

stack_object = store()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
