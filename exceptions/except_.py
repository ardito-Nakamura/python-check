# 「エラー{番号}が発生しました」と出力される関数: raise_exceptionの処理を考えてください。※raise文を使用しないこと
from raise_exceptions import raise_exception_6 as raise_exception


def notice_exception():
    try:
        raise_exception()
    except ValueError as e:
        print("エラー1が発生しました")
        raise e
    except ZeroDivisionError as e:
        print("エラー2が発生しました")
        raise e
    except KeyError as e:
        print("エラー3が発生しました")
        raise e
    except TypeError as e:
        print("エラー4が発生しました")
        raise e
    except AttributeError as e:
        # 直接書き換え
        print("エラー5が発生しました")
        raise e
    except SyntaxError as e:
        # SyntaxErrorを発生させてください(出力はなし)。
        print("エラー6が発生しました")
        raise e


notice_exception()
