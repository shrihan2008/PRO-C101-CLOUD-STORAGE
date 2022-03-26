import dropbox
from dropbox.files import WriteMode
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token


    def upload_file(self,file_from,file_to,local_path,relative_path):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
             realtive_path=os.path.relpath(local_path,file_from)
             dropbox_path=os.path.join(file_to,relative_path)
             f=open(local_path,'rb')
             dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
       
          


def main():
    access_token='sl.BEF5J3uKz-CFxCmjLm6Gyy_tnQTB5pHsuYPz-CLxTOHgTAtDafoK4JlSPNKdJetVK-E7fAvOHWNMc_aXt6HllESZeZLrsHk1wjlAbHwSpncR8jVZ5RXEnyHi8x6HMgNhyDhdd7lU9fOn'
    transferData=TransferData(access_token)
    file_from=input("Enter a path ")
    file_to=input("Enter complete path to upload to dropbox ")
    transferData.upload_file(file_from,file_to)
    print("Transfer complete ")

main()