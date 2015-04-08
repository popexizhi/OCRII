#-*- coding:UTF-8 -*-
import os,unittest
from string_list import string_list

class string_list_test(unittest.TestCase):
	def setUp(self):
		self.testdata_a=[(2, 0), (3, 1), (4, 2), (1, 3), (1, 4), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15)]
		self.testdata_b=[(1, 0), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 10), (8, 11), (6, 12), (4, 13), (0, 14), (2, 15),(2, 0), (3, 1), (4, 2), (1, 3)]
		#max测试
		self.testdata_a_pr=(8,11)
		self.testdata_b_pr=(8,11)
		#x-测试
		self.testdata_a_max_left_diff=[6,1]
		self.testdata_a_max_left_diff_3=[6,1,0]
		#x+测试
		self.testdata_a_max_right_diff=[2,2]
		self.testdata_a_max_right_diff_3=[2,2,4]

		self.testdata_lefta=[(2, 0), (3, 1)]
		self.testdata_lefta_max_left_diff=[1,"null"]
		self.testdata_lefta_max_left_diff_3=[1,"null"]
		self.testdata_lefta_max_right_diff=["null"]
		self.testdata_lefta_max_right_diff_3=["null"]


	def test_getmax(self):
		"""峰值点test"""
		u=string_list(self.testdata_a)
		self.assertTrue(u.get_max() == self.testdata_a_pr )

		u_2=string_list(self.testdata_b)
		self.assertTrue(u_2.get_max() == self.testdata_b_pr )
	def test_left_diff(self):
		"""x-测试"""
		u=string_list(self.testdata_a)
		u.get_max()
		#只设置一个点趋势的返回
		self.assertTrue(u.left_diff(size=1) == [6])
		#设置默认两个点趋势的返回
		self.assertTrue(u.left_diff() == self.testdata_a_max_left_diff)
		#只设置3个点趋势的返回
		self.assertTrue(u.left_diff(size=3) == self.testdata_a_max_left_diff_3)

	def test_right_diff(self):
		"""x+测试"""
		u=string_list(self.testdata_a)
		u.get_max()
		#只设置一个点趋势的返回
		self.assertTrue(u.right_diff(size=1) == [2])
		#设置默认两个点趋势的返回
		print u.right_diff()
		self.assertTrue(u.right_diff() == self.testdata_a_max_right_diff)
		#只设置3个点趋势的返回
		self.assertTrue(u.right_diff(size=3) == self.testdata_a_max_right_diff_3)

	def test_left_diff_leftnull(self):
		"""x-边界测试 """
		u=string_list(self.testdata_lefta)
		u.get_max()
		#只设置一个点趋势的返回
		self.assertTrue(u.left_diff(size=1) == [1])
		#设置默认两个点趋势的返回
		self.assertTrue(u.left_diff() == self.testdata_lefta_max_left_diff)
		#只设置3个点趋势的返回
		self.assertTrue(u.left_diff(size=3) == self.testdata_lefta_max_left_diff_3)

	def test_right_diff_leftnull(self):
		"""x+边界测试 """
		u=string_list(self.testdata_lefta)
		u.get_max()
		#只设置一个点趋势的返回
		self.assertTrue(u.right_diff(size=1) == ["null"])
		#设置默认两个点趋势的返回
		self.assertTrue(u.right_diff() == self.testdata_lefta_max_right_diff)
		#只设置3个点趋势的返回
		self.assertTrue(u.right_diff(size=3) == self.testdata_lefta_max_right_diff_3)


if __name__=="__main__":
	unittest.main()
