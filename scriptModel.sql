CREATE TABLE IF NOT EXISTS empresa (
id INT PRIMARY KEY AUTO_INCREMENT,
nomeFantasia VARCHAR(45),
telefone CHAR(11),
cnpj CHAR(14),
razaoSocial VARCHAR(45),
email VARCHAR(45),
codigoAtivacao CHAR(5)
);

CREATE TABLE IF NOT EXISTS cargo (
id INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS funcionario (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
email VARCHAR(45),
senha VARCHAR(45),
fkEmpresa INT,
fkCargo INT,
CONSTRAINT fkEmpresaFuncionario
FOREIGN KEY (fkEmpresa) REFERENCES empresa(id),
CONSTRAINT fkCargoFuncionario
FOREIGN KEY (fkCargo) REFERENCES cargo(id)
);

CREATE TABLE IF NOT EXISTS maquina (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45) NOT NULL,
nucleosFisicos INT,
nucleosLogicos INT,
capacidadeTotal BIGINT,
ramTotal BIGINT,
dtCadastro DATETIME,
fkEmpresa INT,
CONSTRAINT fkMaquinaEmpresa
FOREIGN KEY (fkEmpresa) REFERENCES empresa(id)
);

CREATE TABLE IF NOT EXISTS registro (
idRegistro INT AUTO_INCREMENT,
fkMaquina INT,
cpuPorcentagemUso DECIMAL(4,1),
cpuFrequenciaAtual INT,
cpuUsoPorNucleo VARCHAR(255),
cpuTemperatura DECIMAL(5,2),
ramDisponivel INT,
ramUsada INT,
ramPercentualUso DECIMAL(4,1),
discoEspacoUsado INT,
discoEspacoLivre INT,
downloadRede BIGINT,
uploadRede BIGINT,
statusCpu VARCHAR (10),
statusRam VARCHAR(10),
statusDisco VARCHAR (10),
statusGeral(10),
dtRegistro DATETIME,
CONSTRAINT pkComposta PRIMARY KEY (idRegistro, fkMaquina),
CONSTRAINT fkMaquinaRegistro
FOREIGN KEY (fkMaquina) REFERENCES maquina(id)
);
