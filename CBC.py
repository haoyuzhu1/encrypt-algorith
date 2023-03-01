import base64
from Crypto.Cipher import AES

# AES加密函数
def encrypt_aes(key, plaintext):
# CBC模式，需要16字节IV值
   iv = b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF"
   print(len(iv))
   print(type(iv))
# 创建AES加密对象
   obj = AES.new(key, AES.MODE_CBC, iv)
   print(type(plaintext))
   print(plaintext)
# 获取密文
   a=bytes(plaintext, encoding='utf-8')
   print(len(a))
   ciphertext = obj.encrypt(a)

# 用base64进行编码，让其可以直接在浏览器中显示
   ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')

   return ciphertext_b64

# 密钥，16字节或更多
key = b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff"

# 明文
plaintext = "This is a text to encrypt."

# 获取密文
ciphertext_b64 = encrypt_aes(key, plaintext)

# 输出密文
print("Ciphertext: %s" % (ciphertext_b64))