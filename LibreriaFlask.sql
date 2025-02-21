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
    Id_usuarios INT AUTO_INCREMENT PRIMARY KEY,
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
    Id_usuarios INT
);

INSERT INTO Direccion (Calle, Pais, Ciudad, Estado, CP) 
VALUES ('Av. Siempre Viva 742', 'México', 'CDMX', 'CDMX', '01234');

/*INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia)
VALUES ('Administrador', 'Juan Pérez', 'juan.perez@example.com', '1234567890', 'admin123');

INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia)
VALUES ('Cliente', 'María Gómez', 'maria.gomez@example.com', '0987654321', 'cliente123');

SELECT * FROM Usuarios;*/

INSERT INTO Inicio_de_Sesion (Email, Contra, Id_libros, Id_ventas) 
VALUES ('juan@example.com', 'contraseña_segura', NULL, NULL);

INSERT INTO Libros (Nombre, Estado, Existencia, Costo, Editorial, Autor, Id_almacen) 
VALUES ('Cien años de soledad', 'Disponible', 50, 299.99, 'Sudamericana', 'Gabriel García Márquez', NULL);

INSERT INTO Almacen (Email, Existencias, Id_sesion, Id_libros) 
VALUES ('juan@example.com', 50, 1, 1);

INSERT INTO Ventas (LibrosComprados, Existencia, Costo, VentasTotalesPesos, Id_libros, Id_usuarios) 
VALUES (5, 45, 299.99, 1499.95, 1, 1);


/*********drop database libreria;*********/

/*ALTER TABLE Usuarios
ADD CONSTRAINT fk_direccion_usuarios FOREIGN KEY (Id_direccion) REFERENCES Direccion(Id_direccion),
ADD CONSTRAINT fk_sesion_usuarios FOREIGN KEY (Id_sesion) REFERENCES inicio_de_sesion(Id_sesion),
ADD CONSTRAINT fk_ventas_usuarios FOREIGN KEY (Id_ventas) REFERENCES Ventas(Id_ventas);

ALTER TABLE Inicio_de_Sesion
ADD CONSTRAINT fk_libros_sesion FOREIGN KEY (Id_libros) REFERENCES Libros(Id_libros),
ADD CONSTRAINT fk_ventas_sesion FOREIGN KEY (Id_ventas) REFERENCES Ventas(Id_ventas);

ALTER TABLE Almacen
ADD CONSTRAINT fk_sesion_almacen FOREIGN KEY (Id_sesion) REFERENCES inicio_de_sesion(Id_sesion),
ADD CONSTRAINT fk_libros_almacen FOREIGN KEY (Id_libros) REFERENCES Libros(Id_libros);

ALTER TABLE Libros
ADD CONSTRAINT fk_almacen_libros FOREIGN KEY (Id_almacen) REFERENCES Almacen(Id_almacen);

ALTER TABLE Ventas
ADD CONSTRAINT fk_libros_ventas FOREIGN KEY (Id_libros) REFERENCES Libros(Id_libros),
ADD CONSTRAINT fk_usuarios_ventas FOREIGN KEY (Id_usuarios) REFERENCES Usuarios(Id_usuarios);*/




