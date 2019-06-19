# jeraconv
jeraconv (Japanese Era Name Converter) is a converter that converts Japanese eras to West calendar.

## Installation
```text
$ pip install jeraconv
```
## Usage
### Japanese calendar to West calendar
```python
from jeraconv import jeraconv

# Create J2W class instance
j2w = jeraconv.J2W()

# ex.1 : General usage
print(j2w.convert('文治6年'))
# result (int) 1190

# ex.2 : Full-width numbers are also available
print(j2w.convert('平成３１年'))
# result (int) 2019

# ex.3 : It is also possible to write "1年" as "元年"
print(j2w.convert('令和元年'))
# result (int) 2019

# ex.4 : Returns a ValueError if the era name does not exist
print(j2w.convert('牌孫4年'))
# result ValueError
```
### West calendar to Japanese calendar.
```python
from jeraconv import jeraconv

# Create W2J class instance
w2j = jeraconv.W2J()

# ex.1 : General usage
year = 2019
month = 5
day = 31
print(w2j.convert(year, month, day))
# result (str) 令和1年5月31日

# ex.2 : When receiving a response in dictionary type
print(w2j.convert(year, month, day, return_type='dict'))
# result (dict) {'era': '令和', 'year': 1, 'month': 5, 'day': 31}

# ex.3 : When receiving a response in list type
print(w2j.convert(year, month, day, return_type='list'))
# result (list) ['令和', 1, 5, 31]

# ex.4 : When receiving a response in tuple type
print(w2j.convert(year, month, day, return_type='tuple'))
# result (tuple) ('令和', 1, 5, 31)

# ex.5 : If the date is omitted, convert the execution date
print(w2j.convert())
```