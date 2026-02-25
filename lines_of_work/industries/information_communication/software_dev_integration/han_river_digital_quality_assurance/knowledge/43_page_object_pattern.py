title = "Page Object 패턴"

content = """
Page Object 패턴은 UI 자동화에서 페이지 구조를 별도 객체로 분리하는 설계 패턴입니다. 유지보수성을 크게 향상시킵니다.

**구조**: 각 페이지(또는 컴포넌트)를 클래스로 정의하고, locator와 동작 메서드를 캡슐화합니다. 테스트는 Page Object 메서드만 호출합니다.

**효과**: UI 변경 시 Page Object만 수정하면 됩니다. 테스트 코드는 비즈니스 로직에 집중합니다.

**확장**: Component Object, Facade 등으로 재사용 가능한 블록을 만듭니다. 한강 디지털의 Selenium 프로젝트 표준입니다.
"""  # noqa: E501

version = "0.0.1"
