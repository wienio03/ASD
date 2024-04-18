class Heap:

    def __init__(self, arr: list, arr_size: int):
        self.arr = arr
        self.arr_size = arr_size 

    def upheap(self, k: int):
        n = self.arr_size
        while k > 0:
            parent = (k - 1) // 2
            if self.arr[k] > self.arr[parent]:
                temp = self.arr[k]
                self.arr[k] = self.arr[parent]
                self.arr[parent] = temp
                k = parent
            else:
                #jesli nie ma operacji do wykonania konczymy
                break
                
    
    def downheap(self, k: int):
        n = self.arr_size
        while k <= self.arr_size // 2:
            l = 2 * k #bo j to nastepnik k
            r = 2 * k + 1
            max = k 
            if l < n and self.arr[l] > self.arr[k]:
                max = l
            
            if r < n and self.arr[r] > self.arr[k]:
                max = r
            
            if max != k:
                tmp = self.arr[k]
                self.arr[k] = self.arr[max]
                self.arr[max] = self.arr[k]
                k = max
            else: 
                #jesli nie ma dalszych operacji to konczymy
                break
        
    def construct(self):
        n = self.arr_size
        for i in range(n // 2 - 1, -1, -1):
            self.downheap(i)



def main():
    size = input()
    test_arr = []
    i = 0
    while i < size:
        test_arr.append(input())
        i += 1
    heap = Heap(test_arr, size)
    heap.construct()
    print(heap)

if __name__ == "__main__":
    main()
