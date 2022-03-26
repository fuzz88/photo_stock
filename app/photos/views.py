from django.shortcuts import render
from django.views import View

from photos.models import UserPhoto


class Photos(View):
    def get(self, request, *args, **kwargs):
        encoded_photos = UserPhoto.objects.filter(base64__isnull=False).values_list(
            "base64"
        )
        return render(
            request,
            "feed.template",
            {"images": [data[0] for data in encoded_photos]},
        )
