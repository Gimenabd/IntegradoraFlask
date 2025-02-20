CREATE DATABASE Libreria;
USE Libreria;

CREATE TABLE Direccion (
    Id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    Calle VARCHAR(100) NOT NULL,
    Pais VARCHAR(50) NOT NULL,
    Ciudad VARCHAR(50) NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    CP VARCHAR(10) NOT NULL
);

CREATE TABLE Usuarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Tipo_de_Usuario ENUM('Cliente', 'Administrador') NOT NULL,
    Nombre_completo VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    Contrasenia VARCHAR(255) NOT NULL,
    Id_direccion INT,
    Id_sesion INT,
    Id_ventas INT
);

CREATE TABLE Inicio_de_Sesion (
    Id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Contra VARCHAR(255) NOT NULL,
    Id_libros INT,
    Id_ventas INT
);

CREATE TABLE Almacen (
    Id_almacen INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Existencias INT NOT NULL,
    Id_sesion INT,
    Id_libros INT
);

CREATE TABLE Libros (
    Id_libros INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    Estado ENUM('Disponible', 'Vendido') NOT NULL,
    Existencia INT NOT NULL,
    Costo DECIMAL(10, 2) NOT NULL,
    Editorial VARCHAR(100),
    Autor VARCHAR(100),
    Id_almacen INT
);

CREATE TABLE Ventas (
    Id_ventas INT AUTO_INCREMENT PRIMARY KEY,
    LibrosComprados INT NOT NULL,
    Existencia INT NOT NULL,
    Costo DECIMAL(10, 2) NOT NULL,
    VentasTotalesPesos DECIMAL(12, 2) NOT NULL,
    Id_libros INT,
    Id_usuario INT
);
INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia)
VALUES ('Administrador', 'Juan Pérez', 'juan.perez@example.com', '1234567890', 'admin123');

INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia)
VALUES ('Cliente', 'María Gómez', 'maria.gomez@example.com', '0987654321', 'cliente123');


SELECT * FROM Usuarios;
/*drop database libreria;*/
