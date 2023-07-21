# How to use GPU with Lambda lab.
GCP나 Amazon 등에서 gpu 인스턴스를 제공하고 있지만, 학생이 사용하기에는 너무 비싼 느낌이 있다.

우연히 tensorflow korea에서  lambda lab이 싸게 GPU instance를 제공한다는 것을 알게되어서, 사이드 프로젝트를 위한 GPU서버로 선택하였다.

## Create Instance (인스턴스 생성)
GPU를 사용하기 위해서는 instance를 생성해야 한다.
![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/33c5a645-4d01-49f4-a9c2-2076cf46743b)

아직 lambda lab에 친숙하지 않기 때문에 혹시모를 요금폭탄을 조심하기 위해서(?) A10 인스턴스를 선택했다.

인스턴스를 생성하면 
![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/b5746474-2fb2-4b2d-b5d8-c521ff30b17d)

위와같은 상태창을 볼 수 있다.
부팅이 끝나면 ssh를 통해 접속할 수 있으며, 사용할 일이 끝난 이후에는 꼭 terminate를 눌러서 인스턴스를 종료해야 한다.

## SSH로 접속
### Window ssh
powershell에서 사용할 수 있는 ssh를 통해 instance에 접속하는 예시이다.
이때 ssh key 파일이 pem 파일 형식으로 제공되기 때문에 -i인자로 pem 파일을 줌으로써 ssh로 instance에 접속할 수 있다.

```
ssh name@ip -i key.pem
```
![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/4d3c8205-9986-47a1-ba69-e940677f68ba)

접속을 하게 되면 instance를 사용할 수 있게되는데, docker는 깔려있지만 anaconda는 없는 것으로 보인다.
따라서 원하는 개발 환경을 docker 이미지로 생성해서 해당 인스턴스에 띄워야겠다는 생각을 했다. (해당 내용은 추후 추가 예정)

기본적으로 서버에 설치되어 있는 cuda 및 python, pytorch 정보는 다음과 같다.

![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/2b5caba8-5b57-49d4-ba42-2e050c98aa4e)

## Instance 종료
사용을 다 했으면, 클라우드 자원을 반납해야한다.
이때, 데이터는 모두 삭제되니 lambda lab storage와 연동하거나, 매번 필요한 데이터를 업로드 해야할 것 같다.
이는 도커파일로 만들어서 저장해서 관리하면 유용할 것 같다. 하지만, 파일 업/다운로드에 걸리는 시간에 대한 클라우드 사용 요금은 조금 마음이 아프게 다가온다..

![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/244d15d2-a315-43a5-8289-5cd82cc435ff)

인스턴스를 종료하고 나면 Usage 탭에서 사용 내역을 확인할 수 있다.
주기적으로 모니터링해서 클라우드 사용 요금을 적게 내도록 관리를 해야겠다.

![image](https://github.com/Bosung-Yang/DeepLearning/assets/139629920/fa16aa77-f817-4f0c-b8ce-82395796bc66)




