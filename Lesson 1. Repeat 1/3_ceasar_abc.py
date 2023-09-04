abc = list(input())
turn = int(input())
code_abc = []
decode_abc = []
for i in range(len(abc)):
    code_abc.append(abc[(i + turn) % len(abc)])
    decode_abc.append(abc[(i - turn) % len(abc)])
print(''.join(code_abc), ''.join(abc), ''.join(decode_abc), sep='\n')
