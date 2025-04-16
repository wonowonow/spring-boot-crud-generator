from springcrud.utils.file import make_dirs, to_path, write_file
from springcrud.utils.input import get_plural

def generate_service_interface(base_package, name, java_version, architecture):
    name_plural = get_plural(name)
    
    if architecture == "hexagonal":
        # Port 인터페이스 추가
        in_port_path = f"src/main/java/{to_path(base_package)}/domain/{name}/port/in"
        make_dirs(in_port_path)
        in_port_file_path = f"{in_port_path}/Use{name}Port.java"
        in_port_content = f"""package {base_package}.domain.{name}.port.in;

import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;

import java.util.List;

public interface Use{name}Port {{
    {name}Response create{name}({name}Request request);
    List<{name}Response> get{name_plural}();
    {name}Response get{name}ById(Long id);
    {name}Response update{name}(Long id, {name}Request request);
    void delete{name}(Long id);
}}
"""
        write_file(in_port_file_path, in_port_content)

        # 서비스 인터페이스 생성
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}Service.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.port.in.Use{name}Port;

public interface {name}Service extends Use{name}Port {{
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

def generate_service_impl(base_package, name, java_version, architecture):
    name_plural = get_plural(name)
    
    if architecture == "hexagonal":
        path = f"src/main/java/{to_path(base_package)}/domain/{name}/service"
        make_dirs(path)
        file_path = f"{path}/{name}ServiceImpl.java"
        content = f"""package {base_package}.domain.{name}.service;

import {base_package}.domain.{name}.domain.{name};
import {base_package}.domain.{name}.dto.{name}Request;
import {base_package}.domain.{name}.dto.{name}Response;
import {base_package}.domain.{name}.port.out.{name}Port;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class {name}ServiceImpl implements {name}Service {{

    private final {name}Port port;

    @Override
    public {name}Response create{name}({name}Request request) {{
        {name} entity = {name}.builder()
                .name(request.name())
                .build();
        {name} saved = port.save(entity);
        return new {name}Response(saved.getId(), saved.getName());
    }}

    @Override
    public List<{name}Response> get{name_plural}() {{
        return port.findAll().stream()
                .map(entity -> new {name}Response(entity.getId(), entity.getName()))
                .collect(Collectors.toList());
    }}

    @Override
    public {name}Response get{name}ById(Long id) {{
        {name} entity = port.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        return new {name}Response(entity.getId(), entity.getName());
    }}

    @Override
    public {name}Response update{name}(Long id, {name}Request request) {{
        {name} entity = port.findById(id)
                .orElseThrow(() -> new RuntimeException("{name} not found"));
        entity.setName(request.name());
        {name} updated = port.save(entity);
        return new {name}Response(updated.getId(), updated.getName());
    }}

    @Override
    public void delete{name}(Long id) {{
        port.deleteById(id);
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