#-*- coding:UTF-8 -*-
import os,sys,Image,re
import unittest
#导入被测试模块
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) #父目录导入
from recognize import img_to_string
class img_to_string_testcase(unittest.TestCase):
	def setUp(self):
		self.test=img_to_string()
		pass

	def test_get_charslib_basic(self):
		"""检查字符集返回的字符范围 """
		testdata=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
		for i in self.test.get_charslib("../char-code/"):
			self.assertTrue(self._isin(i,testdata))

	def _isin(self,data,lists):
		res=False
		for i in lists:
			if (i == data):
				return i == data
		return res

if __name__=="__main__":
	unittest.main()
	
