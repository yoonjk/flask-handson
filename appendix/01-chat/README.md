# Pre-requisites
## step 1 : 아래 명령어를 실행합니다.

```bash
python3 -m venv venv
source .venv/bin/activate
pip install fastapi uvicorn ibm-generative-ai 
source .venv/bin/activate
```

## step 2 : .env 파일 작성
env.example 파일을 .env 파일을로 변경하고 GENAI_KEY/GENAI_API 정보를 입력하고 저장합니다.

GENAI_KEY=aaa
GENAI_API=https://bam-api.res.ibm.com

## step 3 : jinja
**aiofiles**
File Input/Output를 비동기로 할 수 있는 라이브러리

**jinja2**
python에서 가장 많이 사용되는 템플릿 엔진   
- 파이썬 문법(조건, 반복문, 변수)을 간략한 표현으로 데이터를 가공하여 웹페이지에 보임
- 서버에서 받아온 데이터를 보여줄 중간 매체
- 재사용성 용이, 유지보수 용이, 코드 간결성

```bash

pip install aiofiles jinja2
å
```