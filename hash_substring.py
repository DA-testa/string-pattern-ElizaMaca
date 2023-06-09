# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type=input().rstrip().lower()
    
    if input_type == 'i':
        return (input().rstrip(), input().rstrip())
    elif input_type == 'f':
        with open('./tests/06', 'r') as f:
            return (f.readline().rstrip(), f.readline().rstrip())
    else:
        raise ValueError('Invalid input type')

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_length=len(pattern)
    text_length=len(text)
    pattern_hash=hash(pattern)
    text_hash=hash(text[:pattern_length])
    occurrances=[]

    for i in range(text_length-pattern_length+1):
        if pattern_hash==text_hash and pattern==text[i:i+pattern_length]:
            occurrances.append(i)
        if i<text_length-pattern_length:
            text_hash=hash(text[i+1:i+pattern_length+1])
    # and return an iterable variable
    return occurrances

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))