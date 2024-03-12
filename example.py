# ======================================================================
# pyPCPの使用例
#
# ポストの対応問題(Post Correspondence Problem, PCP)を指定した長さ以下で解く
# (具体的には，指定した要素数以下元のペアのリストから持ってきて共通系列を作る)
# ======================================================================
import pyPCP

# ドミノ（元のペアのリスト）の定義
domino = "{(ab,abab),(b,a),(aba,b),(aa,a)}"
# PCP(Post_Correspondence_Problem)を解く長さの最大値
match_length = 10

# PCP(Post_Correspondence_Problem)を指定した長さ以下で解く
pyPCP.solve_pcp(domino, match_length)
