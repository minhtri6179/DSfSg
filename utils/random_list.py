import random


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_demo_lists(list_length, num_lists, min_value, max_value):
    demo_lists = []
    for _ in range(num_lists):
        new_list = [random.randint(min_value, max_value) for _ in range(list_length)]
        demo_lists.append(new_list)

    return demo_lists


def convert_list_to_linkedlist(demo_list):
    dummy = ListNode(0)
    head = dummy
    for val in demo_list:
        cur = ListNode(val)
        head.next = cur
        head = head.next

    return dummy.next


def show_linked_list(head):
    cur = head
    while cur:
        print(f"{cur.val} -> ", end="")
        cur = cur.next


head = convert_list_to_linkedlist([1, 2, 3, 4, 5])
show_linked_list(head)
