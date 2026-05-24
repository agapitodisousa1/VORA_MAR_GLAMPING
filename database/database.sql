CREATE DATABASE IF NOT EXISTS voramar;
USE voramar;
CREATE TABLE usuarios(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    pass VARCHAR(255),
    telefono VARCHAR(20),
    rol ENUM('cliente', 'admin') DEFAULT 'cliente',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
CREATE TABLE alojamientos(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  tipo VARCHAR(50),
  capacidad INT,
  precio_base DECIMAL(10,2),
  descripcion TEXT,
  imagen VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE reservas(
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT,
  alojamiento_id INT,
  fecha_inicio DATE,
  fecha_fin DATE,
  num_personas INT,
  precio_total DECIMAL(10,2),
  estado ENUM('pendiente', 'confirmada', 'cancelada'),
  fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (alojamiento_id) REFERENCES alojamientos(id)
);
