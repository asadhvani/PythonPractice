def calculator(op1, oper, op2):
    if oper=="+":
        result=op1+op2
    if oper=="-":
        result=op1-op2
    if oper=="*":
        result=op1*op2
    if oper=="/":
        result=op1/op2
    return result
def power(o2p1, pow1):
    orig2p1=o2p1
    for x in range(pow1-1):
        o2p1=orig2p1*o2p1
    return o2p1
