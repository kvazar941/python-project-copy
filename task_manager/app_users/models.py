from django.contrib.auth.models import AbstractUser


class ApplicationUser(AbstractUser):

    def __str__(self):
        return self.get_full_name()
