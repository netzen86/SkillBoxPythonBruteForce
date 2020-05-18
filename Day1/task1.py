import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def poll_site(url):
    retry = 0
    while retry != 100:
        with session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Site {url} response {response.status_code} try {retry}")
            retry += 1


def poll_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(poll_site, sites)


if __name__ == "__main__":
    sites = [ "https://www.python.org", "https://google.com", "https://uchi.ru", "https://github.com/", "https://www.yaklass.ru/"]
    start_time = time.time()
    poll_all_sites(sites)
    duration = time.time() - start_time
    print(f"Pinging {len(sites)} in {duration} seconds")