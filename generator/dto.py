from utils.file import make_dirs, to_path, write_file

def generate_dto(base_package, name, java_version, architecture):
    dto_path = f"src/main/java/{to_path(base_package)}/domain/{name}/dto"
    make_dirs(dto_path)

    # Request
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

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {name}Request {{
    private String name;
}}
"""
    write_file(request_path, request_content)

    # Response
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

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {name}Response {{
    private Long id;
    private String name;
}}
"""
    write_file(response_path, response_content)
