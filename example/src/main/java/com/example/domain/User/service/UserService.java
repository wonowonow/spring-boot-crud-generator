package com.example.domain.User.service;

import com.example.domain.User.domain.User;
import com.example.domain.User.dto.UserRequest;
import com.example.domain.User.dto.UserResponse;

import java.util.List;

public interface UserService {
    UserResponse createUser(UserRequest request);
    List<UserResponse> getUsers();
    UserResponse getUserById(Long id);
    UserResponse updateUser(Long id, UserRequest request);
    void deleteUser(Long id);
}
