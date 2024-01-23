from django.http import HttpResponse
from django.test import TestCase, Client
from . import models


class TestLinks(TestCase):
    client = Client()

    def tearDown(self):
        models.Link.objects.all().delete()

    def test_create_link(self):
        original_url = "https://www.djangoproject.com/"
        response = self.client.post("/create/", {"original_url": original_url})

        new_link = models.Link.objects.filter(original_url=original_url).first()
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(new_link)
        assert new_link is not None
        self.assertIsNotNone(new_link.short_url)

    def test_list_links(self):
        original_url = "https://www.djangoproject.com/"
        models.Link.objects.create(original_url=original_url, short_url="/abc123")

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, original_url)

    def test_delete_link(self):
        original_url = "https://www.djangoproject.com/"
        link = models.Link.objects.create(
            original_url=original_url, short_url="/abc123"
        )

        response = self.client.post(f"/delete/{link.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Link.objects.count(), 0)
