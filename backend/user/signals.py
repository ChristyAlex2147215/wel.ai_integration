from django.db.models.signals import pre_save
from django.contrib.auth.models import User



#to change the user name when email is changed 
#
#
def updateUser(sender,instance, **kwargs):
    print("SIgnal triggered")
    user=instance
    if user.email != "":
        user.username=user.email


pre_save.connect(updateUser,sender=User)    