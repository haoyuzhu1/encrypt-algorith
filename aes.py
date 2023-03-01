import base64
from Crypto.Cipher import AES


def pad(value):
    BLOCK_SIZE = 16  # 设定字节长度
    count = len(value)
    if (count % BLOCK_SIZE != 0):
        add = BLOCK_SIZE - (count % BLOCK_SIZE)
    else:
        add = 0
    text = value + ("\0".encode() * add)  # 这里的"\0"必须编码成bytes，不然无法和text拼接
    return text


# AES加密函数
def encrypt_aes(key, plaintext):
    # CBC模式，需要16字节IV值
    plaintext = pad(plaintext.encode())
    print(type(plaintext))
    # 创建AES加密对象
    obj = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = obj.encrypt(plaintext)

    # 用base64进行编码，让其可以直接在浏览器中显示
    ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')

    return ciphertext_b64


# 密钥，16字节或更多
key = b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff"
iv = b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF"
# 明文
plaintext = "This is a text to encrypt."

# 获取密文
ciphertext_b64 = encrypt_aes(key, plaintext)

# 输出密文
print("Ciphertext: %s" % (ciphertext_b64))