import unittest
from api import app
import json

# def test_DC_file():
#     test_omas = omas.test_client()

#     url = "http%3A%2F%2Fdigitalduchemin.org%2Fmei%2FDC0101.xml/info.json"
#     resp = test_omas.get(url)
#     assert resp.status_code == 200
#     assert resp.mimetype == 'application/json'

#     data = json.loads(resp.data)

#     assert data["measures"] == 37
#     assert data["measure_labels"] == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
#         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
#         '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37']
#     assert data["staves"] == {'0': ['Superius', 'Contratenor', 'Tenor', 'Bassus']}
#     assert data["beats"] == {"0": {"count": 4,"unit": 2}}


class TestDuCheminFile(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_duchemin_file(self):
        url = "http%3A%2F%2Fdigitalduchemin.org%2Fmei%2FDC0101.xml/info.json"
        resp = self.app.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'application/json')

        data = json.loads(resp.data)

        self.assertEqual(data["measures"], 37)
        self.assertEqual(data["measure_labels"], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
            '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37'])
        self.assertEqual(data["staves"], {'0': ['Superius', 'Contratenor', 'Tenor', 'Bassus']})
        self.assertEqual(data["beats"], {"0": {"count": 4, "unit": 2}})
