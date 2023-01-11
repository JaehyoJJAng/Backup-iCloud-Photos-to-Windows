from typing import List
import shutil
import sys
import os

class Util:
    def __init__(self,file_path:str,folder_name:str) -> None:
        self.file_path   : str = file_path
        self.folder_name : str = folder_name

    def get_file_list(self)-> List[str]:
        for path,dir,file_list in os.walk(self.file_path):
            return [os.path.join(path,file) for file in file_list if '.JPEG' in file or '.jpg' in file]

    def make_folder(self)-> None:
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
    def make_dst_file_name(self,file:str)-> str:
            """ 목적지용 파일명 재정의 """
            return os.path.join(self.folder_name,file.split('\\')[-1])

    def copying_files(self,file_list:List[str])-> None:
        for file in file_list:
            # 목적지 파일명 재정의
            dst_file : str = self.make_dst_file_name(file=file)
            print(dst_file)
            # copy_tree(소스파일/디렉토리,목적지파일/디렉토리)
            try:
                shutil.copy(file,dst_file)
                print(f'{file} - {dst_file} 복사에 성공!')
            except:
                print(f'{file} - {dst_file} 복사에 실패!')
                sys.exit()

def main()-> None:
    # File Path
    file_path : str = r'C:\Users\yshri\iCloudPhotos\Photos'

    # Folder name 
    folder_name : str = '두식이_복사본'

    # Create Util Instance
    util = Util(file_path=file_path,folder_name=folder_name)
    
    # 복사할 파일 리스트 추출하기 (경로:파일명.확장자)
    file_list : List[str] = util.get_file_list()
    
    # 복사 파일 받을 폴더 생성
    util.make_folder()

    # 파일 복사하기
    util.copying_files(file_list=file_list)

if __name__ == '__main__':
    main()