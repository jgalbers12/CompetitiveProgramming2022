from sys import stdin, stdout

class Heap:

    def __init__(self, max_size):
        self.size = 0
        self.heap = [None] * max_size

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return(i * 2 + 1)

    def right_child(self, i):
        return(i * 2 + 2)

    def insert(self, val):
        i = self.size
        self.heap[i] = val
        self.size += 1
        if self.size == 1:
            return
        while (i > 0):
            parent_i = self.parent(i)
            if self.heap[parent_i] > self.heap[i]:
                (self.heap[parent_i], self.heap[i]) = (self.heap[i], self.heap[parent_i])
                i = parent_i
            else:
                break

    def heapify(self, index):

        if self.size == 1:
            return

        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index
        if (left < self.size and self.heap[left] < self.heap[smallest]):
            smallest = left

        if (right < self.size and self.heap[right] < self.heap[smallest]):
            smallest = right

        if (smallest != index):
            (self.heap[smallest], self.heap[index]) = (self.heap[index], self.heap[smallest])
            index = smallest
            self.heapify(index)

    def delete_min(self):
        if self.size > 0:
            last = self.heap[self.size - 1]
            self.heap[0] = last
            self.size -= 1
            self.heapify(0)
            return True
        else:
            return False

def main():

    max_size = int(stdin.readline())

    leaf_count = [0] * (max_size + 2)

    leaves = Heap(max_size)

    in_arr = [0] * max_size
    out_arr = [0] * max_size

    for i in range(max_size):
        node = int(stdin.readline())
        in_arr[i] = node
        leaf_count[node] += 1

    for i in range(1, max_size + 1):
        if leaf_count[i] == 0:
            leaves.insert(i)

    for i in range(max_size):
        out_arr[i] = leaves.heap[0]
        if leaves.delete_min():
            leaf_count[in_arr[i]] -= 1
            if leaf_count[in_arr[i]] == 0:
                leaves.insert(in_arr[i])
        else:
            stdout.write("Error")
            return
    
    for i in range(max_size):
        stdout.write(f"{out_arr[i]}\n")

if __name__ == "__main__":
    main()