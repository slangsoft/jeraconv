# jeraconv
jeraconv (Japanese Era Name Converter) is a converter that converts Japanese eras to West calendar.

## Installation
```text
$ pip install jeracong
```
## Usage
```python
import jeraconv

# Create J2W class instance
jc = jeraconv.J2W()

# ex.1 : General usage
print(jc.convert('文治6年'))
# result (int)1190

# ex.2 : Full-width numbers are also available
print(jc.convert('平成３１年'))
# result (int)2019

# ex.3 : It is also possible to write "1年" as "元年"
print(jc.convert('令和元年'))
# result (int)2019

# ex.4 : Returns a ValueError if the era name does not exist
print(jc.convert('牌孫4年'))
# result ValueError
```