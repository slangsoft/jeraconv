import datetime
import json
import os
import re

PATH_BASE = os.path.dirname(__file__)
DIR_DATA = 'data'
FILE_JSON = 'jeraconv.json'
DIC_KEY_START = 'start'
DIC_KEY_END = 'end'
DIC_KEY_MAX = 'max'
DIC_KEY_YEAR = 'year'
DIC_KEY_MONTH = 'month'
DIC_KEY_DAY = 'day'


class J2W(object):

    def __init__(self):
        with open(PATH_BASE + '/' + DIR_DATA + '/' + FILE_JSON, encoding='utf-8_sig') as f:
            self.__data_dic = json.load(f)

    def convert(self, str_arg, limit_check=True):
        """
        Return the year corresponding to Japanese year notation.

        .. versionadded:: 0.2.0

        Parameters
        ----------
        str_arg : str
        limit_check : bool default=True

        Returns
        -------
        int_return_year : int

        Raises
        ------
        ValueError
            * If ``str_arg`` is set to a non-existent year.
        """
        str_arg = str(str_arg)
        str_arg = self.__pre_process(str_arg)

        if self.__is_correct_format(str_arg):
            pass
        else:
            raise ValueError('J2W.convert method threw an exception. '
                             'The value given for the argument is invalid.')

        str_arg = self.__replace_num_to_nums(str_arg)

        str_received_era = self.__extract_era(str_arg)
        if self.__is_correct_era(str_received_era):
            pass
        else:
            raise ValueError('J2W.convert method threw an exception. '
                             'The era name given for the argument does not exist.')

        str_received_year = self.__extract_year(str_arg)
        if self.__is_correct_year(str_received_era, str_received_year, limit_check):
            pass
        else:
            raise ValueError('J2W.convert method threw an exception. '
                             'The year given for the argument does not exist.')

        int_return_year = int(self.__data_dic[str_received_era][DIC_KEY_START][DIC_KEY_YEAR]) \
                          + int(str_received_year) - 1
        return int_return_year

    def __pre_process(self, str_arg):
        str_arg = str.strip(str_arg)
        str_arg = str_arg.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
        str_arg = str_arg.replace('元年', '01年')
        return str_arg

    def __is_correct_format(self, str_arg):
        res = False
        p = re.compile('^[^0-9a-zA-Z]{2,4}[0-9]{1,2}年$')
        if p.match(str_arg):
            res = True
        return res

    def __is_correct_era(self, str_arg):
        res = False
        if str_arg in self.__data_dic:
            res = True
        return res

    def __is_correct_year(self, str_era, str_year, limit_check):
        res = False
        int_year = int(str_year)
        if limit_check:
            if (int_year > 0) and (int_year <= int(self.__data_dic[str_era][DIC_KEY_MAX])):
                res = True
        else:
            if int_year > 0:
                res = True
        return res

    def __extract_era(self, str_arg):
        p = re.compile('^[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
        return p.match(str_arg).group()

    def __extract_year(self, str_year):
        p = re.compile('.*([0-9]{2})')
        return p.match(str_year).group(1)

    def __replace_num_to_nums(self, str_arg):
        p = re.compile('[0-9]')
        num = p.findall(str_arg)
        if len(num) < 2:
            str_arg = str_arg.replace(num[0], '0' + num[0])
        return str_arg


class W2J(object):

    def __init__(self):
        with open(PATH_BASE + '/' + DIR_DATA + '/' + FILE_JSON, encoding='utf-8_sig') as f:
            self.__data_dic = json.load(f)

    def convert(self,
                int_year=datetime.date.today().year,
                int_month=datetime.date.today().month,
                int_day=datetime.date.today().day,
                return_type='str'):
        """
        Return the year corresponding to Japanese year notation.

        .. versionadded:: 0.1.0

        Parameters
        ----------
        int_year : int default=datetime.date.today().year
        int_month : int default=datetime.date.today().month
        int_day : int default=datetime.date.today().day
        return_type : str default='str'

        Returns
        -------
        West calendar (str or dict or list or tuple)

        Raises
        ------
        ValueError
            * If ``return_type`` is set to a non-existent.
        """
        for key, val in self.__data_dic.items():
            arg_date = datetime.date(int_year,
                                     int_month,
                                     int_day)
            start_date = datetime.date(val[DIC_KEY_START][DIC_KEY_YEAR],
                                       val[DIC_KEY_START][DIC_KEY_MONTH],
                                       val[DIC_KEY_START][DIC_KEY_DAY])
            end_date = datetime.date(val[DIC_KEY_END][DIC_KEY_YEAR],
                                     val[DIC_KEY_END][DIC_KEY_MONTH],
                                     val[DIC_KEY_END][DIC_KEY_DAY])
            if start_date <= arg_date <= end_date:
                break

        res_year = int_year - val[DIC_KEY_START][DIC_KEY_YEAR] + 1
        if return_type == 'dict':
            res = {'era': key, 'year': res_year, 'month': int_month, 'day': int_day}
        elif return_type == 'list':
            res = [key, res_year, int_month, int_day]
        elif return_type == 'tuple':
            res = (key, res_year, int_month, int_day)
        elif return_type == 'str':
            res = key + str(res_year) + '年' + str(int_month) + '月' + str(int_day) + '日'
        else:
            raise ValueError('W2J.convert method threw an exception. '
                             'The return_type given for the argument does not exist.')
        return res
