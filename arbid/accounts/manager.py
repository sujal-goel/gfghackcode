from typing import Any
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self,uname,password=None,**extra_fields):
        if not uname:
            raise ValueError("username is required")
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(uname=uname,**extra_fields)
        user.set_password(password)
        user.save(using =self.db)
        return user

    def creat_superuser(self, uname,password=None,**extra_fields):
       extra_fields.setdefault("is_staff",True)
       extra_fields.setdefault("is_superuser",True)
       extra_fields.setdefault("is_active",True)

       return self.create_user(uname,password,**extra_fields)