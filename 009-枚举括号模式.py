# 生成括号模式
# 输入括号对数n, 输出所有可能的括号顺序. 如:
# n = 3
# ['((()))', '(())()', '(()())', '()(())', '()()()']
# 递归法

# l为左括号的个数, r右括号个数, p为括号构成的字符串, result为记录各种组合的列表
def generate(l, r, p, result=[]):
    if l:
        generate(l - 1, r, p + "(")
    if r > l:
        generate(l, r - 1, p + ")")
    if not r:
        result.append(p)
    return result

def main(n=5):
    print(generate(l=n,r=n,p=''))

main()

# 分析: (n = 3)
# gen(3, 3, '') -> gen(2, 3, '(') -> gen(1, 3, '((') -> gen(0, 3, '(((') -> gen(0, 2, '((()') ...-> append('((()))')
#                                                    -> gen(1, 2, '(()') -> gen(0, 2, '(()(') ...-> append('(()())')
#                                                                        -> gen(1, 1, '(())') ...-> append('(())()')
#                                 -> gen(2, 2, '()') -> gen(1, 2, '()(') -> gen(0, 2, '()((') ...-> append('()(())')
#                                                                        -> gen(1, 1, '()()') ...-> append('()()()')
# 输入参数为列表或字典时, 重新赋值后不会对原参数造成改变, 但是append / dict['key']=value则会
# 输入参数为字符串、整型或浮点, 不发生改变