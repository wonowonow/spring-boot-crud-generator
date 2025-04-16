from utils.file import make_dirs, to_path, write_file

def generate_repository(base_package, name, java_version, architecture):
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
