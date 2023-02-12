import threading
import time
# 주식 자동매매
# 매수,매도
# 매수 스레드
def buyer():
    for i in range(5):
        print("[매수]데이터 요청중")
        time.sleep(1)
        print("[매수]데이터 분석중")
        time.sleep(1)
        print("[매수] 손절각 ")
        time.sleep(1)
        print("[매수] 풀 매수 들가즈아")
        time.sleep(1)
# 메도 스레드
def seller():
    for i in range(5):
        print("[매도]데이터 요청중")
        time.sleep(1)
        print("[매도]데이터 분석중")
        time.sleep(1)
        print("[매도]오 지금이 매수할 타이밍인가")
        time.sleep(1)
        print("[매도] 풀 매수 들가즈아")
        time.sleep(1)
# 메인 스레등
print("[메인]start")
buyer = threading.Thread(target=buyer)
seller= threading.Thread(target=seller)

buyer.start()
seller.start()

buyer.join()# 매수 스레드가 종료될떄까지 메인스레드가 기다린다.
seller.join()# 매도 스레드가 종료될떄까지 메인스레드가 기다린다.
print("[메인]장이 종료되었습니다.")