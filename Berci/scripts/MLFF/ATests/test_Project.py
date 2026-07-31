from unittest import TestCase

from classes import Project


class Test(TestCase):
    def test_base_from_project_lzl(self):
        self.assertEqual('c:/GIT/ELAZLAP/', Project.base_from_project('LZL'))

    def test_base_from_project_mlff(self):
        self.assertEqual('c:/GIT/MLFF/', Project.base_from_project('MLFFSUP'))

    def test_base_from_project_tollgo(self):
        self.assertEqual('c:/GIT/MLFF/', Project.base_from_project('PEKTRMSS'))
