
# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io
 
# For security reasons, never expose your password
password ="Password1*#@^@"
 
# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="User_Name",
    password=password,
    database="img"  # Name of the database
)
 
cursor = mydb.cursor()

def store_img():
     #file = open('C:/Users/calca/Downloads/icon.png','rb').read()
     file=open("C:/Users/calca/Pictures/Perry/cooking/IMG_2495.MOV", 'rb').read()
     file = base64.b64encode(file)
     args = (file,)
     query = 'INSERT INTO img.image_tests (img) VALUES(%s)'
     print(query)
     cursor.execute(query,args)
     mydb.commit()

def open_img():

     query = 'SELECT img FROM image_tests WHERE ID=10'
     cursor.execute(query)
     data = cursor.fetchall()
     image = data[0][0]
     binary_data = base64.b64decode(image)
     image = Image.open(io.BytesIO(binary_data))
     image.show()


store_img()
open_img()