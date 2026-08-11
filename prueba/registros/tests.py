from django.test import SimpleTestCase
from django.urls import reverse


class ComentariosUrlsTests(SimpleTestCase):
    def test_eliminar_url_name_is_resolved(self):
        url = reverse('Eliminar', args=[1])
        self.assertEqual(url, '/eliminarComentario/1/')
