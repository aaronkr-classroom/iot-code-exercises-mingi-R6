# 4_operators.py
a = 132
b = 45

fmt0 = '{:<10}' # 변수 + 공백 10개까지
fmt1 = '0b{:08b} 0x{:02x} {:3}' # 0b________ 8개 이진법, 0x__16진법 2개, 3개의 10진법

# bit AND &
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n = 30
print('-' * n)

print(fmt0.format('a & b'), fmt1.format(a&b,a&b,a&b))

# bit OR |
print()
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-' * n)
print(fmt0.format('a | b'), fmt1.format(a|b,a|b,a|b))

# bit XOR ^
print("\n bit XOR6")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-' * n)
print(fmt0.format('a ^ b'), fmt1.format(a^b,a^b,a^b))

# bit NOT ~
print("\n bit XOR6")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a&0xFF,~a&0xFF,~a&0xFF))

# bit 왼쪽 시프트 <<
print("\n bit XOR6")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('a << 2'), fmt1.format(a<<2&0xFF,a<<2&0xFF,a<<2&0xFF))

# bit 오른쪽 시프트 >>
print("\n bit XOR6")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('a >> 2'), fmt1.format(a>>2&0xFF,a>>2&0xFF,a>>2&0xFF))

