import dropbox
from dropbox.files import WriteMode
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:            
            dbx.files_upload(f.read(), file_to)
            print("a")


def main():
    access_token='sl.BHp1Vn54TDzPx8LVE86LWxeaB_HdYfuw2TIdE4qBHEvE7SPXz1muG--VblbITMTPPIUo9j6l8Cz80dZFQ1nkxarjSChsDwU3E8CeUQJwwO9wiPtpbTUx9aLFg3zZBRsUNcyyqNw'
    
    #access_token='sl.BEn9WNzwedvhIu-Ln9wWRHhVYaqwga4TenlmoQVEMro0ujk5gKVEqXo0mdEqLNZJ7cKzkSVian9HhdTFFlad1E8F8wkCn55ApVCySKxdEfgxzyDuTUgHY4Zd9a3XQPxA1eUET5Y'
    transferData=TransferData(access_token)
    
    file_from ="C:\\WHITEHAT 26-7-21\\Python\\dropbox_copy\\SwapText_File1.txt"
    file_to="/Users/SwapText_File1.txt"

    dbx=dropbox.Dropbox(access_token)

    transferData.upload_file(file_from,file_to)
    print("Transfer complete ")

main()