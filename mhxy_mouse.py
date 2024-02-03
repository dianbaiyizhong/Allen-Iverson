# https://blog.csdn.net/qq_33126131/article/details/102841015  获取梦幻西游鼠标位置
import aircv as ac
import pydirectinput
import time

time.sleep(3)

import pyautogui
def matchImg(imgsrc, imgobj, confidencevalue=0.5):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgobj)
    imobj = ac.imread(imgsrc)
    match_result = ac.find_template(imsrc, imobj,
                                    confidencevalue) 
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result

if __name__ == '__main__':
    mouse_pos = matchImg('mouse.png','game3.png',0.7)
    target_pos = matchImg('flag.png','game3.png',0.7)
    tx = int(target_pos['result'][0])
    ty = int(target_pos['result'][1])


    x = int(mouse_pos['result'][0])
    y = int(mouse_pos['result'][1])

    x, y = pyautogui.position()

    distance = ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5

    step_x, step_y = (tx - x) / 50, (ty - y) / 50

    print(distance)
    # 控制鼠标逐段移动
    for i in range(50):
        pydirectinput.moveTo(int(x + i * step_x), int(y + i * step_y), duration=0.1)
        time.sleep(0.1)
    

    # pydirectinput.moveRel(xOffset=int(x), yOffset=int(y), duration=0.4, relative=True)


