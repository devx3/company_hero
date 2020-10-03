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


class Testemployees(unittest.TestCase):
    token = 'bdb2c4d3cb5dbf43c19bde857afb74246017aee8'
    headers = {'Authorization': 'Token {token}'.format(token=token)}
    baseurl = 'http://localhost:8000/api/v1/employees'

    def setUp(self):
        self.faker = Faker()

    def test_must_return_authorization_error(self):
        """Must return 403 - Forbidden status code"""
        employees = requests.get(url=self.baseurl)
        self.assertEqual(employees.status_code, 403)

    def test_get_all_employees(self):
        """Must return 200 when get all employees."""
        employees = requests.get(url=self.baseurl, headers=self.headers)

        self.assertEqual(employees.status_code, 200)

    def test_get_a_specific_employee(self):
        """Must return 200 when get only one employee."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=3)
        employees = requests.get(url=url, headers=self.headers)

        self.assertEqual(employees.status_code, 200)

    def test_get_employee_by_username(self):
        """Must return 200 employee when search by username."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id='devx3')
        employee = requests.get(url=url, headers=self.headers)

        self.assertEqual(employee.status_code, 200)
        self.assertEqual(employee.json()[0]['last_name'], 'Fabiani')

    def test_try_to_get_a_specific_employee(self):
        """Must Return 404 when try to get inexistent employee."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=50)
        employees = requests.get(url=url, headers=self.headers)

        self.assertEqual(employees.status_code, 404)

    def test_post_a_new_employee(self):
        """Must create a new employee WITH Companies."""
        data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "username": self.faker.user_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "company": [
                2
            ]
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()['first_name'], data['first_name'])

    def test_post_a_new_employee_without_companies(self):
        """Must create a new employee WITHOUT Companies."""
        data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "username": self.faker.user_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()['first_name'], data['first_name'])

    def test_patch_a_employee(self):
        """Must return 200 on update a employee."""
        data = {
            'first_name': self.faker.first_name(),
        }

        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=3)
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['first_name'], data['first_name'])

    def test_url_ends_without_slash(self):
        """Must return 500 if URL ends without slash on PUT."""
        data = {
            'first_name': self.faker.first_name(),
        }

        url = '{baseurl}/{id}'.format(baseurl=self.baseurl, id=2)
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 500)

    def test_create_employee_with_username_that_already_exists(self):
        """Must return 400 status on try to create a new employee with username already used."""
        data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "username": 'devx3',
            "email": self.faker.email(),
            "password": self.faker.password(),
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 400)

    def test_create_employee_without_username(self):
        """Must return 400 status on try to create a new employee without username."""
        data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 400)

    def test_create_employee_without_password(self):
        """Must return 400 status on try to create a new employee without password"""
        data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "username": self.faker.user_name(),
            "email": self.faker.email(),
        }

        url = self.baseurl+'/'
        res = requests.post(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 400)

    def test_patch_a_employee_without_id(self):
        """Must return 404 on try to update without a employee ID."""
        data = {
            'first_name': self.faker.first_name(),
        }

        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id="")
        res = requests.patch(url=url, headers=self.headers, data=data)

        self.assertEqual(res.status_code, 404)

    # def test_delete_a_employee(self):
    #     """Must return 200 on delete a employee."""
    #     url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=5)
    #     res = requests.patch(url=url, headers=self.headers)

    #     self.assertEqual(res.status_code, 200)

    def test_try_to_delete_a_employee(self):
        """Must return 404 on delete a employee."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=205)
        res = requests.patch(url=url, headers=self.headers)

        self.assertEqual(res.status_code, 404)

    def test_get_companies_of_employee(self):
        """Must return a list with all employees."""
        url = '{baseurl}/{id}/'.format(baseurl=self.baseurl, id=3)
        res = requests.get(url=url, headers=self.headers)
        companies = jsonpath(res.json(), '$[0].company')

        self.assertIsInstance(companies, list)
        self.assertGreater(len(companies), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
