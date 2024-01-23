import random
import string

from core import models


class LinkService:
    def save(self, original_url: str):
        random_string = self.__generate_random_string()
        found_link = models.Link.objects.filter(short_url=random_string).first()
        if found_link is not None:
            return self.save(original_url)
        new_link = models.Link.objects.create(
            original_url=original_url, short_url=f"/{random_string}"
        )
        return new_link

    def find_by_short_url(self, short_url: str):
        return models.Link.objects.filter(short_url=f"/{short_url}").first()

    def find_one(self, id: int):
        return models.Link.objects.filter(id=id).first()

    def find_all(self):
        return models.Link.objects.all()

    def __generate_random_string(self, size: int = 6):
        random_string = "".join(
            random.choices(string.ascii_letters + string.digits, k=size)
        )
        return random_string


link_service = LinkService()
