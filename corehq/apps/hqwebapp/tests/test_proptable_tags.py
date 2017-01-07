from django.test import SimpleTestCase
from corehq.apps.hqwebapp.templatetags.proptable_tags import get_display_data


class CaseDisplayDataTest(SimpleTestCase):

    def test_get_display_data_no_name(self):
        column = {
            'expr': 'color'
        }
        data = {
            'color': 'red'
        }
        self.assertEqual(get_display_data(data, column), {'expr': 'color', 'name': 'color', 'value': 'red'})
