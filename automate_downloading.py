import os
import requests

def download_content():
    response = requests.get(url)
    open(f"C:\\Users\\Himanshu\\Documents\\programs\\python\\photos\\mydir\\folder_{i}\\photo_{j}.jpg", "wb").write(response.content)

if __name__ == "__main__" : 
    no_of_folder = 5
    no_of_photos = 2
    url = "https://picsum.photos/1920/1080"

    for i in range(1,no_of_folder+1):
        os.mkdir(f"C:\\Users\\Himanshu\\Documents\\programs\\python\\photos\\mydir\\folder_{i}")
        for j in range(1,no_of_photos+1):
            print(f"Start Downloading photo_{j} in folder_{i}")
            download_content()
        print(f"--> Finish Downloading photos in folder_{i}\n")

    print("\n-x-x-x-x-x-x-x-x-Work Done-x-x-x-x-x-x-x-x")