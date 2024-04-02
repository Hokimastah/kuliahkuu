import string

n = int(input())
inputs = [input() for _ in range(n)]
charset = string.printable


def timsort(inputs: list[str]):
    longest = len(inputs[0])
    for e in inputs:
        if len(e) > longest:
            longest = len(e)

    def padding(x: str):
        return x.lower() + "0" * (longest - len(x)) if len(x) < longest else x.lower()

    inputs = list(
        map(
            padding,
            inputs,
        )
    )

    for i, e in enumerate(inputs):
        inputs[i] = [[], [charset.index(c) for c in e]]

    # print(inputs)
    for _ in range(longest):
        grouping = {}
        for e in inputs:
            key = ",".join(map(str, e[0]))
            if key not in grouping:
                grouping[key] = [e[1]]
            else:
                grouping[key].append(e[1])
        grouping_i = list(dict.items(grouping))

        for h in grouping_i:
            g = h[1]
            felem_g = [(s[0], s[1:]) for s in g]

            def calculate_minrun(n):
                r = 0
                while n >= 32:
                    r |= n & 1
                    n >>= 1
                return n + r

            minrun = calculate_minrun(len(g))
            chunks = [
                felem_g[i : i + minrun] for i in range(0, len(felem_g), minrun)
            ]  # Split by minrun

            for chunk in chunks:  # Insertion sort
                sorted_chunk = []
                for e in chunk:
                    for i, r in enumerate(sorted_chunk):
                        if r[0] > e[0]:
                            sorted_chunk.insert(i, e)
                            break
                    else:
                        sorted_chunk.append(e)
                chunk[:] = sorted_chunk

            while len(chunks) > 1:
                new_chunks = []
                for i in range(0, len(chunks), 2):  # Merge sort
                    if i < len(chunks) - 1:
                        res = []
                        m, n = 0, 0
                        while m < len(chunks[i]) or n < len(chunks[i + 1]):
                            if m < len(chunks[i]) and (
                                n == len(chunks[i + 1])
                                or chunks[i][m][0] < chunks[i + 1][n][0]
                            ):
                                res.append(chunks[i][m])
                                m += 1
                            elif n < len(chunks[i + 1]):
                                res.append(chunks[i + 1][n])
                                n += 1
                        new_chunks.append(res)
                    else:
                        new_chunks.append(chunks[i])
                chunks = new_chunks

            for nc in chunks:
                for i, c in enumerate(nc):
                    c[1].insert(0, c[0])
                    nc[i] = c[1]

            for c in chunks:
                grouping[h[0]] = c

        # print(grouping)
        grouping_i = list(dict.items(grouping))
        # print(f"eee: {grouping_i}")
        # print(inputs)
        inter = []
        for group in grouping_i:
            for item in group[1]:
                inter.append(
                    [list(filter(bool, group[0].split(","))) + [item[0]], item[1:]]
                )
        # print(inter)
        inputs = inter

    res = []
    for r in inputs:
        res.append("".join(map(lambda x: charset[int(x)] if int(x) != 0 else "", r[0])))
    return res


# testing
# import random
# def random_string(n):
#     return "".join(
#         random.choice(string.ascii_letters) for _ in range(random.randint(5, n))
#     )
# inputs = [random_string(5) for _ in range(250)]

x = list(map(lambda x: x.title(), timsort(inputs)))
for i in x:
    print(i)