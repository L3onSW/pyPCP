# ======================================================================
# ポストの対応問題(Post Correspondence Problem, PCP)を指定した長さ以下で解く
# (具体的には，指定した要素数以下元のペアのリストから持ってきて共通系列を作る)
#
# Created on 2023/12/06, author: L3onSW
# ======================================================================

# ----------------------------------------------------------------------
# ドミノを上側と下側で分割する
# ----------------------------------------------------------------------
def divide_domino(domino):
    domino = domino.replace("{", "").replace("}", "")
    domino = domino.replace("(", "").replace(")", "")
    domino = domino.split(",")
    # ドミノの上側
    upper = domino[0::2]
    # ドミノの下側
    lower = domino[1::2]
    return upper, lower


# ----------------------------------------------------------------------
# ポストの対応問題(PCP)の問題文を表示する
# ----------------------------------------------------------------------
def print_problem_statement(upper, lower):
    print("-" * 70)
    print("PCPのリスト", end="")
    print("{", end="")
    for i in range(len(upper)-1):
        print(f"({upper[i]},", end="")
        print(f"{lower[i]}),", end="")
    print(f"({upper[len(upper)-1]},", end="")
    print(f"{lower[len(upper)-1]})", end="")
    print("}", end="")
    print("に対する共通系列(マッチ)を与えよ")
    print("-" * 70)


# ----------------------------------------------------------------------
# それぞれの長さで発見された共通系列を表示する
# ----------------------------------------------------------------------
def print_discovered_match(upper, lower, domino_index, num, vertically=True):
    # 横に並べて表示する
    print("{", end="")
    for i in range(num-1):
        print(f"({upper[domino_index[i]]},", end="")
        print(f"{lower[domino_index[i]]}),", end="")
    print(f"({upper[domino_index[num-1]]}", end="")
    print(f",{lower[domino_index[num-1]]})", end="}\n")
    # 縦に並べて表示する
    if vertically is True:
        print(" "*8, end="")
        for i in range(num-1):
            print(f"{upper[domino_index[i]]}", end="|")
        print(f"{upper[domino_index[num-1]]}", end="\n")
        print(" "*8, end="")
        for i in range(num-1):
            print(f"{lower[domino_index[i]]}", end="|")
        print(f"{lower[domino_index[num-1]]}", end="\n")


# ----------------------------------------------------------------------
# num個だけ元のペアのリストから文字列を持ってきて結合し,
# その後2つのリストが共通系列かどうか比較する
# ----------------------------------------------------------------------
def string_concatenation_and_comparison(upper, lower, domino_index, num):
    # string1をupperを順番に合体させて作る
    # string2をlowerを順番に合体させて作る
    string1 = ""
    string2 = ""
    for i in range(num):
        string1 += upper[domino_index[i]]
        string2 += lower[domino_index[i]]
    # string1とstring2が一致するなら共通系列であるので表示する
    if string1 == string2:
        print(f"⭕️：{string2}", end=" ")
        print_discovered_match(upper, lower, domino_index, num)


# ----------------------------------------------------------------------
# 指定された長さでポストの対応問題(PCP)を再帰的に解く
# ----------------------------------------------------------------------
def solve_pcp_with_specified_length(upper, lower, domino_index, length, num):
    if length == num:
        string_concatenation_and_comparison(upper, lower, domino_index, num)
    else:
        for i in range(len(upper)):
            domino_index[num] = i
            solve_pcp_with_specified_length(upper, lower,
                                            domino_index, length, num+1)


# ----------------------------------------------------------------------
# ポストの対応問題(PCP)を指定した長さ以下で解く
# ----------------------------------------------------------------------
def solve_pcp(domino, match_length):
    # 元のペアのリストを分割した2つのリストを作る
    upper, lower = divide_domino(domino)
    # PCP(Post_Correspondence_Problem)の問題文を表示する
    print_problem_statement(upper, lower)
    # PCP(Post_Correspondence_Problem)を指定した長さ以下で解く
    for i in range(1, match_length+1, 1):
        domino_index = [-1] * match_length
        # print()
        # print(f"ドミノから{i}個の文字列の組を持ってきた場合")
        solve_pcp_with_specified_length(upper, lower, domino_index, i, 0)
