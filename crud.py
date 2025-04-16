import sys
import time
from utils.input import get_input
from utils.output import print_banner, print_step, print_finish, print_summary
from utils.output import print_section
from generator.entity import generate_entity
from generator.dto import generate_dto
from generator.repository import generate_repository
from generator.service import generate_service_impl, generate_service_interface
from generator.controller import generate_controller

def main():
    # 명령행 인자가 없거나 "crud"가 아닌 경우 안내
    if len(sys.argv) == 1:
        sys.argv.append("crud")
    elif sys.argv[1] != "crud":
        print("❌ 사용법: python crud.py crud")
        return

    print_banner()
    print_section("프로젝트 설정")

    # 1. 패키지 이름 입력 받기
    base_package = get_input("1. 프로젝트의 Base Package를 입력하세요", "com.example")

    # 2. 엔티티 이름 입력 받기
    name = get_input("2. Entity 이름을 입력하세요", "Product")

    # 3. Java 버전 입력 받기
    java_version = 0
    while java_version < 8:
        try:
            version_str = get_input("3. Java 버전 (8 이상)", "17")
            java_version = int(version_str)
            if java_version < 8:
                print("❌ Java 8 이상이어야 합니다.")
        except ValueError:
            print("❌ 숫자를 입력하세요.")

    # 4. 아키텍처 선택
    print("\n아키텍처를 선택하세요:")
    print("  1) 3-레이어 아키텍처")
    print("  2) 헥사고날 아키텍처")

    architecture_choice = ""
    while architecture_choice not in ["1", "2"]:
        architecture_choice = get_input("번호 선택 (1 또는 2)")
        if architecture_choice not in ["1", "2"]:
            print("❌ 1 또는 2 중 하나를 입력하세요.")

    architecture = "3layer" if architecture_choice == "1" else "hexagonal"

    print_summary(architecture, base_package, java_version, name)

    confirm = get_input("위 설정으로 생성할까요? (y/n)", "y").lower()
    if confirm != "y":
        print("❌ 코드 생성이 취소되었습니다.")
        return

    print_section(f"{architecture.upper()} 아키텍처로 CRUD 생성")

    total_steps = 6

    print_step(1, total_steps, "엔티티 클래스 생성 중")
    generate_entity(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_step(2, total_steps, "DTO 클래스 생성 중")
    generate_dto(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_step(3, total_steps, "리포지토리 생성 중")
    generate_repository(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_step(4, total_steps, "서비스 인터페이스 생성 중")
    generate_service_interface(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_step(5, total_steps, "서비스 구현 클래스 생성 중")
    generate_service_impl(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_step(5, total_steps, "컨트롤러 생성 중")
    generate_controller(base_package, name, java_version, architecture)
    time.sleep(0.2)

    print_finish(architecture, name)

if __name__ == "__main__":
    main()
