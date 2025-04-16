from utils.file import make_dirs, to_path, write_file

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
