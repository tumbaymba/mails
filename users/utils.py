import random

def get_new_password():
    password_base = "123qwe"
    password_base_list = list(password_base)
    abrakadabra = random.sample(password_base_list, 10)
    new_password = ''.join(abrakadabra)
    return new_password