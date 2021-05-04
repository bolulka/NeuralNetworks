print('task d')
print('Input n: ')
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
print('Input guesses: ')
while True:
    inp = input()
    if inp == 'STOP' or len(possible_nums) == 1:
        break
    answer = ''.join(filter(str.isalpha, inp)) or None
    guess_ = inp[0:-len(answer)].split()
    guess = set([int(item) for item in guess_])
    if answer == 'YES':
        possible_nums &= guess
        if len(possible_nums) == 1: break
    else:
        possible_nums &= all_nums - guess
        if len(possible_nums) == 1: break

print('Result: ',end=' ')
print(possible_nums)

