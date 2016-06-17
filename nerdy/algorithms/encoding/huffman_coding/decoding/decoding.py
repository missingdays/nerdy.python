
def huffman_decoding(characters, string):
    output = []
    buf = ''

    for c in string:
        buf += c
        if buf in characters.keys():
            output.append(characters[buf])
            buf = ''
           
    return ''.join(output)

if __name__ == '__main__':
    characters = { '0': 'a', '1': 'b' };
    assert 'aabbabab' == huffman_decoding(characters, '00110101')

    characters = { '01': 'a', '00': 'b', '10': 'c', '11': 'd' }
    assert 'abcddcba' == huffman_decoding(characters, '0100101111100001')

    characters = { '0': 'a', '11': 'b', '100': 'c' }
    assert 'abcbca' == huffman_decoding(characters, '011100111000')
    
    print("Huffman decoding python done")
