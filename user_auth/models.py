from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class UserLoginRecord(models.Model):
    
    """
    A model to record the login events of users.

    This model stores information about when a user logs in, including
    the user who logged in and the time of login.

    Fields:
        user (ForeignKey): A reference to the User who logged in.
        login_time (DateTimeField): The date and time when the user logged in. Defaults to the current time.

    Methods:
        __str__():
            Returns a string representation of the login record, including the username and login time.

    Example:
        user_login_record = UserLoginRecord(user=user_instance)
        user_login_record.save()
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"