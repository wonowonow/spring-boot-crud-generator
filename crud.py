import os
import sys
import time

def make_dirs(path):
    os.makedirs(path, exist_ok=True)

def to_path(package):
    return package.replace(".", "/")

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

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

def get_input(prompt, default=None):
    if default:
        result = input(f"{prompt} [{default}]: \n> ")
        return result if result else default
    return input(f"{prompt}: \n> ")

def get_plural(word):
    """단어의 복수형을 반환합니다."""
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith('s') or word.endswith('x') or word.endswith('z') or word.endswith('ch') or word.endswith('sh'):
        return word + 'es'
    else:
        return word + 's'

def generate_entity(base_package, name, java_version, architecture):
    path = f"src/main/java/{to_path(base_package)}/domain/{name}/domain"
    make_dirs(path)
    file_path = f"{path}/{name}.java"
    
    content = f"""package {base_package}.domain.{name}.domain;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class {name} {{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
}}
"""
    write_file(file_path, content)
    print_success(f"생성됨: {file_path}")

def generate_dto(base_package, name, java_version, architecture):
    dto_path = f"src/main/java/{to_path(base_package)}/domain/{name}/dto"
    make_dirs(dto_path)
    
    # Request DTO
    request_path = f"{dto_path}/{name}Request.java"
    if java_version >= 17:
        request_content = f"""package {base_package}.domain.{name}.dto;

public record {name}Request(
    String name
) {{
}}
"""
    else:
        request_content = f"""package {base_package}.domain.{name}.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {name}Request {{
    private String name;
}}
"""
    write_file(request_path, request_content)
    print_success(f"생성됨: {request_path}")
    
    # Response DTO
    response_path = f"{dto_path}/{name}Response.java"
    if java_version >= 17:
        response_content = f"""package {base_package}.domain.{name}.dto;

public record {name}Response(
    Long id,
    String name
) {{
}}
"""
    else:
        response_content = f"""package {base_package}.domain.{name}.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {name}Response {{
    private Long id;
    private String name;
}}
"""
    write_file(response_path, response_content)
    print_success(f"생성됨: {response_path}")

def generate_repository(base_package, name, java_version, architecture):
    if architecture == "hexagonal":
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/repository"
        make_dirs(path)
        file_path = f"{path}/{name}Repository.java"
        content = f"""package {base_package}.domain.{name}.repository;

import {base_package}.domain.{name}.domain.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    else:
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/repository"
        make_dirs(path)
        file_path = f"{path}/{name}Repository.java"
        content = f"""package {base_package}.domain.{name}.repository;

import {base_package}.domain.{name}.domain.{name};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    write_file(file_path, content)
    print_success(f"생성됨: {file_path}")

def generate_service_interface(base_package, name, java_version, architecture):
    name_plural = get_plural(name)
    
    if architecture == "hexagonal":
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}Service.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;

import java.util.List;

public interface {name}Service {{
    {name}Response create{name}({name}Request request);
    List<{name}Response> get{name_plural}();
    {name}Response get{name}ById(Long id);
    {name}Response update{name}(Long id, {name}Request request);
    void delete{name}(Long id);
}}
"""
    else:
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}Service.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;

import java.util.List;

public interface {name}Service {{
    {name}Response create{name}({name}Request request);
    List<{name}Response> get{name_plural}();
    {name}Response get{name}ById(Long id);
    {name}Response update{name}(Long id, {name}Request request);
    void delete{name}(Long id);
}}
"""
    write_file(file_path, content)
    print_success(f"생성됨: {file_path}")

