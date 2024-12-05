import numpy as np
import lib
# note first and second are combined
def code():
    precedences = np.zeros((100, 100), dtype='int')
    print("First")
    records = lib.records(5, '')
    rule_set = set()
    bad_updates = list()
    for rule in records:
        if rule.strip() == "":
            break
        before, after = [int(x) for x in rule.split('|')]
        rule_set.add((after, before))
        #print(before, after)
        precedences[after, before] = 1
    
    result = 0
    for update in records:
        pages = np.fromstring(update, dtype='int', sep=',')
        blocked = np.zeros(100, dtype='int')
        for page in pages:
            if blocked[page]:
                bad_updates.append(pages)
                break
            blocked = blocked + precedences[page]
        else:
            result += pages[pages.shape[0] // 2]
            
    print(result)
    print("Second")
    result = 0
    for update in [x.tolist() for x in bad_updates]:
        # bubble sort
        l = len(update)
        for i in range(l - 1, l  // 2 - 1, -1):
            for j in range(0, i):
                if (update[j], update[j+1]) in rule_set:
                    #swap
                    update[j], update[j+1] = update[j+1], update[j]
        # print(update)
        result += update[l // 2]
    
    
    print (result)
import timeit
print(timeit.timeit(code, number=1))