import re
import requests
import tkinter as tk
from tkinter import messagebox

# 提取 bankAppSchema 的正则表达式
schema_regex = r'bankAppSchema:\s*"([^"]+)"'

def send_request():
    url = url_entry.get()
    if not url:
        messagebox.showerror("错误", "请输入URL")
        return
    
    try:
        # 发起 GET 请求
        response = requests.get(url, headers={
            "Sec-Fetch-Site": "same-origin",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Sec-Fetch-Mode": "navigate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 upwbversion=3.4.6",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-HK,zh-Hant;q=0.9"
        })

        # 检查响应状态
        if response.status_code == 200:
            response_text = response.text
            # 使用正则表达式提取 bankAppSchema 的值
            match = re.search(schema_regex, response_text)
            if match:
                bank_app_schema = match.group(1)
                result_label.config(text=f"bankAppSchema: {bank_app_schema}")
            else:
                result_label.config(text="未找到 bankAppSchema 参数")
        else:
            result_label.config(text=f"请求失败，状态码: {response.status_code}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("请求错误", f"请求失败: {e}")

# 创建主界面
root = tk.Tk()
root.title("bankAppSchema 提取工具")
root.geometry("400x200")

# URL 输入框
tk.Label(root, text="请输入 URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# 发起请求按钮
send_button = tk.Button(root, text="发起请求并提取 bankAppSchema", command=send_request)
send_button.pack(pady=10)

# 结果显示标签
result_label = tk.Label(root, text="", wraplength=300, justify="left")
result_label.pack(pady=10)

root.mainloop()