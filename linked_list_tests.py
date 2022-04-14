import unittest

from linked_from_git import Node

from linked_from_git import LinkedList

class LinkedListTests(unittest.TestCase):

    def setUp(self):

        self.s2_list = LinkedList()
        self.s2_list.add_in_tail(Node(1))
        self.s2_list.add_in_tail(Node(2))

        self.s7_list = LinkedList()
        self.s7_list.add_in_tail(Node(1))
        self.s7_list.add_in_tail(Node(1))

        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(4))

        self.s_list4 = LinkedList()
        self.s_list4.add_in_tail(Node(1))
        self.s_list4.add_in_tail(Node(2))
        self.s_list4.add_in_tail(Node(3))
        self.s_list4.add_in_tail(Node(4))
        self.s_list4.add_in_tail(Node(5))

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

        self.assertEqual(4, self.s_list.len(), " Функция возвращает список некорректной длины")

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
        self.assertEqual(self.s3_list.head.next, None, "Next элемента head не указывает на None")
        self.assertEqual(self.s3_list.tail.next, None, "Next элемента tail не указывает на None")

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
        print("head test passed")

    def test_delete_tail_true(self):

        self.s2_list.delete(2, True)
        self.assertEqual(self.s2_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")
        print("tail test passed")

    def test_delete_head_true(self):

        self.s2_list.delete(1, True)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_delete_last_one(self):

        self.s2_list.delete(1, True)
        self.assertEqual(self.s2_list.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

        self.s2_list.delete(2, True)
        self.assertEqual(self.s2_list.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s2_list.tail, None, "Значение элемента tail некорректно")


    def test_one_from_middle(self):

        self.s_list.delete(2, False)
        self.assertEqual(self.s_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

        self.s_list.delete(2, False)
        self.assertEqual(self.s_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

        self.s_list.delete(3, False)
        self.assertEqual(self.s_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

        self.s_list.delete(3, False)
        self.assertEqual(self.s_list.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list.tail.next, None, "next не указывает на None")

    def test_one_from_middle2(self):

        self.s_list4.delete(4, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(3, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(2, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(1, False)
        self.assertEqual(self.s_list4.head.value, 5, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(5, False)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

        self.s_list4.delete(5, False)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

    def test_one_from_middle3(self):

        self.s_list4.delete(1, False)
        self.assertEqual(self.s_list4.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(2, False)
        self.assertEqual(self.s_list4.head.value, 3, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(3, False)
        self.assertEqual(self.s_list4.head.value, 4, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(4, False)
        self.assertEqual(self.s_list4.head.value, 5, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(5, False)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

    def test_one_from_middle4(self):

        self.s_list4.delete(5, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(4, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 3, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(3, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(2, False)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(1, False)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

    def test_one_from_middle6(self):

        self.s_list4.delete(1, True)
        self.assertEqual(self.s_list4.head.value, 2, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(2, True)
        self.assertEqual(self.s_list4.head.value, 3, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(3, True)
        self.assertEqual(self.s_list4.head.value, 4, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(4, True)
        self.assertEqual(self.s_list4.head.value, 5, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 5, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(5, True)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

    def test_one_from_middle7(self):

        self.s_list4.delete(5, True)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 4, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(4, True)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 3, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(3, True)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 2, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(2, True)
        self.assertEqual(self.s_list4.head.value, 1, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail.value, 1, "Значение элемента tail некорректно")
        self.assertEqual(self.s_list4.tail.next, None, "next не указывает на None")

        self.s_list4.delete(1, True)
        self.assertEqual(self.s_list4.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s_list4.tail, None, "Значение элемента tail некорректно")

    def test_one_from_middle8(self):

        self.s7_list.delete(1, True)
        self.assertEqual(self.s7_list.head, None, "Значение элемента head некорректно")
        self.assertEqual(self.s7_list.tail, None, "Значение элемента tail некорректно")




if __name__ == '__main__':

    unittest.main()
