from datetime import datetime

def get_current_time():
    # 获取当前时间
    current_time = datetime.now()
    
    # 格式化当前时间为 "月-日-时-分"
    formatted_time = current_time.strftime("%m月-%d日-%H时-%M分")
    
    return formatted_time