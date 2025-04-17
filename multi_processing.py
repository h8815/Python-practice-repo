import multiprocessing
import requests  # type: ignore

def downloadFiles(url, name):
    print(f"Start Downloading photo{name}")
    response = requests.get(url)
    open(f"photos/photo{name}.jpg", "wb").write(response.content)
    print(f"Finish Downloading photo{name}")
if __name__ == "__main__" :

    url = "https://picsum.photos/2000/3000"
    process_join = []

    for i in range(5):
        procs = multiprocessing.Process(target=downloadFiles, args=(url,i))
        procs.start()
        process_join.append(procs)

    for _ in process_join:
        procs.join()
