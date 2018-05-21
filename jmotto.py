from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system

LOGIN = 'https://www1.j-motto.co.jp/fw/dfw/po80/portal/jsp/J10201.jsp?https://www1.j-motto.co.jp/fw/dfw/gws/cgi-bin/aspioffice/iocjmtgw.cgi?cmd=login'
ORG_ID = 'JM0586825' # 組織ID
USRE_ID = '02017' # 会員番号
ELEMENT_ORG = 'memberID'
ELEMENT_USER = 'userID'
ELEMENT_PASS = 'password'
ELEMENT_SUBMIT = 'loginSubmit'
ELEMENT_INFO = "//a[@data-hashcmd='infoindex']"
START_TEXT = '未読のお知らせがあります。'
NULL_TEXT = '未読のお知らせはありません。'
MAIN_URL = 'https://gws41.j-motto.co.jp/cgi-bin/JM0586825/dneo.cgi?'
# コマンド用
KILL_FIREFOX = 'pkill -f firefox'
KILL_FIREFOX_APP = 'pkill -f /Applications/firefox.app'


def get_information(url, password):
    option = Options()
    option.set_headless()
    browser = webdriver.Firefox(options=option)
    # j-mottoログイン
    browser.get(LOGIN)

    # ページが開くまで5秒待機
    sleep(5)

    insert_org = browser.find_element_by_id(ELEMENT_ORG)
    insert_org.send_keys(ORG_ID)
    insert_user = browser.find_element_by_id(ELEMENT_USER)
    insert_user.send_keys(USRE_ID)
    insert_pass = browser.find_element_by_id(ELEMENT_PASS)
    insert_pass.send_keys(password)
    browser.find_element_by_class_name(ELEMENT_SUBMIT).click()

    # ページが開くまで10秒待機
    sleep(10)
    # information要素取得
    information = browser.find_elements_by_xpath(ELEMENT_INFO)

    array_info = []
    for item in information:
        array_info.append(str(item.text))
    return array_info


def func_make_text(enter_password):
    """スクレイピングしたinformationの内容をテキストデータ、辞書型配列の順に加工する
    入力：なし
    出力：辞書型配列{'text':return_text}
    """
    get_text = get_information(LOGIN, enter_password)
    if get_text:
        return_text = START_TEXT
        for item in get_text:
            return_text += "\n" + item
        # 処理が終わったらfirefoxをkillする
        system(KILL_FIREFOX)
        system(KILL_FIREFOX_APP)
        return {'text': return_text}
    else:
        return_text = NULL_TEXT
        return {'text': return_text}

# test
if __name__ == '__main__':
    print_text = func_make_text()
    print(str(print_text['text']))

