from django.urls import reverse, resolve

class TestUrl:

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk':8})
        print(path)
        assert resolve(path).view_name == 'detail'