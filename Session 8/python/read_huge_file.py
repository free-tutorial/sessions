from tqdm import tqdm

path = "/home/ali/personal/mentorship/huge-file.txt"

with open(path) as f:
    my_bytes = 0
    words = set()
    pbar = tqdm(f)
    for line in pbar:
        words.update(line.rstrip().split(" "))
        my_bytes += len(line)
        pbar.set_description(f"{my_bytes//1000000} MB processed")
