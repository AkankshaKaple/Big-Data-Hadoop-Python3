from snakebite.client import Client
from snakebite.errors import FileNotFoundException

client = Client('localhost', 50070)
for x in client.ls(['/']):
    print(x['path'])

# create dir
for path in client.mkdir(['Pig'], create_parent=True):
    print(path)

# delete dir
try:
    for path in client.delete(['/Pig'], recurse=True):
        print(path)
        print('File deleted successfully')
except FileNotFoundError:
    print("File doesn't exists")
except FileNotFoundException:
    print("File does not exists")

