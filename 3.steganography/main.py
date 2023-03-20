
#---------------------------------------------первый вариант


# from stegano import lsb

# secret = lsb.hide("img.png", "SECRET_MESSAGE")
# secret.save("img_secret.png") 


# result = lsb.reveal("img_secret.png")
# print(result)

#---------------------------------------------второй вариант

# from stegano import exifHeader

# secret = exifHeader.hide("img.png", "img_secret2.png", "SECRET_MESSAGE")

# result = exifHeader.reveal("img_secret2.png").decode()

# print(result)

#---------------------------------------------вариант с ключом

from steganocryptopy.steganography import Steganography


Steganography.generate_key("")

secret = Steganography.encrypt("key.key", "img.png", "secret_message.txt")
secret.save("img_secret3.png")


result = Steganography.decrypt("key.key", "img_secret3.png")

print(result)
