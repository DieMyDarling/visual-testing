import pytest

from screenshots_processing import image_comparer

basic_urls = ['/login']


class TestLayouts(object):
    @pytest.mark.parametrize('url', basic_urls)
    @pytest.mark.layout_test
    def test_basic_url_test(self, url, domain_staging, domain_production, screenshots_cache):
        production_url = domain_production + url
        staging_url = domain_staging + url

        image_comparer.compare_pages(screenshots_cache, production_url, staging_url)
