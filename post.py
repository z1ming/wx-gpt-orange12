# -*- encoding: utf-8 -*-
"""
@File: post.py
@Author: mengziming021
@Time: 2023/5/23 5:54 下午
"""
import json

import requests


def postGpt(content):
    try:
        # 发起POST请求
        headers = {'Authorization': 'Bearer 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',
                   'Content-Type': 'application/json'}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ]
        }
        response = requests.post('https://orange12.work/v1/chat/completions', headers=headers, data=json.dumps(data))

        # 处理响应
        print(response.status_code)  # 获取响应状态码
        print(response.text)  # 获取响应内容
        print(json.loads(response.text)["choices"][0]["message"]["content"])
        return json.loads(response.text)["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)
