from springcrud.utils.file import make_dirs, to_path, write_file
from springcrud.utils.input import get_plural

def generate_controller(base_package, name, java_version, architecture):
    name_lower = name.lower()
    plural = get_plural(name)
    path_name = get_plural(name_lower)

    if architecture == "hexagonal":
        # 인바운드 포트 어댑터 생성
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/infrastructure/adapter/in/web"
        make_dirs(path)
        file_path = f"{path}/{name}WebAdapter.java"

        content = f"""package {base_package}.domain.{name}.infrastructure.adapter.in.web;

import {base_package}.domain.{name}.dto.*;
import {base_package}.domain.{name}.port.in.Use{name}Port;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/{path_name}")
public class {name}WebAdapter {{

    private final Use{name}Port port;

    @PostMapping
    public ResponseEntity<{name}Response> create{name}(@RequestBody {name}Request request) {{
        return ResponseEntity.ok(port.create{name}(request));
    }}

    @GetMapping
    public ResponseEntity<List<{name}Response>> get{plural}() {{
        return ResponseEntity.ok(port.get{plural}());
    }}

    @GetMapping("/{{id}}")
    public ResponseEntity<{name}Response> get{name}ById(@PathVariable Long id) {{
        return ResponseEntity.ok(port.get{name}ById(id));
    }}

    @PutMapping("/{{id}}")
    public ResponseEntity<{name}Response> update{name}(@PathVariable Long id, @RequestBody {name}Request request) {{
        return ResponseEntity.ok(port.update{name}(id, request));
    }}

    @DeleteMapping("/{{id}}")
    public ResponseEntity<Void> delete{name}(@PathVariable Long id) {{
        port.delete{name}(id);
        return ResponseEntity.noContent().build();
    }}
}}
"""
    else:
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/controller"
        make_dirs(path)
        file_path = f"{path}/{name}Controller.java"

        content = f"""package {base_package}.domain.{name}.controller;

import {base_package}.domain.{name}.dto.*;
import {base_package}.domain.{name}.service.{name}Service;
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
    public ResponseEntity<List<{name}Response>> get{plural}() {{
        return ResponseEntity.ok(service.get{plural}());
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
