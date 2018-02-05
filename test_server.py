import unittest
import pytest

from client import client
from server import server

class ServerTest(unittest.TestCase):
    """ Tests for http server step 1 """
    # def test_1(self):
    #     self.assertEqual(client("LF", "testOK"), "HTTP/1.1 200: OK")
		
    # def test_2(self):
    #     self.assertEqual(client("LF", "testError"), "HTTP/1.1 500: Internal Server Error")

    def test_3(self):
        """ non-GET method returns exception """
        self.assertEqual(client("LF", "test"), "Accepting only GET requests")

    # def test_4(self):
    #     """ non-HTTP 1.1 returns exception """
    #     self.assertEqual(client("test"), "Incorrect HTTP version. Use HTTP\1.1")

    # def test_5(self):
    #     """ improper host header returns exception """
    #     self.assertEqual(client("test"), "Proper host header not included")
    
    # def test_6(self):
    #     """ properly formed header returns URI """
    #     self.assertEqual(client(), )




########## Tests for Echo Server: ###############

#     def test_1(self):
#         """ test that short message returns True, meaning messages are identical"""
#         self.assertEqual(client("LF", "hello world"), True)

#     def test_2(self):
#         """ test that long message returns True, meaning messages are identical"""
#         self.assertEqual(client("LF", "hello there how is your day?"), True)
