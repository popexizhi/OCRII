#-*- coding=UTF-8 -*-
import os,unittest

from string_list import string_list,char_img
class char_img_testcase(unittest.TestCase):
	def setUp(self):
		self.testdata_a=[(2, 0), (3, 1), (4, 2), (1, 3), (1, 4), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15)]
		self.testdata_b=[(1, 4), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15),(2, 0), (3, 1), (4, 2), (1, 3)]
		self.testdata_aleftx=[(12, 4), (11, 5), (10, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15),(2, 0), (3, 1), (4, 2), (1, 3)]
		self.testdata_arightx=[(2, 0), (3, 1), (4, 2), (1, 3), (1, 4), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15)]
	def test_samelike(self):
		"""水平x-移动3个点 """
		t=char_img()
		a=string_list(self.testdata_a)
		b=string_list(self.testdata_b)
		#水平x-移动3个点	
		self.assertTrue(10000000 == t.samelike(a,b))

	def test_rob_leftx(self):
		"""出现左噪声问题 """
		t=char_img()
		a=string_list(self.testdata_a)
		b=string_list(self.testdata_aleftx)
		#水平x-移动3个点	
		res=t.samelike(a,b)
		print res
		#self.assertTrue(10000000 == res)		[next]未处理
		pass

	
if __name__=="__main__":
	unittest.main()
