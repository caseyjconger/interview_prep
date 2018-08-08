import sys
class Stack(object):
    '''
    Class implementing stack as an array
    '''
    def __init__(self, arr=None, maxsize=100000):
        self.maxsize = maxsize
        if arr is not None:
            if len(arr) > self.maxsize:
                raise MemoryError
            self.items = arr
        else:
            self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]

def main():
    num_entries = int(sys.stdin.readline())
    stack = Stack()
    max_stack = Stack()
    for _ in range(num_entries):
        entry = sys.stdin.readline()
        entry_split = entry.rstrip()
        entry_split = entry_split.split(' ')
        
        if entry_split[0] == '1':
            val = int(entry_split[1])
            if max_stack.items == []:
                max_stack.push(val)
            elif val >= max_stack.items[-1]:
                max_stack.push(val)
            stack.push(int(entry_split[1]))
            
        elif entry_split[0] == '2':
            if stack.peek() == max_stack.peek():
                max_stack.pop()
            stack.pop()
            
        elif entry_split[0] == '3':
            max_element = max_stack.peek()
            print(max_element)
        else:
            raise NameError


if __name__ == '__main__':
    main()
