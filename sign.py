import requests
import os
import json
import time
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 小黑盒API基础URL
BASE_URL = "https://api.xiaoheihe.cn"

def get_headers():
    """获取请求头"""
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.xiaoheihe.cn',
        'Referer': 'https://www.xiaoheihe.cn/app/bbs/home'
    }

def login(account, password):
    """登录小黑盒账号"""
    login_url = f"{BASE_URL}/account/login"
    
    data = {
        "account": account,
        "password": password,
        "remember": True
    }
    
    try:
        response = requests.post(login_url, headers=get_headers(), json=data)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            logger.info("登录成功!")
            # 保存cookie和token
            cookies = response.cookies
            return cookies
        else:
            logger.error(f"登录失败: {result.get('msg', '未知错误')}")
            return None
    except Exception as e:
        logger.error(f"登录请求异常: {e}")
        return None

def daily_sign(cookies):
    """执行每日签到"""
    sign_url = f"{BASE_URL}/bbs/app/api/sign/v2"
    
    headers = get_headers()
    
    try:
        response = requests.post(sign_url, headers=headers, cookies=cookies)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            logger.info(f"签到成功! {result.get('data', {}).get('msg', '')}")
            return True
        else:
            logger.warning(f"签到失败或已签到: {result.get('msg', '未知错误')}")
            return False
    except Exception as e:
        logger.error(f"签到请求异常: {e}")
        return False

def check_sign_status(cookies):
    """检查签到状态"""
    status_url = f"{BASE_URL}/bbs/app/api/check/signin"
    
    try:
        response = requests.get(status_url, headers=get_headers(), cookies=cookies)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            is_signed = result.get('data', {}).get('is_sign', False)
            if is_signed:
                logger.info("今日已签到!")
            else:
                logger.info("今日未签到，准备签到...")
            return is_signed
        else:
            logger.error(f"检查签到状态失败: {result.get('msg', '未知错误')}")
            return False
    except Exception as e:
        logger.error(f"检查签到状态请求异常: {e}")
        return False

def main():
    # 从环境变量获取账号和密码
    account = os.environ.get('HEYBOX_ACCOUNT')
    password = os.environ.get('HEYBOX_PASSWORD')
    
    if not account or not password:
        logger.error("未设置小黑盒账号或密码环境变量")
        return
    
    # 1. 登录
    cookies = login(account, password)
    if not cookies:
        return
    
    # 2. 检查签到状态
    is_signed = check_sign_status(cookies)
    
    # 3. 如果未签到则执行签到
    if not is_signed:
        daily_sign(cookies)

if __name__ == '__main__':
    main()
import requests
import os
import json
import time
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 小黑盒API基础URL
BASE_URL = "https://api.xiaoheihe.cn"

def get_headers():
    """获取请求头"""
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.xiaoheihe.cn',
        'Referer': 'https://www.xiaoheihe.cn/app/bbs/home'
    }

def login(account, password):
    """登录小黑盒账号"""
    login_url = f"{BASE_URL}/account/login"
    
    data = {
        "account": account,
        "password": password,
        "remember": True
    }
    
    try:
        response = requests.post(login_url, headers=get_headers(), json=data)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            logger.info("登录成功!")
            # 保存cookie和token
            cookies = response.cookies
            return cookies
        else:
            logger.error(f"登录失败: {result.get('msg', '未知错误')}")
            return None
    except Exception as e:
        logger.error(f"登录请求异常: {e}")
        return None

def daily_sign(cookies):
    """执行每日签到"""
    sign_url = f"{BASE_URL}/bbs/app/api/sign/v2"
    
    headers = get_headers()
    
    try:
        response = requests.post(sign_url, headers=headers, cookies=cookies)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            logger.info(f"签到成功! {result.get('data', {}).get('msg', '')}")
            return True
        else:
            logger.warning(f"签到失败或已签到: {result.get('msg', '未知错误')}")
            return False
    except Exception as e:
        logger.error(f"签到请求异常: {e}")
        return False

def check_sign_status(cookies):
    """检查签到状态"""
    status_url = f"{BASE_URL}/bbs/app/api/check/signin"
    
    try:
        response = requests.get(status_url, headers=get_headers(), cookies=cookies)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'ok':
            is_signed = result.get('data', {}).get('is_sign', False)
            if is_signed:
                logger.info("今日已签到!")
            else:
                logger.info("今日未签到，准备签到...")
            return is_signed
        else:
            logger.error(f"检查签到状态失败: {result.get('msg', '未知错误')}")
            return False
    except Exception as e:
        logger.error(f"检查签到状态请求异常: {e}")
        return False

def main():
    # 从环境变量获取账号和密码
    account = os.environ.get('HEYBOX_ACCOUNT')
    password = os.environ.get('HEYBOX_PASSWORD')
    
    if not account or not password:
        logger.error("未设置小黑盒账号或密码环境变量")
        return
    
    # 1. 登录
    cookies = login(account, password)
    if not cookies:
        return
    
    # 2. 检查签到状态
    is_signed = check_sign_status(cookies)
    
    # 3. 如果未签到则执行签到
    if not is_signed:
        daily_sign(cookies)

if __name__ == '__main__':
    main()
