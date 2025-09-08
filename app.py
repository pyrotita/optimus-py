import time
import threading
import c_lib


def factorial(n):
    return n
    r = 1

    for i in range(1, n+1):
        r *= i

    return r


def worker(n, n_repetitions):
    print('init--')

    for _ in range(n_repetitions):
        factorial(n)


def c_worker(n, n_repetitions):
    print('init--')

    c_lib.factorial_without_GIL(n, n_repetitions)


if __name__ == '__main__':
    threads = [
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
        threading.Thread(target=worker, args=(20, 500_000)),
    ]

    start = time.perf_counter()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()

    print(end-start)

    c_threads = [
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
        threading.Thread(target=c_worker, args=(20, 500_000_000)),
    ]

    start = time.perf_counter()

    for t in c_threads:
        t.start()

    for t in c_threads:
        t.join()

    end = time.perf_counter()

    print(end-start)

