class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self, head=None):
        self._head = head

    def isEmpty(self):
        return self._head is None

    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, node):
        if self.isEmpty():
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def append(self, node):
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def remove(self, node):
        cur = self._head
        while cur.next != node:
            cur = cur.next
        node_next = node.next
        cur.next = node_next
        node.next = None
        node = None

    def find(self, node):
        """
        check if an item exists
        :param item:
        :return:
        """
        cur = self._head
        while cur is not None:
            if cur == node:
                return True
            else:
                cur = cur.next
        return False


def main():
    n1 = Node(35)
    n2 = Node(28)
    n3 = Node(10)
    list = SingleLinkList()
    list.add(n1)
    list.add(n3)
    list.append(n2)
    list.travel()
    list.remove(n2)
    list.travel()
    print("n1 exist: %s" % list.find(n2))
    print("isEmpty: %s" % list.isEmpty())
    print("length: %s" % list.length())


if __name__ == '__main__':
    main()
