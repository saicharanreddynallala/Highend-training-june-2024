class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class sll:
    def __init__(self,data) -> None:
        self.head = Node(data)
    def display(self):
        t = self.head
        while (t!=None):
            print(t.data,end="->")
            t = t.next
        print()
    def add_back(self,data):
        t = self.head
        while t.next!= None:
            t = t.next
        t.next = Node(data)
    def add_front(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def search_ele(self,data):
        t= self.head
        while t!= None:
            if t.data == data:
                return True
            t = t.next
        return False      
    def middle_node(self):
        t= self.head
        prev = self.head
        while t and t.next:
            t = t.next.next
            prev = prev.next
        print(prev.data)
    def all_pairs(self):
        t1 = self.head
        while t1!= None:
            t2 = t1
            while t2 != None:
                print((t1.data,t2.data),end=" ")
                t2 = t2. next
            t1 = t1.next
        print()
    def even_or_odd_len(self):
        slow =fast = self.head
        count = 0
        while fast!= None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            count +=2
        if fast:
            count +=1
        print(count %2)
    def max_subsequence(self):
        curr = self.head
        next = curr.next
        max_count = 0
        count = 1
        while next != None :
            if next.data - curr.data ==1:
                count +=1 
                next = next.next
                curr = curr.next
            else:
                max_count = max(max_count , count)
                curr = next
                next = next.next
                count = 1
        return max(count , max_count)
    def bubble_sort(self):
        t1 = self.head
        while t1!= None:
            t2 = t1
            while t2 != None:
                if t1.data < t2.data:
                    t1.data ,t2.data= t2.data, t1.data
                t2 = t2. next
            t1 = t1.next
    def palindrome(self):
        def check(node1,node2):
            if not node2.next:
                return node1.data == node2.data
            return node1.data == node2.data and check(node1 ,node2.next)
        return check(self.head,self.head)
    def bubble(self):
        c = 0
        T =self.head
        p = None
        while (T.next != None):
            f = 0
            t = self.head
            while t.next is not p:
                if t.data > t.next.data:
                    f =1
                    t.data,t.next.data = t.next.data,t.data
                t= t.next
                c +=1
            if not f:
                break
        p = t
        T = T.next
    def reverse_list(self):
        prev = self.head
        temp = prev.next
        prev.next = None
        c = temp.next
        while c is not None:
            c = temp.next
            temp.next = prev
            prev = temp
            temp = c 
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return self.head
        dummy = Node(0)
        prev = dummy
        dummy.next = self.head
        curr = self.head
        while curr and curr.next:
            f ,s = curr.next ,curr.next.next
            f.next = curr
            curr.next =s
            prev.next = f
            
            prev = curr
            curr =curr.next
        return dummy.next   
l1 = sll(5)
l1.add_back(7)
l1.add_back(8)
l1.add_back(2)
l1.add_back(1)
l1.add_back(4)
# l1.display()

# print(l1.search_ele(15612))
# l1.middle_node()
# l1.all_pairs()
# l1.even_or_odd_len()
# l2.even_or_odd_len()
# print(l1.max_subsequence())
# l1.bubble_sort()
# l1.display()
# print(l1.palindrome())
# l1.bubble()
# l1.reverse_list()
l1.display()
l1.head = l1.swap_pairs()
l1.display()