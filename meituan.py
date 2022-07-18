import os
import platform
import time
import sys

import uiautomator2 as u2

# 连接手机
def connect_phone(device_name):
    d = u2.connect(device_name)
    if not d.service("uiautomator").running():
        # 启动uiautomator服务
        print("start uiautomator")
        d.service("uiautomator").start()
        time.sleep(2)

    if not d.agent_alive:
        print("agent_alive is false")
        u2.connect()
        d = u2.connect(device_name)
    return d


def play_voice(content):
    """
    播放声音提醒
    """
    system = platform.system()
    if system == "Windows":
        from playsound import playsound
        #video_path = os.path.join(os.getcwd(), "sources\success.mp3")
        #playsound(video_path)
    else:
        os.system(f'say "{content}"')


def qiang_cai(device_name):
    d = connect_phone(device_name)

    # TEST
    #print(d.dump_hierarchy())

    #d.app_start("com.sankuai.meituan")  # 美团
    d.app_start("com.meituan.retail.v.android")  # 美团买菜
    count = 1
    time_start = time.time()

    #TEST
    #print(("结算" in str(d.dump_hierarchy())))
    #d.click((682+792)/2, (2268+2328)/2)
    print(d.dump_hierarchy())

    '''
     <node index="1" text="" resource-id="" class="android.view.ViewGroup" package="com.sankuai.meituan" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[682,2268][792,2328]" />
    '''

    while True:
        start = time.time()
        if d(textContains="合计").exists:
            print("点击结算")
            #d(textContains="结算").click()

            # By coordinates
            #x,y = d(textContains="合计").center
            #d.click(x,y)

            # By tree
            d1 = d(className="android.support.v4.view.ViewPager", packageName="com.meituan.retail.v.android", clickable=False, enabled=True, focusable=True, focused=False, scrollable=True, longClickable=False, selected=False)
            print("d1: ", d1.info)
            d2 = d1.child(index="0", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d2: ", d2.info)
            d3 = d2.child(index="0", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d3: ", d3.info)
            d4 = d3.child(index="0", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d4: ", d4.info)
            d5 = d4.child(index="1", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d5: ", d5.info)
            '''d6 = d5.child(index="0", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d6: ", d6.info)
            d7 = d6.child(index="1", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d7: ", d7.info)
            d8 = d7.child(index="0", className="android.view.ViewGroup", clickable=False, enabled=True, focusable=False, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d8: ", d8.info)
            d9 = d8.child(index="1", className="android.view.ViewGroup", clickable=True, enabled=True, focusable=True, focused=False, scrollable=False, longClickable=False, selected=False)
            print("d9: ", d9.info)
            d9.click()'''


            '''print(d(className="android.support.v4.view.ViewPager") \
                .child(index=0) \
                .child(index=0) \
                .child(index=0) \
                .child(index=1) \
                .child(index=0) \
                .child(index=1) \
                .child(index=0) \
                .child(index=1) \
                .info)'''
        elif d(text="我知道了").exists:
            print("点击我知道了")
            d(text="我知道了").click()
        elif d(text="重新加载").exists:
            print("重新加载")
            d(text="重新加载").click()
        elif d(text="返回购物车").exists:
            print("点击返回购物车")
            d(text="返回购物车").click()
        elif d(text="立即支付").exists:
            print("点击立即支付")
            d(text="立即支付").click()
        elif d(text="确认并支付").exists:
            print("点击确认并支付")
            d(text="确认并支付").click()
        elif d(resourceId="btn-line").exists:
            #play_voice("主人我抢到菜了，快来支付！主人我抢到菜了，快来支付！主人我抢到菜了，快来支付！主人我抢到菜了，快来支付！主人我抢到菜了，快来支付！主人我抢到菜了，快来支付！")
            print("确认支付")
            d(resourceId="btn-line").click()
            break
        else:
           print("FUCKED UP")
           break
        print("本次花费时间:", time.time() - start)
        print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
        count += 1



def run(device_name):
    while True:
        try:
            qiang_cai(device_name)

            #TEST
            break
        except Exception as e:
            print(e)
            play_voice("有异常，尝试重新启动中")
            time.sleep(5)


if __name__ == '__main__':


    # 此处填写设备编号
    # device_name = "emulator-5554"
    device_name = "8KE0219606027677"
    # device_name = "b8c282ac"
    run(device_name)

