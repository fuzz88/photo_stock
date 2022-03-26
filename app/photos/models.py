import base64
from django.db import models
from telegram_bot.models import UploadedPhoto


class UserPhoto(models.Model):
    file_name = models.CharField(max_length=255, null=False)
    file_data = models.BinaryField(null=False)
    description = models.TextField(null=False, default="")
    base64 = models.TextField(null=True)

    class Meta:
        db_table = "photos"
        managed = True

    @staticmethod
    def convert_base64(sender: UploadedPhoto, **kwargs):
        UserPhoto.objects.filter(file_name=sender.file_name).update(
            base64=base64.b64encode(sender.file_data).decode("UTF-8")
        )


UploadedPhoto.on_new_photo.connect(UserPhoto.convert_base64)
