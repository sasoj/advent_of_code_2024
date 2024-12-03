import lib
good = 0
for report in lib.int_records(2):
    x = report[0]
    y = report[1]
    sign = lib.sign(x - y)
    ok = True
    index = 2
    while ok: 
        ok = 0 < (x - y) * sign < 4
        if index >= len(report):
            break
        x = y
        y = report[index]
        index += 1
    
    good += 1 if ok else 0
    print(report, ok)

print(good)


print("Second")

def check(report):
    def check2(rest_report, x, sign, can_skip):
        for y in rest_report:
            ok = 0 < (x-y)*sign < 4
            if not ok and can_skip:
                # ignore this y and use the joker
                can_skip = False
                ok = True
            else:
                x = y
            if not ok:
                break
        return ok
    # cases: go up and down, assume bad first or good first
    ok1 = check2(report[1:], report[0], 1, True)
    ok2 = check2(report[1:], report[0], -1, True)
    ok3 = check2(report[2:], report[1], 1, False)
    ok4 = check2(report[2:], report[1], -1, False)

    return (ok1 or ok2 or ok3 or ok4, ok1, ok2, ok3, ok4)


good = 0

for report in lib.int_records(2):
    ok = check(report)
    print(report, ok)
    good += 1 if ok[0] else 0
    
print(good)

