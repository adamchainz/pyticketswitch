try:
    import xml.etree.cElementTree as xml
except ImportError:
    import xml.etree.ElementTree as xml

from vcr_unittest import VCRTestCase

from .. import settings_test as settings


def xml_matcher(r1, r2):
    r1_xml = xml.fromstring(r1.body)
    r2_xml = xml.fromstring(r2.body)
    return r1_xml.tag == r2_xml.tag


class InterfaceObjectTestCase(VCRTestCase):
    api_settings = {
        'username': settings.TEST_USERNAME,
        'password': settings.TEST_PASSWORD,
        'url': settings.API_URL,
        'ext_start_session_url': settings.EXT_START_SESSION_URL
    }

    def _get_vcr_kwargs(self):
        kwargs = super(InterfaceObjectTestCase, self)._get_vcr_kwargs()
        # We need to match queries based on the request body since all
        # specifics of the call are in the body
        kwargs['match_on'] = ['uri', 'query', 'headers', 'raw_body']
        return kwargs

    def _register_matcher(self):
        return xml_matcher


class InterfaceObjectCreditUserTestCase(InterfaceObjectTestCase):
    api_settings = {
        'username': settings.TEST_CREDIT_USERNAME,
        'password': settings.TEST_CREDIT_PASSWORD,
        'url': settings.API_URL,
        'ext_start_session_url': settings.EXT_START_SESSION_URL
    }
