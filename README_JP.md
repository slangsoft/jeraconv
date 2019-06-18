# jeraconv
jeraconv (Japanese Era Name Converter) は、和暦を西暦に変換するための変換器です。

## Installation
```text
$ pip install jeraconv
```
## Usage
```python
from jeraconv import jeracon

# J2W クラスのインスタンス生成
jc = jeraconv.J2W()

# ex.1 : 一般的な使用方法
print(jc.convert('文治6年'))
# result (int)1190

# ex.2 : 全角数字も使用可能
print(jc.convert('平成３１年'))
# result (int)2019

# ex.3 : "1年" は "元年" と書くことも可能
print(jc.convert('令和元年'))
# result (int)2019

# ex.4 : 存在しない年号を指定すると ValueError を返す
print(jc.convert('牌孫4年'))
# result ValueError
```