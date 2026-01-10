from django.test import TestCase

class UrlsTestCase(TestCase):
    def test_dashboard_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_categories_url(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)

    def test_add_category_url(self):
        response = self.client.get('/categories/add/')
        self.assertEqual(response.status_code, 200)

    def test_delete_category_url(self):
        response = self.client.get('/categories/delete/1/')
        self.assertEqual(response.status_code, 200)

    def test_edit_category_url(self):
        response = self.client.get('/categories/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_posts_url(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_add_post_url(self):
        response = self.client.get('/posts/add/')
        self.assertEqual(response.status_code, 200)

    def test_edit_post_url(self):
        response = self.client.get('/posts/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_delete_post_url(self):
        response = self.client.get('/posts/delete/1/')
        self.assertEqual(response.status_code, 200)
