from concurrent.futures import ThreadPoolExecutor


def f(n):
    d[n] = n**2
    return n  # No need to wrap in list

d = {}
with ThreadPoolExecutor(max_workers=20) as exec:
    master_list = list(exec.map(f, range(1, 10)))

print(master_list)
print(d)