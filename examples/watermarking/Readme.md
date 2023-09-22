# 프로젝트 개요.
1. Docker 컨테이너 기반 학습환경 만들기.  
2. 학습 관리.
3. 배포.
4. Gradio로 서비스.

##  1. Docker 컨테이너 기반 학습환경 만들기.  
Host server : Ubuntu 20.04 
목적 : GPU (클라우드) 서버에서 라이브러리 관리 및 의존성 문제를 해결하기 위한 컨테이너 생성 및 실행.
수행 내용 :   
Docker container가 gpu를 사용할 수 있도록 nvidia-docker 설치.  
Ubuntu image를 다운 받고, 학습에 필요한 라이브러리 설치.
학습 환경이 마련된 container를 다시 이미지로 만들어서 저장 및 배포.

## 2. 학습 관리.
MLflow를 이용하여, Tracking server를 구축하여 학습과정에서 파라미터에 따른 성능평가 로그 작성 기능 구현.
Tracking server에 아티팩트 및 모델 파일 저장 가능 구현.

## 3. 배포

## 4. 서비스
Gradio를 통해, 이미지와 텍스트를 사용자로부터 입력 받는 UI 구현.
입력받은 이미지와 텍스트를 mlflow api를 통해 watermarking 수행 후 사용자에게 전달.
Decoding의 경우, 사용자가 입력한 이미지를 inference apif를 거쳐 사용자에게 워터마크 메세지 전달.
