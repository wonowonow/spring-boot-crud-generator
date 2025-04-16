# Spring Boot CRUD 생성기

이 프로그램은 Spring Boot 프로젝트에서 엔티티 기반의 CRUD 기능을 자동으로 생성해주는 도구입니다. 3-레이어 아키텍처와 헥사고날 아키텍처를 지원합니다.

## 기능

- 도메인별 폴더 구조 자동 생성
- 엔티티, DTO, 리포지토리, 서비스, 컨트롤러 자동 생성
- Java 버전에 따른 코드 최적화 (Java 17+ 버전에서는 Record 클래스 사용)
- 3-레이어 아키텍처 및 헥사고날 아키텍처 지원
- RESTful API 엔드포인트 자동 구현
- 복수형 변환 로직 내장 (Category → Categories, Box → Boxes 등)

## 설치 방법

### 방법 1: pip를 사용한 설치 (권장)

```bash
# 패키지 설치
pip install spring-boot-crud-generator

# 실행
spring-crud
```

### 방법 2: 직접 다운로드

별도의 설치 과정 없이 Python 3.6 이상만 설치되어 있으면 바로 사용할 수 있습니다.

#### 요구사항

- Python 3.6 이상

#### 다운로드 및 실행

1. 이 저장소에서 `crud.py` 파일을 다운로드합니다.
2. 터미널/명령 프롬프트에서 다음 명령어를 실행합니다:

```bash
python crud.py crud
```

## 바로 실행하기 (Git Clone 없이)

1. 다음 명령으로 단일 파일을 다운로드합니다:

```bash
# curl 사용
curl -o crud.py https://raw.githubusercontent.com/wonowonow/spring-boot-crud-generator/main/crud.py

# wget 사용
wget https://raw.githubusercontent.com/wonowonow/spring-boot-crud-generator/main/crud.py
```

2. 다운로드한 파일을 실행합니다:

```bash
python crud.py crud
```

## 사용 방법

1. 프로그램을 실행하면 대화형 프롬프트가 나타납니다.
2. 다음 정보를 입력해야 합니다:
   - 패키지 이름 (예: com.example)
   - 엔티티 이름 (예: Product)
   - Java 버전 (8 이상)
   - 아키텍처 (3-레이어 또는 헥사고날)
3. 확인 후 코드가 자동으로 생성됩니다.

## 생성되는 파일 구조 (Product / 3Layer 생성으로 가정)

```
src/main/java/com/example/domain/Product/
├── controller/
│   └── ProductController.java
├── domain/
│   └── Product.java
├── dto/
│   ├── ProductRequest.java
│   └── ProductResponse.java
├── repository/
│   └── ProductRepository.java
└── service/
    ├── ProductService.java
    └── ProductServiceImpl.java
```

## URL 매핑

생성된 컨트롤러는 다음과 같은 REST API 엔드포인트를 제공합니다:

| HTTP 메서드 | 엔드포인트             | 설명                     |
|----------|----------------------|------------------------|
| POST     | /api/products        | 새 리소스 생성              |
| GET      | /api/products        | 모든 리소스 조회             |
| GET      | /api/products/{id}   | ID로 특정 리소스 조회        |
| PUT      | /api/products/{id}   | ID로 특정 리소스 업데이트     |
| DELETE   | /api/products/{id}   | ID로 특정 리소스 삭제        |

## 참고사항

- 생성된 코드는 기본적인 CRUD 기능만 포함합니다. 필요에 따라 추가 기능을 구현해야 합니다.
- Spring Boot 프로젝트에 다음 의존성이 필요합니다:
  - Spring Web
  - Spring Data JPA
  - Lombok
  - H2 Database (또는 선호하는 다른 데이터베이스)
- Entity 클래스에는 기본적으로 id와 name 필드만 포함되어 있으므로 실제 요구사항에 맞게 수정해야 합니다.

## 당신도 기여할 수 있어요!!!

- 좋은 아이디어가 있으신 분들은 Issue 나 PR 올려주셔서 기여해주시면 감사하겠습니다.

### 👥 Contributors

- 이 프로젝트에 기여해주셔서 감사합니다!

[![Contributors](https://contrib.rocks/image?repo=wonowonow/spring-boot-crud-generator)](https://github.com/wonowonow/spring-boot-crud-generator/graphs/contributors)

## PR로 기여하기
1. GitHub에서 리포지토리를 Fork한다.
2. 내 깃허브 계정으로 복사된 포크 리포지토리를 git clone 한다.
3. 브랜치 생성 후 작업, 커밋한다.
4. 내 포크 리포지토리에 push한다.
5. GitHub에서 Pull Request(PR) 생성하여 원본 리포지토리에 보낸다.
