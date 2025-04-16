def print_banner():
    print("\n\n")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                                            ┃")
    print("┃   █▀▀ █▀█ █░█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█                   ┃")
    print("┃   █▄▄ █▀▄ █▄█ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄                   ┃")
    print("┃                                                                            ┃")
    print("┃   Spring Boot 엔티티 기반 CRUD 코드 생성기                                 ┃")
    print("┃                                                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\n")

def print_success(message):
    print(f"✅ {message}")

def print_section(message):
    print(f"\n━━━ {message} ━━━\n")

def print_step(step, total, message):
    print(f"[{step}/{total}] {message}...")

def print_summary(architecture, base_package, java_version, name):
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔹 패키지명: {base_package}")
    print(f"🔹 엔티티명: {name}")
    print(f"🔹 Java 버전: {java_version}")
    print(f"🔹 아키텍처: {'3레이어' if architecture == '3layer' else '헥사고날'}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def print_finish(architecture, name):
    print("\n")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                                            ┃")
    print("┃   🎉  코드 생성이 완료되었습니다!                                          ┃")
    print("┃                                                                            ┃")
    print(f"┃   {architecture.upper()} 아키텍처를 사용한 {name} 엔티티의 CRUD 코드가 생성되었습니다.{' ' * (24 - len(architecture) - len(name))}┃")
    print("┃                                                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")