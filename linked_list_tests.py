import unittest

from linked2 import Node

from linked2 import LinkedList

class LinkedListTests(unittest.TestCase):

    def setUp(self):

        self.s2_list = LinkedList()
        self.s2_list.add_in_tail(Node(1))
        self.s2_list.add_in_tail(Node(2))

        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(4))

    def test_find_all(self):

        self.assertEqual(2, len(self.s_list.find_all(3)), " Функция возвращает список некорректной длины")
        self.assertEqual(1, self.s_list.find_all(1)[0].value, " Функция возвращает некорректный список ")
        self.assertEqual(2, self.s_list.find_all(2)[0].value, " Функция возвращает некорректный список ")
        self.assertEqual(3, self.s_list.find_all(3)[0].value, " Функция возвращает некорректный список ")
        self.assertEqual([], self.s_list.find_all(5), " Функция возвращает некорректный список ")

    def test_delete(self):

        self.s_list.delete(4, True)
        self.s_list.delete(1, False)
        self.assertEqual(self.s_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 3, "Значение элемента tail некорректно")
        self.s_list.delete(2, True)
        self.assertEqual(self.s_list.head.value, 3, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 3, "Значение элемента tail некорректно")
        self.s_list.delete(3, False)
        self.assertEqual(self.s_list.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail, None, "Значение элемента tail некорректно")

    def test_delete_tail_false(self):

        self.s2_list.print_all_nodes()
        self.s2_list.delete(2, False)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_head_false(self):

        self.s2_list.print_all_nodes()
        self.s2_list.delete(1, False)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_tail_true(self):

        self.s2_list.print_all_nodes()
        self.s2_list.delete(2, True)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_head_true(self):

        self.s2_list.print_all_nodes()
        self.s2_list.delete(1, True)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

if __name__ == '__main__':

    unittest.main()
