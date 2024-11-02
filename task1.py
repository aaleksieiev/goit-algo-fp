class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next    

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node    

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node        

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse(self):
        curr = self.head
        prev = None

        # Прохід по всіх елементах
        while curr is not None:

            # Сбереження наступного
            next_node = curr.next

            # Заміна вкащівника на наступний елемент на попередній
            curr.next = prev

            # Перехід до наступного елементу
            prev = curr
            curr = next_node

        # Збереження нової глови
        self.head = prev

    def sorted_insert(self, newnode, sorted_head):
        # Обробка head елементу
        if sorted_head is None or sorted_head.data >= newnode.data:
            newnode.next = sorted_head
            return newnode
        else:
            curr = sorted_head
            
            # Знахдження вузла перед точкою вставки
            while curr.next is not None and curr.next.data < newnode.data:
                curr = curr.next
            newnode.next = curr.next
            curr.next = newnode
            return sorted_head

    def insertion_sort(self):
    
        # Ініціалізація відсортованого списку
        sorted_head = None
        curr = self.head
        
        # Проходження списку і вставка відсортованого елемента
        while curr is not None:
            next_node = curr.next
            
            # Всатвка
            sorted_head = self.sorted_insert(curr, sorted_head)
            
            # Перехід до наступного
            curr = next_node
        self.head = sorted_head

    def merge(self, llist):
        # Проходження списку. щоб знайти останній елемент
        last_element = self.head
        while last_element.next:
            last_element = last_element.next

        # Додавання елемент в список
        element_to_merge = llist.head
        while element_to_merge:
            self.insert_at_beginning(element_to_merge.data)
            element_to_merge = element_to_merge.next

        self.insertion_sort()


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse()
print("Зв'язний список після обертання:")
llist.print_list()

llist.insertion_sort()
print("Зв'язний список після сортування:")
llist.print_list()

llist2 = LinkedList()

# Вставляємо вузли в початок
llist2.insert_at_beginning(52)
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(13)

# Вставляємо вузли в кінець
llist2.insert_at_end(-20)
llist2.insert_at_end(3)

llist.merge(llist2)
print("Зв'язний список після сортування:")
llist.print_list()
