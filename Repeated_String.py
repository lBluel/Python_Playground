
# Complete the 'repeatedString' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    def extra_a(e):
        ex = 0
        for m in e:
            if m == 'a':
                ex += 1
        return ex                
    t = s

    step = 0
    cnt = 0
    while step < len(s):
        if s[step] == 'a':
            cnt += 1
        step += 1        
    anums = cnt * int(n / len(s)) + extra_a(s[:n % len(s)])
    return anums       
     
if __name__ == '__main__':
    result = repeatedString(s = 'abc', n = 200)
    print(result)