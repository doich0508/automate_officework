from password import func_password
from jmotto import func_make_text
from slack import func_post_slack


main_password, main_token = func_password()
main_text = func_make_text(main_password)
func_post_slack(main_token, main_text)
