import time

total_num = []
total_numContinue = []
time_start = time.time()
linkNum = [0,0,0,0,0]
for i in range(1, 29):
    for j in range(i + 1, 30):
        if i + 1 == j:
            linkNum[0] = 1
        else:
            linkNum[0] = 0
        for k in range(j + 1, 31):
            if j + 1 == k:
                linkNum[1] = 1
            else:
                linkNum[1] = 0
            for l in range(k + 1, 32):
                if k + 1 == l:
                    linkNum[2] = 1
                else:
                    linkNum[2] = 0
                for m in range(l + 1, 33):
                    if l + 1 == m:
                        linkNum[3] = 1
                    else:
                        linkNum[3] = 0
                    for n in range(m + 1, 34):
                        num = str(i) + "-" + str(j) + "-" + str(k) + "-" + str(l) + "-" + str(m) + "-" + str(n)
                        if m + 1 == n:
                            linkNum[4] = 1
                        else:
                            linkNum[4] = 0
                        total = 0
                        for ii in linkNum:
                            total = total + ii
                        if total > 3:
                            total_numContinue.append(num)
                            continue
                        total_num.append(num)
time_end = time.time()
print('totally cost', time_end - time_start)
print('len ', len(total_num))
print('len total_numContinue ', len(total_numContinue))
