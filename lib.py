def records(day, test=""):
    with open(f"inputs/{day}{test}.txt") as f:
        for line in f:
            yield line
            
def int_records(day, test=""):
    for r in records(day, test):
        yield [int(i) for i in r.split()]
        
def sign(n):
    return 0 if n < 0 else 1