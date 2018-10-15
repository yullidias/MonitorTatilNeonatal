/*
Created: 15/05/2018
Modified: 30/05/2018
Model: MySQL 5.7
Database: MySQL 5.7
*/


-- Create tables section -------------------------------------------------

-- Table responsaveis

CREATE TABLE `responsaveis`
(
  `cpf` Varchar(15) NOT NULL,
  `rg` Varchar(15),
  `nome_responsavel` Varchar(50) NOT NULL
)
;

ALTER TABLE `responsaveis` ADD PRIMARY KEY (`cpf`)
;

-- Table neonatos

CREATE TABLE `neonatos`
(
  `id_neonato` Int NOT NULL,
  `nome_neonato` Varchar(50) NOT NULL,
  `data_nascimento` Date NOT NULL,
  `cpf` Varchar(15) NOT NULL
)
;

CREATE INDEX `IX_Relationship11` ON `neonatos` (`cpf`)
;

ALTER TABLE `neonatos` ADD PRIMARY KEY (`id_neonato`)
;

-- Table incubadoras

CREATE TABLE `incubadoras`
(
  `id_incubadora` Int NOT NULL,
  `nome_incubadora` Varchar(20) NOT NULL
)
;

ALTER TABLE `incubadoras` ADD PRIMARY KEY (`id_incubadora`)
;

-- Table sensores

CREATE TABLE `sensores`
(
  `id_i2c_sensor` Varchar(8) NOT NULL,
  `nome_sensor` Varchar(25)
)
;

ALTER TABLE `sensores` ADD PRIMARY KEY (`id_i2c_sensor`)
;

-- Table informacoes

CREATE TABLE `informacoes`
(
  `id_informacao` Serial NOT NULL,
  `dado` Double NOT NULL,
  `data_aquisicao` Datetime NOT NULL,
  `id_i2c_sensor` Varchar(8) NOT NULL,
  `id_tipo` Int NOT NULL
)
;

CREATE INDEX `IX_Relationship14` ON `informacoes` (`id_i2c_sensor`)
;

CREATE INDEX `IX_Relationship15` ON `informacoes` (`id_tipo`)
;

ALTER TABLE `informacoes` ADD PRIMARY KEY (`id_informacao`)
;

-- Table tipos

CREATE TABLE `tipos`
(
  `id_tipo` Int NOT NULL,
  `nome_tipo` Varchar(20) NOT NULL
)
;

ALTER TABLE `tipos` ADD PRIMARY KEY (`id_tipo`)
;

-- Table dispositivos

CREATE TABLE `dispositivos`
(
  `mac` Varchar(20) NOT NULL,
  `nome_dispositivo` Varchar(20) NOT NULL,
  `ip_dispositivo` Varchar(15) NOT NULL
)
;

ALTER TABLE `dispositivos` ADD PRIMARY KEY (`mac`)
;

-- Table portas

CREATE TABLE `portas`
(
  `num_porta` Int(4) NOT NULL,
  `desc_sinal` Varchar(15) NOT NULL
)
;

ALTER TABLE `portas` ADD PRIMARY KEY (`num_porta`)
;

-- Table neonatos_incubadoras

CREATE TABLE `neonatos_incubadoras`
(
  `idNeonato` Int NOT NULL,
  `id_incubadora` Int NOT NULL,
  `data_entrada` Datetime NOT NULL,
  `data_saida` Datetime
)
;

ALTER TABLE `neonatos_incubadoras` ADD PRIMARY KEY (`idNeonato`,`id_incubadora`,`data_entrada`)
;

-- Table incubadoras_sensores

CREATE TABLE `incubadoras_sensores`
(
  `id_incubadora` Int NOT NULL,
  `id_i2c_sensor` Varchar(8) NOT NULL
)
;

ALTER TABLE `incubadoras_sensores` ADD PRIMARY KEY (`id_incubadora`,`id_i2c_sensor`)
;

-- Table incubadoras_dispositivos

CREATE TABLE `incubadoras_dispositivos`
(
  `id_incubadora` Int NOT NULL,
  `mac` Varchar(20) NOT NULL,
  `data_conexao` Datetime NOT NULL,
  `data_remocao` Datetime
)
;

ALTER TABLE `incubadoras_dispositivos` ADD PRIMARY KEY (`id_incubadora`,`mac`,`data_conexao`)
;

-- Table dispositivos_portas

CREATE TABLE `dispositivos_portas`
(
  `mac` Varchar(20) NOT NULL,
  `envia` Bool NOT NULL,
  `recebe` Bool NOT NULL,
  `num_porta` Int(4) NOT NULL
)
;

ALTER TABLE `dispositivos_portas` ADD PRIMARY KEY (`mac`,`num_porta`)
;

-- Create foreign keys (relationships) section ------------------------------------------------- 


ALTER TABLE `neonatos` ADD CONSTRAINT `Relationship1` FOREIGN KEY (`cpf`) REFERENCES `responsaveis` (`cpf`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `neonatos_incubadoras` ADD CONSTRAINT `Relationship2` FOREIGN KEY (`idNeonato`) REFERENCES `neonatos` (`id_neonato`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `neonatos_incubadoras` ADD CONSTRAINT `Relationship3` FOREIGN KEY (`id_incubadora`) REFERENCES `incubadoras` (`id_incubadora`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `incubadoras_sensores` ADD CONSTRAINT `Relationship4` FOREIGN KEY (`id_incubadora`) REFERENCES `incubadoras` (`id_incubadora`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `incubadoras_sensores` ADD CONSTRAINT `Relationship5` FOREIGN KEY (`id_i2c_sensor`) REFERENCES `sensores` (`id_i2c_sensor`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `incubadoras_dispositivos` ADD CONSTRAINT `Relationship6` FOREIGN KEY (`id_incubadora`) REFERENCES `incubadoras` (`id_incubadora`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `incubadoras_dispositivos` ADD CONSTRAINT `Relationship7` FOREIGN KEY (`mac`) REFERENCES `dispositivos` (`mac`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `informacoes` ADD CONSTRAINT `Relationship14` FOREIGN KEY (`id_i2c_sensor`) REFERENCES `sensores` (`id_i2c_sensor`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `informacoes` ADD CONSTRAINT `Relationship15` FOREIGN KEY (`id_tipo`) REFERENCES `tipos` (`id_tipo`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `dispositivos_portas` ADD CONSTRAINT `Relationship16` FOREIGN KEY (`mac`) REFERENCES `dispositivos` (`mac`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


ALTER TABLE `dispositivos_portas` ADD CONSTRAINT `Relationship17` FOREIGN KEY (`num_porta`) REFERENCES `portas` (`num_porta`) ON DELETE RESTRICT ON UPDATE RESTRICT
;


