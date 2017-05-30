import heapq
from collections import defaultdict



def encode(frequency):
    # Priority queue holding the frequency
    heap = [[count, [symbol, '']] for symbol, count in frequency.items()]
    heapq.heapify(heap)

    # while there are still items to pop off the heap
    while len(heap) > 1:
        # pop the substrings with the two lowest frequencies
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # establish the code for the substring
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        # add the combined substring and frequency back to the queue
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    sort_parameter = lambda p: (len(p[-1]), p)
    return sorted(heapq.heappop(heap)[1:], key=sort_parameter)


if __name__ == '__main__':
    '''input for single word'''
    # string = input("Enter word: ")

    ''' input for file'''
    fname = input("FileName: ")
    f = open(fname)
    string = f.read()

    # build a dictionary to hold the frequency of each character
    frequency = defaultdict(int)
    unique = set(string)
    for symbol in unique:
        frequency[symbol] = string.count(symbol)

    # build and output huffman encoding
    huff = encode(frequency)
    print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
    encoded_string = ''
    for p in huff:
        if(p[0] == "\n"):
            print("'newline'".ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
        elif(p[0] == " "):
            print("'whitespace'".ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
        else:
            print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])

    # uild and output the encoding
    for char in string:
        for p in huff:
            if p[0] == char:
                encoded_string+=p[1]
                break
    print("Encoded String = "+encoded_string)
    print("Encoded String Length =",len(encoded_string))
