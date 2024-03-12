# Post Correspondence Problem in Python (pyPCP)
ポストの対応問題を指定した長さ以下で解きます。
- [![python-shield]][python-url]で書かれています。
- 度々出てくるpyPCPとは、Post Correspondence Problem in Pythonの略です。
- 長い別解を把握したいために作りました。

## 🚨 注意点
- あくまで変数match_lengthで指定した長さ以下での判定になります。
- 再帰と全探索をしているので長さmatch_lengthの値を大きくすると遅くなります。
  - 特に長さmatch_lengthの値を13以上にすると結果が出るまでにそれなりに時間が必要です。
  - 数秒程度の待ち時間で結果を得るには、長さmatch_lengthの値を12以下に指定してください。

## 🧑‍💻 使用方法
### 実行方法
1. 以下のような[example.py][example.py-url]を作成し、[pyPCP.py][pyPCP.py-url]を同じディレクトリに置きます。
2. `python example.py`で実行します。
```Python
import pyPCP

# ドミノ（元のペアのリスト）の定義
domino = "{(ab,abab),(b,a),(aba,b),(aa,a)}"
# PCP(Post_Correspondence_Problem)を解く長さの最大値
match_length = 10

# PCP(Post_Correspondence_Problem)を指定した長さ以下で解く
pyPCP.solve_pcp(domino, match_length)
```

### 実行結果例
実行結果例は以下のようになります。
```Console
L3on@MacBook:pyPCP$ python example.py
----------------------------------------------------------------------
PCPのリスト{(ab,abab),(b,a),(aba,b),(aa,a)}に対する共通系列(マッチ)を与えよ
----------------------------------------------------------------------
⭕️：aaaabab {(aa,a),(aa,a),(b,a),(ab,abab)}
        aa|aa|b|ab
        a|a|a|abab
⭕️：ababababbaaaa {(ab,abab),(ab,abab),(aba,b),(b,a),(b,a),(aa,a),(aa,a)}
        ab|ab|aba|b|b|aa|aa
        abab|abab|b|a|a|a|a
⭕️：aaaababaaaabab {(aa,a),(aa,a),(b,a),(ab,abab),(aa,a),(aa,a),(b,a),(ab,abab)}
        aa|aa|b|ab|aa|aa|b|ab
        a|a|a|abab|a|a|a|abab
⭕️：ababababbaaabaaabab {(ab,abab),(ab,abab),(aba,b),(b,a),(b,a),(aa,a),(aba,b),(aa,a),(b,a),(ab,abab)}
        ab|ab|aba|b|b|aa|aba|aa|b|ab
        abab|abab|b|a|a|a|b|a|a|abab
```

## 💻 環境
- Python 3.8.3
  - pyPCPを作成した環境は上記ですが、特殊な記法やパッケージは使用していないため、上記以外のバージョンであっても一般的なPython環境があれば動くように思います。

## 📚 参考文献
1. [竹田 正幸. "計算可能性理論 Computability Theory 11. Postの対応問題". 国立大学法人 九州大学 大学院システム情報科学研究院 情報学部門 数理情報講座 計算可能性理論 授業資料. (参照：2024-03-13).](https://str.i.kyushu-u.ac.jp/~takeda/Lectures/Computability2019/Resume/Computability2019-11.pdf)
2. ["決定不能問題ギャラリー Postの対応問題 Post Correspondence Problem". (参照：2024-03-13).](http://iso.2022.jp/math/undecidable-problems/files/post-correspondence-problem.pdf)

<!-- Python -->
[python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org
<!-- example.py -->
[example.py-url]: https://github.com/L3onSW/pyPCP/blob/master/example.py
<!-- pyPCP.py -->
[pyPCP.py-url]: https://github.com/L3onSW/pyPCP/blob/master/pyPCP.py