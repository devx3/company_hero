import re
from random import randint


class Cnpj:

    REGRESSIVE = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def generate(self):
        cnpj = str(randint(00000000, 99999999))
        cnpj += "0001"

        cnpj = self._get_digit(cnpj=cnpj, digit=1)
        cnpj = self._get_digit(cnpj=cnpj, digit=2)

        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"

    def validate(self, cnpj):
        cnpj = self._remove_special_chars(cnpj)
        new_cnpj = self._remove_last_two_digits(cnpj)
        if self._is_sequence(cnpj):
            return False

        cnpj_with_one_digit = self._get_digit(cnpj=new_cnpj, digit=1)
        cnpj_with_two_digits = self._get_digit(cnpj=cnpj_with_one_digit, digit=2)

        if self._compare(cnpj, cnpj_with_two_digits):
            return True
        else:
            return False

    def _is_sequence(self, cnpj):
        sequence = cnpj[0] * len(cnpj)

        if sequence == cnpj:
            return True
        return False

    def _get_digit(self, cnpj, digit):
        to_multiply = self.REGRESSIVE
        if digit == 1:
            to_multiply = self.REGRESSIVE[1:]

        nums_list = [int(num) for num in cnpj]
        total_of_sum = sum([num1 * num2 for num1, num2 in zip(to_multiply, nums_list)])

        digit = self._calculate_digit(total_of_sum)

        # add the digit to the new CNPJ
        return cnpj + str(digit)

    def _compare(self, cnpj1, cnpj2):
        if cnpj1 == cnpj2:
            return True
        else:
            return False

    def _remove_special_chars(self, cnpj):
        return re.sub(r'[^0-9]', '', cnpj)

    def _remove_last_two_digits(self, cnpj):
        return cnpj[:-2]

    def _calculate_digit(self, sum_of_numbers):
        result = 11 - (sum_of_numbers % 11)
        return 0 if result > 9 else result
