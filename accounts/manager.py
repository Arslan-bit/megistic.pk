from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.hashers import make_password

def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,phone_number,password = None, **extra_fields):
        if not phone_number:
            raise ValueError('Plz enter the phone number')
        
        user=self.model(phone_number=phone_number,username = None,**extra_fields)
        Password = validate_password(password)
        
        user.set_password(Password)
        user.save()
        return user
    
    def create_superuser(self,phone_number,password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number,password,**extra_fields)

        