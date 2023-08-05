DROP DATABASE IF EXISTS author;
CREATE DATABASE author;
USE author;

DROP TABLE IF EXISTS autor;
CREATE TABLE IF NOT EXISTS autor(
    autor_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    genero ENUM('M', 'F'),
    fecha_nacimiento DATE NOT NULL,
    pais_origen VARCHAR(40) NOT NULL,
    CONSTRAINT unique_combinacion UNIQUE (nombre, apellido, fecha_nacimiento),
    fecha_registro DATETIME DEFAULT current_timestamp
);

DROP TABLE IF EXISTS libros;
CREATE TABLE libros(
    libro_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    autor_id INT UNSIGNED NOT NULL,
    titulo VARCHAR(50),
    descripcion VARCHAR(250),
    paginas INTEGER UNSIGNED,
    fecha_publicacion DATE NOT NULL,
    fecha_creacion DATETIME DEFAULT current_timestamp,
    FOREIGN KEY (autor_id) REFERENCES autor(autor_id)
);


INSERT INTO autor (nombre, apellido, genero, fecha_nacimiento, pais_origen)
VALUES ('Pepe', 'El Toro', 'M', '2001-03-05', 'México'), ('Alan', 'El Perro', 'M', '2001-03-05', 'México');

SELECT * FROM autor;
DESC libros;


DELIMITER #

CREATE FUNCTION agregar_dias(fecha DATE, dias INT)
RETURNS DATE 
BEGIN
    return FECHA + interval DIAS day;
END#
