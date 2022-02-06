import numpy as np
N = int(input())
mochi_list = sorted([int(input()) for n in range(N)])
diff_list = np.diff(mochi_list)
can_stack_num = len([1 for diff in diff_list if diff>0]) + 1
print(can_stack_num)
