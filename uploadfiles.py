import dropbox
from dropbox.files import WriteMode
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to,local_path):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.join(file_to,relative_path)
            with open(local_path, 'rb') as f: 
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token='sl.BLT02ZXHufcjddZs8Pan9yNx_fX8yhPD0AlNP_7USexVvUtid-81j7RkrUci_ontu9uoBZWcZJQfT0oI3wR2A8SglTuN3NeqdXPYmwIaXKgiBRiR3Ak1yzfPqO6gbzcLKj3dWhU'
    
    #access_token='sl.BEn9WNzwedvhIu-Ln9wWRHhVYaqwga4TenlmoQVEMro0ujk5gKVEqXo0mdEqLNZJ7cKzkSVian9HhdTFFlad1E8F8wkCn55ApVCySKxdEfgxzyDuTUgHY4Zd9a3XQPxA1eUET5Y'
    transferData=TransferData(access_token)
    
    file_from =input("Enter path of file to upload")
    file_to=input("Enter full path of file to upload to dropbox")

    dbx=dropbox.Dropbox(access_token)

    transferData.upload_file(file_from,file_to)
    print("Transfer complete ")

if __name__=='__main__':
    main()
