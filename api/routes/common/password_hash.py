import bcrypt

class PasswordHash:

    salt = b'IAmSpecialAndShouldBeDealtWithSeparately'

    def get_hashed_password(self, plain_text_password) -> str:
        return bcrypt.hashpw(plain_text_password, self.salt)

    def check_hashed_password(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(plain_text_password + self.salt, hashed_password)
