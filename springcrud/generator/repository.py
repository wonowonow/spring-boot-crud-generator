from springcrud.utils.file import make_dirs, to_path, write_file

def generate_repository(base_package, name, java_version, architecture):
    if architecture == "hexagonal":
        # 포트 (인터페이스) 생성
        port_path = f"src/main/java/{to_path(base_package)}/domain/{name}/port/out"
        make_dirs(port_path)
        port_file_path = f"{port_path}/{name}Port.java"
        port_content = f"""package {base_package}.domain.{name}.port.out;

import {base_package}.domain.{name}.domain.{name};
import java.util.List;
import java.util.Optional;

public interface {name}Port {{
    {name} save({name} entity);
    List<{name}> findAll();
    Optional<{name}> findById(Long id);
    void deleteById(Long id);
}}
"""
        write_file(port_file_path, port_content)

        # 어댑터 (구현체) 생성
        adapter_path = f"src/main/java/{to_path(base_package)}/domain/{name}/infrastructure/adapter/out/persistence"
        make_dirs(adapter_path)
        adapter_file_path = f"{adapter_path}/{name}PersistenceAdapter.java"
        adapter_content = f"""package {base_package}.domain.{name}.infrastructure.adapter.out.persistence;

import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.port.out.{name}Port;
import {base_package}.domain.{name}.repository.{name}Repository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

@Component
@RequiredArgsConstructor
public class {name}PersistenceAdapter implements {name}Port {{

    private final {name}Repository repository;

    @Override
    public {name} save({name} entity) {{
        return repository.save(entity);
    }}

    @Override
    public List<{name}> findAll() {{
        return repository.findAll();
    }}

    @Override
    public Optional<{name}> findById(Long id) {{
        return repository.findById(id);
    }}

    @Override
    public void deleteById(Long id) {{
        repository.deleteById(id);
    }}
}}
"""
        write_file(adapter_file_path, adapter_content)

    # 표준 Repository 생성
    path = f"src/main/java/{to_path(base_package)}/domain/{name}/repository"
    make_dirs(path)
    file_path = f"{path}/{name}Repository.java"

    content = f"""package {base_package}.domain.{name}.repository;

import {base_package}.domain.{name}.domain.{name};
import org.springframework.data.jpa.repository.JpaRepository;

public interface {name}Repository extends JpaRepository<{name}, Long> {{
}}
"""
    write_file(file_path, content)
