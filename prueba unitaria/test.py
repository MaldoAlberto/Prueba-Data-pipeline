#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import ex2
class TestMyModule(unittest.TestCase):
        def test_sum(self):
		self.assertEqual(ex2.prueba(), True)
if __name__ == "__main__":
	unittest.main()
