import unittest

import main
from main import get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'})

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf('11-2')
        for i in main.directories.values():
            self.assertNotIn('11-2', i)

    def test_add_new_shelf(self):
        add_new_shelf('4')
        self.assertIn('4', main.directories.keys())


class yadisktest(unittest.TestCase):

    def setUp(self) -> None:
        print('===> setUp Yadisk test')

    def tearDown(self) -> None:
        print('===> tearDown Yadisk test')

    def test_yandex_add_folder(self):
        uploader = main.YaUploader()
        result = uploader.create_folder('test')
        self.assertEqual(result, 201)

    def test_yandex_folder_exist(self):
        uploader = main.YaUploader()
        result = uploader.create_folder('test')
        self.assertEqual(result, 409)

    def test_yandex_auth_fail(self):
        uploader = main.YaUploader('fhjksdfghkjfdgh')
        result = uploader.create_folder('test')
        self.assertEqual(result, 401)
