from threading import Thread, Lock
import time
import random


mil_second_start = 15
mil_second_end = 20
unit = 1000


# Work function for child thread
def job(lock, job_num, result):
    seconds = random.randrange(mil_second_start*unit, mil_second_end*unit)/unit
    time.sleep(seconds)  # simulate each job different execution time
    print('    -- job ' + str(job_num))
    with lock:
        result.append(job_num)  # for comparison with original list


def get_list_n_elem_each_time_gen(input_list, n):
    for elem in range(0, len(input_list), n):
        yield input_list[elem:elem + n]


def check_list_is_same(org_list, result_list):
    for li in org_list:
        if li not in result_list:
            print('Elem missing.')
            input()  # pause
            return False
    return True


def threads_demo():
    job_num_list = list(range(1, 500))
    result_list = []
    step = 24
    list_n_elem_slices = get_list_n_elem_each_time_gen(job_num_list, step)
    for slice_index, list_n_elem_slice in enumerate(list_n_elem_slices):
        lock = Lock()
        threads = []
        # print("Threads build & start...")
        print('-- slice ' + str(slice_index))
        for job_index, job_num in enumerate(list_n_elem_slice):
            threads.append(Thread(target=job, args=(lock, job_num, result_list)))
            threads[job_index].start()
        # print("Waiting for all threads done...")
        for job_index, job_num in enumerate(list_n_elem_slice):
            threads[job_index].join()
        # print("All threads done.")
    check_list_is_same(job_num_list, result_list)
    print("Done.")


if __name__ == '__main__':
    threads_demo()

