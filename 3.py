def appearance(intervals):
    for i in range(len(intervals)):
        interval = intervals[i]
        events = []
        real_interval = interval['data']
        for k in real_interval:
            ev = real_interval[k]
            for u in range(0, len(ev)-11, 2):
                for z in range(0, len(ev) - 3, 2):
                    if ev[z] <= ev[z+2] and ev[z+2] <= ev[z+1]:
                        ev.pop(z + 1)
                        ev.pop(z + 1)
                        break
                    if ev[u] < ev[z] and ev[u+1] > ev[z] and u != z:
                        ev.pop(u + 1)
                        ev.pop(z)
                        break

            print(ev)
            for z in range(len(ev)):
                events.append((ev[z], 1 - 2 * (z % 2)))
        events.sort()
        cnt = 0
        start = -1
        elapsedtime = 0

        for e in events:
            cnt += e[1]
            if cnt == 3:
                start = e[0]
            if cnt == 2 and start > 0:
                elapsedtime += e[0] - start
                start = -1
        print(elapsedtime)



tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

appearance(tests)