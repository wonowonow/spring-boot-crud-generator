package com.example.domain.Product.service;

import com.example.domain.Product.domain.Product;
import com.example.domain.Product.dto.ProductRequest;
import com.example.domain.Product.dto.ProductResponse;
import com.example.domain.Product.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService {

    private final ProductRepository repository;

    @Override
    public ProductResponse createProduct(ProductRequest request) {
        Product entity = Product.builder()
                .name(request.name())
                .build();
        Product saved = repository.save(entity);
        return new ProductResponse(saved.getId(), saved.getName());
    }

    @Override
    public List<ProductResponse> getProducts() {
        return repository.findAll().stream()
                .map(entity -> new ProductResponse(entity.getId(), entity.getName()))
                .collect(Collectors.toList());
    }

    @Override
    public ProductResponse getProductById(Long id) {
        Product entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Product not found"));
        return new ProductResponse(entity.getId(), entity.getName());
    }

    @Override
    public ProductResponse updateProduct(Long id, ProductRequest request) {
        Product entity = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Product not found"));
        entity.setName(request.name());
        Product updated = repository.save(entity);
        return new ProductResponse(updated.getId(), updated.getName());
    }

    @Override
    public void deleteProduct(Long id) {
        repository.deleteById(id);
    }
}
