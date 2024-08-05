abcd = "aaaaaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccddddddddddddeeeeeeeee"

counts = {}
for x in abcd:
    if x in counts:
        counts[x] = counts[x] + 1
    else:
        counts[x] = 1
print(counts)