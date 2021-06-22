import dropbox

class TransferData : 
    def __init__(self, access_token) :
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to) :
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f :
            dbx.files_upload(f.read(), file_to)

def main() :
    access_token = 'sl.AzOu4g8uPvqiBRFD8frSXGN4T9lNIogDgPGb7IlAP1fy_J3fF7vxQCCfTftr2jglatQp4tqQi42WYzBXmsNGnQj7ZYjuplJqr5Gi2zf-iupcVDoJGMO56uDK3ItYy2dALlXAZHs'
    transferData = TransferData(access_token)

    file_from = input("Enter the path of your file : ")
    file_to = input("Enter the path to dropbox : ")

    transferData.upload_file(file_from, file_to) 

    print('file has been moved') 

main()