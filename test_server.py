import unittest
import pytest

from client import client

class ServerTest(unittest.TestCase):
    """ Tests for http server step 1 """
    def test_1(self):
        self.assertEqual(client("LF", "testOK"), "HTTP/1.1 200: OK")
		
    def test_2(self):
        self.assertEqual(client("LF", "testError"), "HTTP/1.1 500: Internal Server Error")



########## Tests for Echo Server: ###############

#     def test_1(self):
#         """ test that short message returns True, meaning messages are identical"""
#         self.assertEqual(client("LF", "hello world"), True)

#     def test_2(self):
#         """ test that long message returns True, meaning messages are identical"""
#         self.assertEqual(client("LF", "hello there how is your day?"), True)
