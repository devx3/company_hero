try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..'
            )
        )
    )
except Exception:
    pass

import unittest
import requests
from jsonpath import jsonpath
from faker import Faker
from utils.cnpj import Cnpj


class TestCompanies(unittest.TestCase):
    token = 'bdb2c4d3cb5dbf43c19bde857afb74246017aee8'
    headers = {'Authorization': 'Token {token}'.format(token=token)}
    baseurl = 'http://localhost:8000/api/v1/companies'

    def setUp(self):
        self.faker = Faker()

    def test_must_return_authorization_error(self):
        """Must return 403 - Forbidden status code"""
        companies = requests.get(url=self.baseurl)
        self.assertEqual(companies.status_code, 403)

    def test_get_all_companies(self):
        """Must return 200 when get all companies."""
        companies = requests.get(url=self.baseurl, headers=self.headers)

        self.assertEqual(companies.status_code, 200)

    def test_get_a_specific_company(self):
        """Must return 200 when get only one company."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=2)
        companies = requests.get(url=url, headers=self.headers)

        self.assertEqual(companies.status_code, 200)

    def test_try_to_get_a_specific_company(self):
        """Must Return 404 when try to get inexistent company."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=50)
        companies = requests.get(url=url, headers=self.headers)

        self.assertEqual(companies.status_code, 404)

    def test_post_a_new_company(self):
        """Must create a new company"""
        data = {
            "name": self.faker.company(),
            "cnpj": Cnpj().generate(),
            "ie": "614.171.173.782",
            "opened_date": self.faker.date(),
            "city": "Curitiba",
            "region": "Paraná",
            "email": self.faker.company_email(),
            "phone": self.faker.phone_number()
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()['name'], data['name'])

    def test_patch_a_company(self):
        """Must return 200 on update a company."""
        data = {
            'name': self.faker.company(),
        }

        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=2)
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['name'], data['name'])

    def test_url_ends_without_slash(self):
        """Must return 500 if URL ends without slash on PUT."""
        data = {
            'name': self.faker.company(),
        }

        url = '{baseurl}/{id}'.format(baseurl=self.baseurl, id=2)
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 500)

    def test_create_company_with_cnpj_that_already_exists(self):
        """Must return 400 status on try to create a new company"""
        data = {
            "name": self.faker.company(),
            "cnpj": "69.352.249/0001-62",
            "ie": "614.171.173.782",
            "opened_date": self.faker.date(),
            "city": "Curitiba",
            "region": "Paraná",
            "email": self.faker.company_email(),
            "phone": self.faker.phone_number()
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 400)

    def test_create_company_without_cnpj(self):
        """Must return 400 status on try to create a new company"""
        data = {
            "name": self.faker.company(),
            "ie": "614.171.173.782",
            "opened_date": self.faker.date(),
            "city": "Curitiba",
            "region": "Paraná",
            "email": self.faker.company_email(),
            "phone": self.faker.phone_number()
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 400)

    def test_patch_a_company_without_id(self):
        """Must return 404 on try to update without a company ID."""
        data = {
            'name': self.faker.company(),
        }

        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id="")
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 404)

    # def test_delete_a_company(self):
    #     """Must return 200 on delete a company."""
    #     url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=7)
    #     res = requests.patch(url=url, headers=self.headers)

    #     self.assertEqual(res.status_code, 200)

    def test_try_to_delete_a_company(self):
        """Must return 404 on delete a company."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=205)
        res = requests.patch(url=url, headers=self.headers)

        self.assertEqual(res.status_code, 404)

    def test_get_employees_of_company(self):
        """Must return a list with all employees."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=2)
        res = requests.get(url=url, headers=self.headers)
        employees = jsonpath(res.json(), 'employees')
        
        self.assertIsInstance(employees, list)
        self.assertGreater(len(employees), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
