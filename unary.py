import re

pre_code = ''
code = list()

message = input()

for char in message:
    char_in_bin = f'{ord(char):b}'.zfill(7)
    # char_in_bin: str.
    # Pour l'exemple, char = 'C'
    #   ord(char) = 67
    #   f'{ord(char):b}' = '1000011'
    #   ici zfill(7) ne change rien
    #   mais '1'.zfill(7) = '0000001' ;-)
    pre_code += char_in_bin

seqs = re.findall(r"0+|1+", pre_code)
# seqs: list.
# Pour l'exemple, seqs = ['1', '0000', '11']
for seq in seqs:
    code.append('00' if seq[0] == '0' else '0')
    code.append('0' * len(seq))

print(' '.join(code))