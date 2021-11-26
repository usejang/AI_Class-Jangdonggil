머신 러닝 교과서 2판


##  6장: 모델 평가와 하이퍼파라미터 튜닝의 모범 사례

### 목차

- 파이프라인을 사용한 효율적인 워크플로
  - 위스콘신 유방암 데이터셋
  - 파이프라인으로 변환기와 추정기 연결
- k-겹 교차 검증을 사용한 모델 성능 평가
  - 홀드아웃 방법
  - k-겹 교차 검증
- 학습 곡선과 검증 곡선을 사용한 알고리즘 디버깅
  - 학습 곡선으로 편향과 분산 문제 분석
  - 검증 곡선으로 과대적합과 과소적합 조사
- 그리드 서치를 사용한 머신 러닝 모델 세부 튜닝
  - 그리드 서치를 사용한 하이퍼파라미터 튜닝
  - 중첩 교차 검증을 사용한 알고리즘 선택
- 여러 가지 성능 평가 지표
  - 오차 행렬
  - 분류 모델의 정밀도와 재현율 최적화
  - ROC 곡선 그리기
  - 다중 분류의 성능 지표
- 불균형한 클래스 다루기
- 요약

### 코드 사용 방법 안내

이 책의 코드를 사용하는 가장 좋은 방법은 주피터 노트북(`.ipynb` 파일)입니다. 주피터 노트북을 사용하면 단계적으로 코드를 실행하고 하나의 문서에 편리하게 (그림과 이미지를 포함해) 모든 출력을 저장할 수 있습니다.

![](../ch02/images/jupyter-example-1.png)

주피터 노트북은 매우 간단하게 설치할 수 있습니다. 아나콘다 파이썬 배포판을 사용한다면 터미널에서 다음 명령을 실행하여 주피터 노트북을 설치할 수 있습니다:

    conda install jupyter notebook

다음 명령으로 주피터 노트북을 실행합니다.

    jupyter notebook

브라우저에서 윈도우가 열리면 원하는 `.ipynb`가 들어 있는 디렉토리로 이동할 수 있습니다.

**설치와 설정에 관한 더 자세한 내용은 1장의 [README.md 파일](../ch01/README.md)에 있습니다.**

**(주피터 노트북을 설치하지 않았더라도 깃허브에서 [`ch06.ipynb`](https://github.com/rickiepark/python-machine-learning-book-3rd-edition/blob/master/ch06/ch06.ipynb)을 클릭해 노트북 파일을 볼 수 있습니다.)**.

코드 예제 외에도 주피터 노트북에는 책의 내용에 맞는 섹션 제목을 함께 실었습니다. 또한 주피터 노트북에 원본 이미지와 그림을 포함시켰기 때문에 책을 읽으면서 코드를 쉽게 따라할 수 있으면 좋겠습니다.

![](../ch02/images/jupyter-example-2.png)