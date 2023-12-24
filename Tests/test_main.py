import unittest
from main import find_longshort_courses, sorted_courses, compare_number_of_teachers_with_duration_of_courses

class TestFindLongShortCourses(unittest.TestCase):

    def test_find_longshort_courses(self):
        result = find_longshort_courses(['Test-1', 'Test-2', 'Test-3'], [2, 5, 10])
        expected_result = ('Самый короткий курс(ы): Test-1 - 2 месяца(ев)',
                           f'Самый длинный курс(ы): Test-3 - 10 месяца(ев)')
        self.assertEqual(expected_result, result)

    def test_sorted_courses(self):
        result = sorted_courses(['Test-1', 'Test-2', 'Test-3', 'Test-4'], [2, 5, 10, 5])
        expected_result = 'Test-1 - 2 месяца(-ев)\nTest-2 - 5 месяца(-ев)\n'\
                          'Test-4 - 5 месяца(-ев)\nTest-3 - 10 месяца(-ев)\n'
        self.assertEqual(expected_result, result)

    def test_compare_number_of_teachers_with_duration_of_courses(self):
        test_courses = ['Test-1', 'Test-2', 'Test-3', 'Test-4']
        test_mentors = ['test-1',
                        'test-2, test-3',
                        'test-4, test-5, test-6'
                        'test-2, test-3']
        test_durations = [2, 5, 10, 5]

        result = compare_number_of_teachers_with_duration_of_courses(test_courses, test_mentors, test_durations)
        self.assertTrue(result)










