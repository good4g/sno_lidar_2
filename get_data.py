import threading

import serial

#clean_data = [[0, 88], [5, 92], [10, 64], [15, 44], [20, 36], [25, 30], [30, 28], [35, 25], [40, 23], [45, 21], [50, 19], [55, 19], [60, 19], [65, 17], [70, 17], [75, 17], [80, 16], [85, 16], [90, 16], [95, 17], [100, 17], [105, 17], [110, 18], [115, 19], [120, 20], [125, 20], [130, 22], [135, 25], [140, 27], [145, 31], [150, 38], [155, 50], [160, 66], [165, 83], [170, 128], [175, 116], [180, 116]], [26.832815729997478, 66.09084656743322, 46.475800154489, 25.298221281347036, 19.8997487421324, 10.770329614269007, 12.609520212918492, 9.797958971132712, 9.38083151964686, 8.94427190999916, 6.082762530298219, 0.0, 5.916079783099616, 0.0, 0.0, 5.744562646538029, 0.0, 0.0, 5.744562646538029, 0.0, 0.0, 5.916079783099616, 6.082762530298219, 6.244997998398398, 0.0, 9.16515138991168, 11.874342087037917, 10.198039027185569, 15.231546211727817, 21.97726097583591, 32.49615361854384, 43.08131845707603, 50.32891812864648, 97.44229061347029, 54.11099703387473, 0.0]

ad = []


def get_data_from_rangefinder(uart):

    global ad

    while uart.is_open:
        dirty_data = uart.readline().decode().strip()

        # 5 0 17
        angle_y, angle_x, dist = map(int, dirty_data.split())
        ad += [[angle_y, angle_x, dist]]
        if len(ad) == 2:
            #print(ad)
            return ad
        elif len(ad) == 3:
            last_two = ad[1:]
            ad = [ad[-1]]

            return last_two



