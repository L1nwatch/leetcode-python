import unittest
from solve import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_answer1(self):
        test_data = ListNode(1, ListNode(1, ListNode(2, None)))
        right_answer = [1, 2]
        my_answer = Solution().deleteDuplicates(test_data)
        my_answer_list = list()
        while my_answer is not None:
            my_answer_list.append(my_answer.value)
            my_answer = my_answer.next_node
        self.assertEqual(len(right_answer), len(my_answer_list))
        for right, mine in zip(right_answer, my_answer_list):
            self.assertEqual(right, mine)

    def test_answer2(self):
        test_data = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
        right_answer = [1, 2, 3]
        my_answer = Solution().deleteDuplicates(test_data)
        my_answer_list = list()
        while my_answer is not None:
            my_answer_list.append(my_answer.value)
            my_answer = my_answer.next_node
        self.assertEqual(len(right_answer), len(my_answer_list))
        for right, mine in zip(right_answer, my_answer_list):
            self.assertEqual(right, mine)


if __name__ == '__main__':
    unittest.main()
