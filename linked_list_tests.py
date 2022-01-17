import unittest

from LinkedList1 import Node

from LinkedList1 import LinkedList

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

    def test_delete_len_check(self):

        self.assertEqual(self.s2_list.len(), 2, "Значение длины до удаления некорректно")
        self.assertEqual(self.s2_list.head.next, self.s2_list.tail, "Next элемента head не указывает на второй элемент")
        self.assertEqual(self.s2_list.tail.next, None, "Next элемента tail не указывает на None")
        self.s2_list.delete(1, False)
        self.assertEqual(self.s2_list.len(), 1, "Значение длины после удаления некорректно")
        self.assertEqual(self.s2_list.head.next, None, "Next элемента head не указывает на None")
        self.assertEqual(self.s2_list.tail.next, None, "Next элемента tail не указывает на None")

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

        self.s2_list.delete(2, False)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s2_list.tail.next, None, "next не указывает на None")

    def test_delete_head_false(self):

        self.s2_list.delete(1, False)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s2_list.tail.next, None, "next не указывает на None")

    def test_delete_tail_true(self):

        self.s2_list.delete(2, True)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s2_list.tail.next, None, "next не указывает на None")
        self.assertEqual(self.s2_list.len(), 1, "len should be 1")

    def test_delete_head_true(self):

        self.s2_list.delete(1, True)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s2_list.tail.next, None, "next не указывает на None")

    def test_delete_single_head(self):
        s3_list = LinkedList()
        s3_list.add_in_tail(Node(1))
        s3_list.delete(1, True)
        self.assertEqual(s3_list.head, None, "Значение элемента head некорректно")
        self.assertEqual(s3_list.tail, None, "Значение элемента tail некорректно")

if __name__ == '__main__':

    unittest.main()
