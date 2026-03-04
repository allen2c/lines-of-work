title = "클라우드 통합"

content = """
AWS, GCP, Naver Cloud, Azure 등 클라우드 서비스와의 통합은 관리형 컴포넌트를
활용해 빠르게 구축할 수 있습니다. 리전, 네트워크, 비용을 고려해 설계합니다.

**관리형 서비스:** 큐(SQS, Pub/Sub), 스트리밍(Kinesis, Dataflow), 함수
(Lambda, Cloud Functions)를 조합합니다. IaC(Terraform, CloudFormation)로
인프라를 버전 관리합니다.

**연결 옵션:** VPC 피어링, PrivateLink로 사설 연결을 구성할 수 있습니다.
퍼블릭 API는 API Gateway와 WAF로 보호합니다. 멀티 클라우드 시 메시징
프로토콜(AMQP, MQTT) 표준을 활용해 벤더 종속성을 줄입니다.
"""  # noqa: E501

version = "0.0.1"
