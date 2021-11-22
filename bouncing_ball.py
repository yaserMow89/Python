#The Explanation is in another file in the same folder with name bouncing_ball_Readme
import math
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return int(math.log((window+0.001)/h, bounce)) * 2 + 1
