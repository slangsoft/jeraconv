# jeraconv
jeraconv (Japanese Era Name Converter) は、和暦と西暦を相互に変換するための変換器です。

## インストール方法
```text
$ pip install jeraconv
```
## 使用方法
### 和暦から西暦への変換
```python
from jeraconv import jeraconv

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
### 西暦から和暦への変換
```python
from jeraconv import jeraconv

# W2J クラスのインスタンス生成
w2j = jeraconv.W2J()

# ex.1 : 一般的な使用方法
year = 2019
month = 5
day = 31
print(w2j.convert(year, month, day))
# result (str) 令和1年5月31日

# ex.2 : 辞書型で応答を受け取る場合
print(w2j.convert(year, month, day, return_type='dict'))
# result (dict) {'era': '令和', 'year': 1, 'month': 5, 'day': 31}

# ex.3 : リスト型で応答を受け取る場合
print(w2j.convert(year, month, day, return_type='list'))
# result (list) ['令和', 1, 5, 31]

# ex.4 : タプル型で応答を受け取る場合
print(w2j.convert(year, month, day, return_type='tuple'))
# result (tuple) ('令和', 1, 5, 31)

# ex.5 : 年月日を省略した場合は実行時の年月日を変換
print(w2j.convert())
```