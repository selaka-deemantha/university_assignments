def angle_cal(s):
    h,m=s.split(":")
    hour_angle=0
    minut_angle=0
    if int(h)==12:
        hour_angle=0+ int(m)*0.5
    else:
        hour_angle=int(h)*30 + int(m)*0.5
    minut_angle=int(m)*6
    if abs(minut_angle-hour_angle)<=180:
        return abs(minut_angle-hour_angle)
    else:
        return 360-abs(minut_angle-hour_angle)






print(angle_cal("2:40"))