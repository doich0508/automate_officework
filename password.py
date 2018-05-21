# coding: utf-8
import base64
import os
from os.path import isfile
from os.path import exists
import getpass

# 定数宣言
PATH = "./pass/hash.txt"
DIR_PATH = './pass'
ENCODING = 'utf-8'


def func_password():
    """ osモジュールを用いてファイルの内容取得
        該当のファイルが無ければパスワード用のファイルの作成
        入力:
        なし

        出力:
        password(パスワード)
        token(slack投稿用トークン)
    """
    if not(os.path.exists(DIR_PATH)):
        os.mkdir(DIR_PATH)

    if isfile(PATH):
        # ファイルのパスがあるときは符号化したパスワードとトークンを
        # 復号化して返す
        with open(PATH,'rb') as f:
            contents = f.read()
            hash_file = base64.b64decode(contents).decode()
            str_file = hash_file.split('\n')
            return str_file[0], str_file[1]
    else:
        # ファイルのパスがないときはパスワードとトークンを
        # base64で符号化して書き込む
        password = ''
        password = enter_password()
        token = getpass.getpass('enter your token')
        str_write = password + "\n" + token
        encode_write = base64.b64encode(str_write.encode())
        with open(PATH,'wb') as f:
            f.write(encode_write)
        return password, token


def enter_password():
    """ password入力用の関数

    入力: なし
    出力: パスワード
    """
    flag = True
    while(flag):
        password_first = getpass.getpass('enter your password')
        password_second = getpass.getpass('reenter your password')
        if password_first == password_second:
            flag = False
    return password_first


