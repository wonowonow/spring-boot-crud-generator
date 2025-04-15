package com.example.domain.User.service;

import com.example.domain.User.service.UserService;
import com.example.domain.User.domain.User;
import com.example.domain.User.dto.UserRequest;
import com.example.domain.User.dto.UserResponse;
import com.example.domain.User.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository repository;

    @Override
    public UserResponse createUser(UserRequest request) {
        User entity = User.builder()
                .name(request.name())
                .build();
        User saved = repository.save(entity);
        return new UserResponse(saved.getId(), saved.getName());
    }

    @Override
    public List<UserResponse> getUsers() {
        return repository.findAll().stream()
                .map(entity -> new UserResponse(entity.getId(), entity.getName()))
                .collect(Collectors.toList());
    }

    @Override
    public UserResponse getUserById(Long id) {
        User entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found"));
        return new UserResponse(entity.getId(), entity.getName());
    }

    @Override
    public UserResponse updateUser(Long id, UserRequest request) {
        User entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found"));
        entity.setName(request.name());
        User updated = repository.save(entity);
        return new UserResponse(updated.getId(), updated.getName());
    }

    @Override
    public void deleteUser(Long id) {
        repository.deleteById(id);
    }
}
