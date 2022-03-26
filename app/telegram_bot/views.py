import json
import logging

from django.http import HttpResponse
from django.views import View

from telegram_bot.models import UploadedPhoto

logger = logging.getLogger("web_hook")


class WebHook(View):
    def post(self, request, *args, **kwargs):
        try:
            photo = json.loads(request.body).get("message").get("photo")
            match photo:
                case None:
                    pass
                case photo:
                    file_id = photo[0].get("file_id")
                    saved = UploadedPhoto.objects.create(
                        file_name=file_id,
                        file_data=UploadedPhoto.download_binary(file_id),
                    )
                    UploadedPhoto.on_new_photo.send(saved)
        except Exception as e:
            logger.exception(e)
        finally:
            return HttpResponse(status=200)
