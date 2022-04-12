import unittest

from linked_from_git import Node

from linked_from_git import LinkedList

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

        self.s_list3 = LinkedList()
        self.s_list3.add_in_tail(Node(0))
        self.s_list3.add_in_tail(Node(0))
        self.s_list3.add_in_tail(Node(1))
        self.s_list3.add_in_tail(Node(1))
        self.s_list3.add_in_tail(Node(1))
        self.s_list3.add_in_tail(Node(2))
        self.s_list3.add_in_tail(Node(2))

    def test_delete_00111222_check(self):

        self.s3_list = LinkedList()
        self.s3_list.add_in_tail(Node(0))
        self.s3_list.add_in_tail(Node(0))
        self.s3_list.add_in_tail(Node(1))
        self.s3_list.add_in_tail(Node(1))
        self.s3_list.add_in_tail(Node(1))
        self.s3_list.add_in_tail(Node(2))
        self.s3_list.add_in_tail(Node(2))

        self.s3_list.delete(1, True)  # останется 0 0 2 2
        self.s3_list.delete(2, True)  # останется 0 0

        self.assertEqual(self.s3_list.head.next, self.s3_list.tail, "Next элемента head не указывает на второй элемент")
        self.assertEqual(self.s3_list.tail.next, None, "Next элемента tail не указывает на None")

        self.assertEqual(self.s3_list.head.value, 0, "Value элемента head не равно 0")
        self.assertEqual(self.s3_list.tail.value, 0, "Value элемента tail не равно 0")

        self.s3_list.delete(0, False)  # будет удален первый ноль, останется один элемент ноль
        self.assertEqual(self.s3_list.head.value, 0, "Value элемента head не равно 0")
        self.assertEqual(self.s3_list.tail.value, 0, "Value элемента tail не равно 0")
        self.assertEqual(self.s3_list.head.next, None, "Next элемента head не указывает на None")
        self.assertEqual(self.s3_list.tail.next, None, "Next элемента tail не указывает на None")
        self.s3_list.delete(0, False)  # будет удален первый ноль, не останется ничего
        self.assertEqual(self.s3_list.head, None, "head не none")
        self.assertEqual(self.s3_list.tail, None, "tail не none")
        # self.assertEqual(self.s3_list.head.next, None, "Next элемента head не указывает на None")
        # self.assertEqual(self.s3_list.tail.next, None, "Next элемента tail не указывает на None")

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
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")

    def test_delete(self):

        self.s_list.delete(4, True)
        self.s_list.delete(1, False)
        self.assertEqual(self.s_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 3, "Значение элемента tail некорректно")
        self.s_list.delete(2, True)
        self.assertEqual(self.s_list.head.value, 3, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 3, "Значение элемента tail некорректно")
        self.s_list.delete(3, False)
        self.assertEqual(self.s_list.head.value, 3, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 3, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.head.next, None, "Значение указателя хвоста некорректно")


    def test_delete_tail_false(self):

        self.s2_list.delete(2, False)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_head_false(self):

        self.s2_list.delete(1, False)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_tail_true(self):

        self.s2_list.delete(2, True)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_head_true(self):

        self.s2_list.delete(1, True)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

if __name__ == '__main__':

    unittest.main()
