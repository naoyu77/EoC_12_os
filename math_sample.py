"""
2進数での算術演算サンプル
Nand2Tetris 第12章 Math クラスの実装例
"""


def multiply(x: int, y: int) -> int:
    """
    乗算: シフトと加算だけで実現

    原理: y を2進数で分解し、各ビットが1の位置で
    シフトした x を加算する
    """
    sum_result = 0
    shifted_x = x

    print(f"\n=== {x} × {y} を計算 ===")
    print(f"x = {x} ({bin(x)})")
    print(f"y = {y} ({bin(y)})")
    print()

    for i in range(16):  # 16ビット整数を想定
        bit = (y >> i) & 1  # y の i番目ビット

        if bit == 1:
            print(f"ビット{i} = 1: sum += {shifted_x}")
            sum_result += shifted_x
        else:
            print(f"ビット{i} = 0: 加算しない")

        shifted_x <<= 1  # 左シフト（×2）

        if shifted_x > 65535:  # オーバーフロー防止
            break

    print(f"\n結果: {sum_result}")
    return sum_result


def divide(x: int, y: int) -> int:
    """
    除算: 再帰的アルゴリズム

    原理: 除数を2倍していき、大きい塊から引く
    """
    print(f"divide({x}, {y})")

    if y > x:
        print(f"  {y} > {x} なので 0 を返す")
        return 0

    q = divide(x, 2 * y)  # 除数を2倍して再帰

    remainder = x - 2 * q * y
    print(f"  戻り: x={x}, y={y}, q={q}, 残り={remainder}")

    if remainder < y:
        result = 2 * q
        print(f"  {remainder} < {y} なので {result} を返す")
    else:
        result = 2 * q + 1
        print(f"  {remainder} >= {y} なので {result} を返す")

    return result


def divide_iterative(x: int, y: int) -> int:
    """
    除算: ループ版（筆算と同じ方法）

    原理: 除数を大きくしてから、大きい方から引く
    """
    print(f"\n=== {x} ÷ {y} を計算（ループ版） ===")

    quotient = 0

    # 除数を大きくしていく
    temp_y = y
    power = 1
    print(f"除数を大きくする: ", end="")
    while temp_y <= x:
        print(f"{temp_y} → ", end="")
        temp_y *= 2
        power *= 2
    print(f"{temp_y}（超えた）")

    # 大きい方から引いていく
    print("\n大きい方から引く:")
    while power > 1:
        temp_y //= 2
        power //= 2
        quotient *= 2

        if temp_y <= x:
            x -= temp_y
            quotient += 1
            print(f"  {temp_y} を引く → 残り {x}, 商に +{power} (= {y}×{power})")
        else:
            print(f"  {temp_y} は引けない")

    print(f"\n結果: {quotient}")
    return quotient


def sqrt(x: int) -> int:
    """
    平方根: 二分探索

    原理: 上位ビットから順に「このビットを立てても
    二乗がxを超えないか」を確認
    """
    print(f"\n=== √{x} を計算 ===")

    y = 0

    # 16ビット整数の平方根は最大8ビット
    for j in range(7, -1, -1):
        bit_value = 1 << j  # 2^j
        candidate = y + bit_value
        square = candidate * candidate

        if square <= x:
            y = candidate
            print(f"ビット{j}: ({candidate})² = {square} <= {x} → y = {y}")
        else:
            print(f"ビット{j}: ({candidate})² = {square} > {x} → 立てない")

    print(f"\n結果: {y}")
    return y


if __name__ == "__main__":
    print("=" * 50)
    print("乗算のサンプル")
    print("=" * 50)

    result = multiply(12, 10)
    assert result == 120, f"期待: 120, 実際: {result}"

    result = multiply(6, 5)
    assert result == 30, f"期待: 30, 実際: {result}"

    print("\n" + "=" * 50)
    print("除算のサンプル（再帰版）")
    print("=" * 50)

    print(f"\n--- 30 ÷ 4 ---")
    result = divide(30, 4)
    assert result == 7, f"期待: 7, 実際: {result}"

    print("\n" + "=" * 50)
    print("除算のサンプル（ループ版）")
    print("=" * 50)

    result = divide_iterative(30, 4)
    assert result == 7, f"期待: 7, 実際: {result}"

    result = divide_iterative(1000, 4)
    assert result == 250, f"期待: 250, 実際: {result}"

    print("\n" + "=" * 50)
    print("平方根のサンプル")
    print("=" * 50)

    result = sqrt(25)
    assert result == 5, f"期待: 5, 実際: {result}"

    result = sqrt(100)
    assert result == 10, f"期待: 10, 実際: {result}"

    print("\n" + "=" * 50)
    print("すべてのテストが成功しました！")
    print("=" * 50)