def generate_service_impl(base_package, name, java_version, architecture):
    name_plural = get_plural(name)
    
    if architecture == "hexagonal":
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}ServiceImpl.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.service.{name}Service;
import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;
import {base_package}.domain.{name}.repository.{name}Repository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class {name}ServiceImpl implements {name}Service {{

    private final {name}Repository repository;

    @Override
    public {name}Response create{name}({name}Request request) {{
        {name} entity = {name}.builder()
                .name(request.name())
                .build();
        {name} saved = repository.save(entity);
        return new {name}Response(saved.getId(), saved.getName());
    }}

    @Override
    public List<{name}Response> get{name_plural}() {{
        return repository.findAll().stream()
                .map(entity -> new {name}Response(entity.getId(), entity.getName()))
                .collect(Collectors.toList());
    }}

    @Override
    public {name}Response get{name}ById(Long id) {{
        {name} entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        return new {name}Response(entity.getId(), entity.getName());
    }}

    @Override
    public {name}Response update{name}(Long id, {name}Request request) {{
        {name} entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        entity.setName(request.name());
        {name} updated = repository.save(entity);
        return new {name}Response(updated.getId(), updated.getName());
    }}

    @Override
    public void delete{name}(Long id) {{
        repository.deleteById(id);
    }}
}}
"""
    else:
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}ServiceImpl.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;
import {base_package}.domain.{name}.repository.{name}Repository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class {name}ServiceImpl implements {name}Service {{

    private final {name}Repository repository;

    @Override
    public {name}Response create{name}({name}Request request) {{
        {name} entity = {name}.builder()
                .name(request.name())
                .build();
        {name} saved = repository.save(entity);
        return new {name}Response(saved.getId(), saved.getName());
    }}

    @Override
    public List<{name}Response> get{name_plural}() {{
        return repository.findAll().stream()
                .map(entity -> new {name}Response(entity.getId(), entity.getName()))
                .collect(Collectors.toList());
    }}

    @Override
    public {name}Response get{name}ById(Long id) {{
        {name} entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        return new {name}Response(entity.getId(), entity.getName());
    }}

    @Override
    public {name}Response update{name}(Long id, {name}Request request) {{
        {name} entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        entity.setName(request.name());
        {name} updated = repository.save(entity);
        return new {name}Response(updated.getId(), updated.getName());
    }}

    @Override
    public void delete{name}(Long id) {{
        repository.deleteById(id);
    }}
}}
"""
    write_file(file_path, content)
    print_success(f"생성됨: {file_path}")

def generate_controller(base_package, name, java_version, architecture):
    name_lower = name.lower()
    name_plural = get_plural(name)
    path_name = get_plural(name_lower)
    
    if architecture == "hexagonal":
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/controller"
        make_dirs(path)
        file_path = f"{path}/{name}Controller.java"
        content = f"""package {base_package}.domain.{name}.controller;

import {base_package}.domain.{name}.service.{name}Service;
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/{path_name}")
public class {name}Controller {{

    private final {name}Service service;

    @PostMapping
    public ResponseEntity<{name}Response> create{name}(@RequestBody {name}Request request) {{
        return ResponseEntity.ok(service.create{name}(request));
    }}

    @GetMapping
    public ResponseEntity<List<{name}Response>> get{name_plural}() {{
        return ResponseEntity.ok(service.get{name_plural}());
    }}

    @GetMapping("/{{id}}")
    public ResponseEntity<{name}Response> get{name}ById(@PathVariable Long id) {{
        return ResponseEntity.ok(service.get{name}ById(id));
    }}

    @PutMapping("/{{id}}")
    public ResponseEntity<{name}Response> update{name}(@PathVariable Long id, @RequestBody {name}Request request) {{
        return ResponseEntity.ok(service.update{name}(id, request));
    }}

    @DeleteMapping("/{{id}}")
    public ResponseEntity<Void> delete{name}(@PathVariable Long id) {{
        service.delete{name}(id);
        return ResponseEntity.noContent().build();
    }}
}}
"""
    else:
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/controller"
        make_dirs(path)
        file_path = f"{path}/{name}Controller.java"
        content = f"""package {base_package}.domain.{name}.controller;

import {base_package}.domain.{name}.service.{name}Service;
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/{path_name}")
public class {name}Controller {{

    private final {name}Service service;

    @PostMapping
    public ResponseEntity<{name}Response> create{name}(@RequestBody {name}Request request) {{
        return ResponseEntity.ok(service.create{name}(request));
    }}

    @GetMapping
    public ResponseEntity<List<{name}Response>> get{name_plural}() {{
        return ResponseEntity.ok(service.get{name_plural}());
    }}

    @GetMapping("/{{id}}")
    public ResponseEntity<{name}Response> get{name}ById(@PathVariable Long id) {{
        return ResponseEntity.ok(service.get{name}ById(id));
    }}

    @PutMapping("/{{id}}")
    public ResponseEntity<{name}Response> update{name}(@PathVariable Long id, @RequestBody {name}Request request) {{
        return ResponseEntity.ok(service.update{name}(id, request));
    }}

    @DeleteMapping("/{{id}}")
    public ResponseEntity<Void> delete{name}(@PathVariable Long id) {{
        service.delete{name}(id);
        return ResponseEntity.noContent().build();
    }}
}}
"""
    write_file(file_path, content)
    print_success(f"생성됨: {file_path}")

