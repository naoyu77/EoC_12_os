/**
 * 2進数での算術演算サンプル
 * Nand2Tetris 第12章 Math クラスの実装例（C++版）
 */

#include <iostream>
#include <bitset>

using namespace std;

/**
 * 乗算: シフトと加算だけで実現
 *
 * 原理: y を2進数で分解し、各ビットが1の位置で
 * シフトした x を加算する
 */
int multiply(int x, int y) {
    int sum_result = 0;
    int shifted_x = x;

    cout << "\n=== " << x << " × " << y << " を計算 ===" << endl;
    cout << "x = " << x << " (" << bitset<8>(x) << ")" << endl;
    cout << "y = " << y << " (" << bitset<8>(y) << ")" << endl;
    cout << endl;

    for (int i = 0; i < 16; i++) {  // 16ビット整数を想定
        int bit = (y >> i) & 1;      // y の i番目ビット

        if (bit == 1) {
            cout << "ビット" << i << " = 1: sum += " << shifted_x << endl;
            sum_result += shifted_x;
        } else {
            cout << "ビット" << i << " = 0: 加算しない" << endl;
        }

        shifted_x <<= 1;  // 左シフト（×2）

        if (shifted_x > 65535) {  // オーバーフロー防止
            break;
        }
    }

    cout << "\n結果: " << sum_result << endl;
    return sum_result;
}

/**
 * 除算: 再帰的アルゴリズム
 */
int divide(int x, int y) {
    cout << "divide(" << x << ", " << y << ")" << endl;

    if (y > x) {
        cout << "  " << y << " > " << x << " なので 0 を返す" << endl;
        return 0;
    }

    int q = divide(x, 2 * y);  // 除数を2倍して再帰

    int remainder = x - 2 * q * y;
    cout << "  戻り: x=" << x << ", y=" << y << ", q=" << q << ", 残り=" << remainder << endl;

    int result;
    if (remainder < y) {
        result = 2 * q;
        cout << "  " << remainder << " < " << y << " なので " << result << " を返す" << endl;
    } else {
        result = 2 * q + 1;
        cout << "  " << remainder << " >= " << y << " なので " << result << " を返す" << endl;
    }

    return result;
}

/**
 * 平方根: 二分探索
 */
int sqrt_int(int x) {
    cout << "\n=== √" << x << " を計算 ===" << endl;

    int y = 0;

    // 16ビット整数の平方根は最大8ビット
    for (int j = 7; j >= 0; j--) {
        int bit_value = 1 << j;  // 2^j
        int candidate = y + bit_value;
        int square = candidate * candidate;

        if (square <= x) {
            y = candidate;
            cout << "ビット" << j << ": (" << candidate << ")² = " << square << " <= " << x << " → y = " << y << endl;
        } else {
            cout << "ビット" << j << ": (" << candidate << ")² = " << square << " > " << x << " → 立てない" << endl;
        }
    }

    cout << "\n結果: " << y << endl;
    return y;
}

int main() {
    cout << string(50, '=') << endl;
    cout << "乗算のサンプル" << endl;
    cout << string(50, '=') << endl;

    int result = multiply(12, 10);
    if (result != 120) {
        cerr << "エラー: 期待 120, 実際 " << result << endl;
        return 1;
    }

    result = multiply(6, 5);
    if (result != 30) {
        cerr << "エラー: 期待 30, 実際 " << result << endl;
        return 1;
    }

    cout << "\n" << string(50, '=') << endl;
    cout << "除算のサンプル（再帰版）" << endl;
    cout << string(50, '=') << endl;

    cout << "\n--- 30 ÷ 4 ---" << endl;
    result = divide(30, 4);
    if (result != 7) {
        cerr << "エラー: 期待 7, 実際 " << result << endl;
        return 1;
    }

    cout << "\n" << string(50, '=') << endl;
    cout << "平方根のサンプル" << endl;
    cout << string(50, '=') << endl;

    result = sqrt_int(25);
    if (result != 5) {
        cerr << "エラー: 期待 5, 実際 " << result << endl;
        return 1;
    }

    result = sqrt_int(100);
    if (result != 10) {
        cerr << "エラー: 期待 10, 実際 " << result << endl;
        return 1;
    }

    cout << "\n" << string(50, '=') << endl;
    cout << "すべてのテストが成功しました！" << endl;
    cout << string(50, '=') << endl;

    return 0;
}
