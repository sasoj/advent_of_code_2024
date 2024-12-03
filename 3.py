
def code():
    import lib

    def parser(line, index):
        def expect_digit(d):
            nonlocal index
            c = line[index]
            if '0' <= c <= '9':
                index += 1
                d[0] = d[0] * 10 + int(c)
                return True
            else:
                return False
        def expect_comma():
            nonlocal index
            if line[index] == ',':
                index += 1
                return True
            else:
                return False

        def expect_close():
            nonlocal index
            if line[index] == ')':
                index += 1
                return True
            else:
                return False
        d1=[0]
        d2 = [0]
        ok = (
            expect_digit(d1) and (
                expect_digit(d1) and (
                    expect_digit(d1) and expect_comma()
                    or 
                    expect_comma())
                or 
                expect_comma())
            
            and expect_digit(d2) and (
                expect_digit(d2) and (
                    expect_digit(d2) and expect_close()
                    or 
                    expect_close())
                or 
                expect_close())
            )
        return ok, d1[0], d2[0], index

    sum = 0   
    for line in lib.records(3, ''):
        index = 0
        # print (line)

        while True:
            index = line.find('mul(', index)
            if index < 0:
                break
            index += 4
            if index >= len(line):
                break
            ok, a, b, index = parser(line, index)
            #print(ok, correct, index)        
            if ok:
                # a, b = [int(n) for n in "".join(correct).split(",")]
                sum += a * b
    print (sum)
                
                
                

    print("Second")
    sum = 0   
    do = True
    for line in lib.records(3, ''):
        index = 0
        # print (line)
        while True:
            new_index = line.find('mul(', index)
            if new_index < 0:
                break
            new_index += 4
            if new_index >= len(line):
                break
            do_index = line.rfind('do()', index, new_index)
            dont_index = line.rfind("don't()", index, new_index)
            if do_index > dont_index:
                do = True
            elif dont_index > do_index:
                do = False
            index = new_index
            ok, a, b, index = parser(line, index)
            # print(ok, correct, index)      
            if ok and do:
                sum += a * b
    print (sum)


import timeit
print(timeit.timeit(code, number=1))