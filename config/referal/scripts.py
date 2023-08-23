import secrets
import string


def generate_invite_code(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))

    return crypt_rand_string
