import os
from multiprocessing.dummy import Pool, Manager


def copy_file_worker(file_name, old_folder_name, new_folder_name, queue):
    fr = open(old_folder_name + "/" + file_name, "r")
    fw = open(new_folder_name + "/" + file_name, "w")
    while True:
        content = fr.readline()
        if not content:
            break
        fw.write(content)

    fr.close()
    fw.close()
    queue.put(file_name)


def main():
    old_folder_name = "Test"
    new_folder_name = old_folder_name + "_copy"
    os.mkdir(new_folder_name)
    pool = Pool(5)
    queue = Manager().Queue()
    file_list = os.listdir(old_folder_name)
    file_size = len(file_list)
    for file in file_list:
        pool.apply_async(copy_file_worker, (file, old_folder_name, new_folder_name, queue))
    num = 0
    while num < file_size:
        queue.get()
        num += 1
        print("Copy Rate: %.2f%%" % (num / file_size * 100))
    print("Done!")


if __name__ == '__main__':
    main()
