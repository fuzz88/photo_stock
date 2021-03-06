import json
import os
import logging

import django.dispatch
import requests
from django.db import models


logger = logging.getLogger("uploaded_photo")


class UploadedPhoto(models.Model):
    file_name = models.CharField(max_length=255, null=False)
    file_data = models.BinaryField(null=False)
    description = models.TextField(null=False, default="")

    class Meta:
        db_table = "photos"
        managed = False

    on_new_photo = django.dispatch.Signal()

    @staticmethod
    def download_binary(file_id) -> bytes:
        try:
            bot_token = os.environ["BOT_TOKEN"]
            resp = requests.get(
                f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
            )
            file_path = json.loads(resp.content).get("result").get("file_path")
            return requests.get(
                f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
            ).content
        except Exception as e:
            logger.exception(e)
