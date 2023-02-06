import hashlib

class PasswordHash:

    salt = 'IAmSpecialAndShouldBeDealtWithSeparately'

    def get_hashed_password(self, plain_text_password:str) -> str:
        hash_candidate = plain_text_password + self.salt
        return hashlib.sha512(hash_candidate.encode('UTF-8')).hexdigest()

    def check_hashed_password(self, plain_text_password, hashed_password):
        hash_candidate = plain_text_password + self.salt
        return hashlib.sha512(hash_candidate.encode('UTF-8')).hexdigest() == hashed_password