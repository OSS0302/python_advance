import multiprocessing as mp
# 프로세스에서 실행할 함수

def sub_proccess(name):
    print("[sub] start")
    print(name)
    cp = mp.current_process()
    print(f"[sub] pid : {cp.pid}")
    print("[sub]end")
# 메인 프로세스
if __name__ == "__main__": # 윈도우에만 써야한다.
    print("[main]start")
    p=mp.Process(target=sub_proccess,args=('startcoding',))
    p.start()
    cp = mp.current_process()
    print(f"[main]pid : {cp.pid}")
    print("[main]end")