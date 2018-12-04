from collections import defaultdict, Counter
import re
import datetime

times = {}

with open("day4input.txt", "r") as f:
    for line in f.readlines():
        split = line.split('] ')
        timestr = split[0].lstrip('[')
        detail = split[1].rstrip('\n')

        time = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M")
        times[time] = detail

# go through chronologically
current_guard = -1
fell_asleep = -1
guard_sleeps = defaultdict(list)

for time in sorted(times.keys()):
    detail = times[time]
    search = re.search(r'Guard #([\d]{1,}) begins shift', detail) 
    if search:
        current_guard = search.group(1)
    elif detail == "wakes up":
        for minute in range(fell_asleep, time.minute):
            guard_sleeps[current_guard].append(minute)
    elif detail == "falls asleep":
        fell_asleep = time.minute

max_sleeps = {}
for guard in guard_sleeps:
    counter = Counter(guard_sleeps[guard])
    max_sleeps[guard] = counter.most_common(1)[0]

sleepiest_guard = max(max_sleeps.keys(), key=(lambda key: max_sleeps[key][1]))
sleepiest_minute = max_sleeps[sleepiest_guard][0]


print(int(sleepiest_guard)*sleepiest_minute)
