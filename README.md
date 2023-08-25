# async_process_test
단순히 순차로 프린트만 찍는 테스트라,
제어권 넘겨 줄 때 시간 소요 때문에 2번 방법이 제일 빠를 줄 알았으나
당연한 결과가 나옴

## benchmark
------------
1. run_in_executor Process + async loop
2. run_in_executor Process + loop
3. Process + async loop
4. Process + loop
