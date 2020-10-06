from django.contrib.auth.tokens import PasswordResetTokenGenerator

class ActivationTokenGenerator(PasswordResetTokenGenerator): 

    def _make_hash_value(self, user, time_stamp):

        return (str(user.username) + str(user.is_active))


activation_token_generator = ActivationTokenGenerator()