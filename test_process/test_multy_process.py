import logging as log
import atexit
import concurrent.futures
from driver import driver_test

pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)

@atexit.register
def sig_handler():
    log.info("try to dispose process pool")
    pool.shutdown(wait=True)
    log.info("finish dispose")

def main():

    futures = []
    futures.append(pool.submit(driver_test))
    futures.append(pool.submit(driver_test))

    for future in futures:
        try:
            result = future.result()
            log.info(result)  # check success or error
        except Exception as e:
            log.error(e)

if __name__ == '__main__':
    main()