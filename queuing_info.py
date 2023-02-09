import json
import requests
import jionlp as jio

def get_build_info(num=False):
    """
    输入你的身份证信息查询实体优租房的排队详情;
    """
    url = "https://ent.sipprh.com/ModuleDefaultCompany/RentManage/SearchRentNo"

    if num is False:
        human_base_num = "xxxxxxxxxxxxxxxxxx"
    else:
        human_base_num = num

    params = {"CertNo": human_base_num}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    response = requests.post(url=url,headers=headers,params=params)
    res_json = json.loads(response.text)
    res = jio.remove_html_tag(res_json['prompWord'])
    print(res)
    return res 

def feishu_bot(num):
    """
    复制你申请的bot的webhook地址;
    """
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/'填写你申请的webhook的token'"


    payload_message = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "租房小助手温馨提示您",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": get_build_info(num)
                            }
                        ]
                    ]
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
    return response.text

def mod_select(bot=False,num=False):
    if bot is False:
        get_build_info(num)
    else:
        feishu_bot(num)

mod_select()