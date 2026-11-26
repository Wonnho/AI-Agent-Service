from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini", temperature=0,)

#text to analysis

text="""

프로젝트 설명

[수원] AI 마케팅 오케스트레이터 리드 및 개발 (Python/GCP)



1. 개요

 - 삼성전자 AI 개발 프로젝트

  (글로벌 마케팅 멀티 에이전트 오케스트레이터 리딩 및 개발)

 - 리드 1명, 개발 2명 ​

2. 업무내용

 - 프로젝트 기술 리딩 및 개발팀 운영(작업 분해, 담당 배정, 코드 리뷰, 기술 부채/리스크 관리)

 - 일정/마일스톤 관리(Mock-first 개발 → 고객 MCP 실연동 전환 → UAT 리허설 단계별 진척 관리)

 - 릴리스 게이트 운영 및 품질 책임(CI/CD 파이프라인 승인, 15분 이내 롤백 관리, 비기능 목표 검증)

 - 고객 커뮤니케이션 및 연동 선행조건 관리(미결 과제 협의, 고객 MCP 서버 연동 승인, IAM/네트워크 요건 조율)

 - 거버넌스 가드 준수 관리(운영 배포 및 실제 집행/발송 경로 금지, 합성/가상 데이터 원칙 등 납품 범위 관리)

 - 서브에이전트(멤버) 및 입력 빌더 구현(Google ADK BaseAgent 기반 개발, 공통 계약 준수, 사실 추출 및 출처 기록)

 - Mock 멤버 → 실제 연동 전환(설정 기반 MCP 래퍼로 고객 non-prod MCP 서버 연동, 에이전트 온보딩)

 - Backend API 및 Frontend 개발(OpenAPI 명세 기반 엔드포인트, RBAC, Vite + TypeScript 기반 화면/뷰어/브리핑 플레이어)

 - 멤버 런타임 배포/관측 및 테스트 자동화(Cloud Run 배포, GCS 산출물 저장, OpenTelemetry 계측, 단위/Smoke/Playwright E2E 테스트)


3. 자격요건

 - 경력: 고급 (리드 1명, 개발 2명)

 - (필수) Python 기반 백엔드/API 개발 및 코드 리뷰 실무 역량

 - (필수) LLM 기반 애플리케이션 또는 AI 에이전트 개발 경험 (리드 5년 이상 / 개발 1년 이상)

 - (필수) 개발 리드/PL 경력 5년 이상 및 대기업 SI 고객 커뮤니케이션/범위 관리 경험 (리드 포지션 한정)

 - (필수) REST API 설계/구현 및 OpenAPI 명세 기반 개발 경험

 - (필수) 클라우드(GCP 우선, AWS/Azure 가능) 및 컨테이너 서비스(Cloud Run, ECS, Kubernetes 등) 설계/배포 경험

 - (필수) Git 협업, 단위/E2E 테스트 전략 및 CI/CD 기반 프로젝트 관리 경험

 - (우대) Google ADK, Vertex AI(Agent Engine, Gemini) 기반 프로젝트 리딩 또는 사용 경험

 - (우대) 멀티 에이전트 오케스트레이션, MCP/A2A 프로토콜 구현/적용 경험

 - (우대) Firestore, Cloud Tasks, GCS 등 GCP 매니지드 서비스 및 OpenTelemetry 계측 경험

 - (우대) TypeScript/Vite 기반 SPA 개발 및 Playwright E2E 테스트 경험

 - (우대) Human-in-the-loop 승인 흐름, 비용 상한/Kill switch 등 AI 거버넌스 운영 경험

 - (우대) 마케팅/광고/캠페인 도메인 이해 및 글로벌 조직 프로젝트/영어 커뮤니케이션 가능자​

4. 계약조건

 - 기간: 12월~1월 사업 진행 후, 연단위 예정 (2026.12~2028.01.31) 

 - 장소: 수원

 - 급여: 세전 850~1,000만원 (개발~리드) 예상

"""

#template ​

templates= {

    "summary":ChatPromptTemplate.from_messages([

    ("system"," You are a summary technician. answer in korean"),

    ("human","summarize {text}"),

    ]),

    "sentiment analysis" : ChatPromptTemplate.from_messages([

          ("system"," You are a sentiment analyst. answer in korean"),

    ("human","analyze the tone and overall sentiment(positive/negative/neutral) on {text}"),

    ]),

    "content creator": ChatPromptTemplate.from_messages([

          ("system"," You are a content creator. answer in korean"),

    ("human","re-create {text} at the advanced level"),

    ]),

}


# for purpose,tmpl in templates.items():

#     message=tmpl.format_messages(text=text)

#     response=llm.invoke(message)

#     print(f"[{purpose}]\n {response.content}\n")



for purpose, tmpl in templates.items():

      print("purpose:",purpose)

      print("tmpl type:",type(tmpl)) # <class '...ChatPromptTemplate'>

      print("input variables:", tmpl.input_variables) # ['text']

      print("tmpl messages:",tmpl.messages) # the message template list