def process_with_animation(total_steps):
    for i in range(1, total_steps + 1):
        print_step(i, total_steps, f"처리 중")
        time.sleep(0.3)  # 애니메이션 효과를 위한 지연

def main():
    # 명령행에서 직접 호출될 때와 pip로 설치 후 spring-crud로 호출될 때 모두 동작하도록 수정
    if len(sys.argv) > 1 and sys.argv[1] == "crud":
        # crud 인자가 있으면 기존 방식대로 작동
        pass
    elif len(sys.argv) == 1:
        # pip로 설치 후 spring-crud로 실행될 때는 sys.argv가 ['crud.py']만 포함
        # 이 경우 자동으로 crud 인자가 있는 것처럼 동작
        sys.argv.append("crud")
    else:
        print("사용법: python crud.py crud")
        return

    print_banner()
    
    print_section("프로젝트 설정")
    
    # 1. 패키지 이름 입력 받기
    base_package = get_input("1. 프로젝트 이름 Package name을 입력하세요", "com.example")
    
    # 2. 엔티티 이름 입력 받기
    name = get_input("2. 만드려는 Entity 이름을 입력하세요", "Product")
    
    # 3. Java 버전 입력 받기
    java_version = 0
    while java_version < 8:
        try:
            java_version_str = get_input("3. Java 버전을 입력하세요 (8 이상)", "17")
            java_version = int(java_version_str)
            if java_version < 8:
                print("❌ Java 버전은 8 이상이어야 합니다.")
        except ValueError:
            print("❌ 숫자를 입력하세요.")
    
    # 4. 아키텍처 선택
    print("\n아키텍처를 선택하세요:")
    print("  1) 3-레이어 아키텍처 (기본 MVC)")
    print("  2) 헥사고날 아키텍처 (포트 및 어댑터)")
    
    architecture_choice = ""
    while architecture_choice not in ["1", "2"]:
        architecture_choice = get_input("번호 선택")
        if architecture_choice not in ["1", "2"]:
            print("❌ 1 또는 2 중 하나를 입력하세요.")
    
    architecture = "3layer" if architecture_choice == "1" else "hexagonal"
    
    # 설정 정보 보여주기
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  🔹 패키지명: {base_package}")
    print(f"  🔹 엔티티: {name}")
    print(f"  🔹 Java 버전: {java_version}" + (" (Record 클래스 사용)" if java_version >= 17 else ""))
    print(f"  🔹 아키텍처: {'3-레이어' if architecture == '3layer' else '헥사고날'}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    confirm = get_input("\n위 설정으로 코드를 생성하시겠습니까? (y/n)", "y").lower()
    if confirm != "y":
        print("❌ 코드 생성이 취소되었습니다.")
        return
    
    print_section(f"{architecture.upper()} 아키텍처로 {name} 엔티티에 대한 CRUD 생성 시작")
    
    # 진행 상황 표시
    total_steps = 6
    
    print_step(1, total_steps, "엔티티 클래스 생성 중")
    generate_entity(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    print_step(2, total_steps, "DTO 클래스 생성 중")
    generate_dto(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    print_step(3, total_steps, "리포지토리 인터페이스 생성 중")
    generate_repository(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    print_step(4, total_steps, "서비스 인터페이스 생성 중")
    generate_service_interface(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    print_step(5, total_steps, "서비스 구현 클래스 생성 중")
    generate_service_impl(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    print_step(6, total_steps, "컨트롤러 클래스 생성 중")
    generate_controller(base_package, name, java_version, architecture)
    time.sleep(0.2)
    
    # 완료 메시지
    print("\n")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                                            ┃")
    print("┃   🎉  코드 생성이 완료되었습니다!                                          ┃")
    print("┃                                                                            ┃")
    print(f"┃   {architecture.upper()} 아키텍처를 사용한 {name} 엔티티의 CRUD 코드가 생성되었습니다.{' ' * (24 - len(architecture) - len(name))}┃")
    print("┃                                                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

if __name__ == "__main__":
    main()