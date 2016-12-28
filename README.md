# machineLearnigAlgorithm


1. kNN Algorithm
- 장점
    - 높은 정확도
    - 오류데이터에 둔감
    - 데이터에 대한 가정이 없음
- 단점
    - 계산비용이 높음
    - 많은 메모리 요구
- 적용
    - 수치형
    - 명목형

- 기본 개념
   - 훈련집합의 모든 데이터에 '분류항목'이 존재하며 훈련집합의 분류항목을 통해 새로운 데이터를 학습시키는 알고리즘.
   - 분류 항목이 없는 새로운 데이터의 학습법
        - 이미 분류항목을 알고있는 데이터 집합에서 상위 k개를 뽑아 다수결을 통해 결정한다.

- 예제 상황
    - 영화의 장르를 구분한다. (로맨스, 액션)
    - 두 장르의 feature로는 발차기횟수, 키스횟수로만 한다.