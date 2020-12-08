with open("input.txt","r") as f:
    data = [line.rstrip() for line in f]

inst_set = []
line_num = 0
for line in data:
    inst, num = line.split(" ")
    inst_set.append((line_num,(inst,num)))
    line_num += 1

def executeInst(inst, acc):
    (op, num) = inst
    if op == "nop":
        return (1, acc)
    elif op == "jmp":
        return (num, acc)
    else:
        acc = str(int(num)+int(acc))
        return (1, acc)

def detectLoop(inst_set):
    slow = slow_ind = fast_ind  = 0
    while True:
        if slow == 2:
            offset, _ = executeInst(inst_set[slow_ind][1], 0)
            slow_ind += int(offset)
            slow = 0
        else:
            offset, _ = executeInst(inst_set[fast_ind][1], 0)
            fast_ind += int(offset)
            slow += 1
        if fast_ind >= len(inst_set):
            return -1
        if (fast_ind == slow_ind and slow == 0):
            break
    return slow_ind

start_ind = prev_acc = acc = 0
cycle_ind = detectLoop(inst_set)

for i in range(2):
    while True:
        prev_acc = acc
        off, acc = executeInst(inst_set[start_ind][1], acc)
        start_ind += int(off)
        if i == 0:
            off, _ = executeInst(inst_set[cycle_ind][1], 0)
            cycle_ind += int(off)

        if (start_ind == cycle_ind):
            break
print(prev_acc)

def fixInstSet(inst_set):
    i = acc = 0
    trans = str. maketrans("jmno","nojm")
    while True:
        line, (op, num) = inst_set[i]
        if  op != 'acc':
            op = op.translate(trans)
            inst_set[i] = (line, (op,num))
            if detectLoop(inst_set) == -1:
                break
            else:
                op = op.translate(trans)
                inst_set[i] = (line, (op,num))
        off, acc = executeInst(inst_set[i][1], acc)
        i += int(off)
    return inst_set

inst_set = fixInstSet(inst_set)
ind = acc = pacc = 0
while True:
    pacc = acc
    offset, acc = executeInst(inst_set[ind][1], acc)
    ind += int(offset)
    if ind >= len(inst_set):
        break
print(pacc)
