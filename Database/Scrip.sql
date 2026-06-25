---TABLA MASCOTAS---
CREATE TABLE mascotas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    especie VARCHAR(100)
);

--INSERTAR DATOS----
INSERT INTO mascotas (nombre, especie) VALUES ('Lucas', 'Perro');
INSERT INTO mascotas (nombre, especie) VALUES ('Felix', 'Gato');

---SELECT DE LA TABLA---
SELECT * FROM MASCOTAS

--TABLA LIBROS--

CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100)
);
---INSERTAR DATOS---
INSERT INTO libros (titulo, autor) VALUES
('Don Quijote', 'Miguel de Cervantes'), 
('Cien años de soledad', 'Gabriel García Márquez');

--SELECT TABLA--
SELECT * FROM LIBROS

--TABLA PELICULAS--
CREATE TABLE peliculas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    genero VARCHAR(50)
);

-- INSERTAR DATOS--
INSERT INTO peliculas (titulo, genero) VALUES 
('Inception', 'Ciencia Ficción'), 
('Avatar', 'Acción');

--	SELECT TABLA--
SELECT * FROM PELICULAS


