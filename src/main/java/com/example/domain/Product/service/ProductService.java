package com.example.domain.Product.service;

import com.example.domain.Product.domain.Product;
import com.example.domain.Product.dto.ProductRequest;
import com.example.domain.Product.dto.ProductResponse;

import java.util.List;

public interface ProductService {
    ProductResponse createProduct(ProductRequest request);
    List<ProductResponse> getProducts();
    ProductResponse getProductById(Long id);
    ProductResponse updateProduct(Long id, ProductRequest request);
    void deleteProduct(Long id);
}
