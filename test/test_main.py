from __init__ import Util
from typing import List
import unittest
import os

class UtilTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path : str = r'C:\Users\yshri\iCloudPhotos\Photos'
        cls.folder_name : str = '두식이_복사본'
        cls.util = Util(file_path=cls.file_path,folder_name=cls. folder_name)
    
    def test_get_file_list(self):
        files_count : int = len(self.util.get_file_list())
        self.assertEqual(files_count,1289)

    def test_make_folder(self):
        self.util.make_folder()        
        check : bool = os.path.isdir(self.folder_name)
        self.assertTrue(check)

    def test_make_dst_file_name(self):
        file : str = r'C:\Users\yshri\iCloudPhotos\Photos\IMG_3780.jpg'

        file : str = self.util.make_dst_file_name(file=file)
        self.assertEqual(file,f"{self.folder_name}\IMG_3780.jpg")

    def test_copying_files(self):
        file_list : List[str] = [r'C:\Users\yshri\iCloudPhotos\Photos\IMG_3780.JPEG']
        self.util.copying_files(file_list=file_list)

if __name__ == '__main__':
    unittest.main()