-- create database grupo10;

-- drop database grupo10;

use grupo10;

create table empresa (
	id int primary key auto_increment,
    nomeFantasia varchar (45),
    telefone char (11),
    cnpj char (14),
    razaoSocial varchar (45),
    email varchar (45),
    codigoAtivacao char (5)
);

create table maquina (
	id int primary key auto_increment,
    nome varchar(45) not null,
    nucleosFisicos int,
    nucleosLogicos int,
    capacidadeTotal bigint,
    ramTotal bigint,
    dtCadastro datetime,
    fkEmpresa int,
    constraint fkMaquinaEmpresa foreign key (fkEmpresa) references empresa(id)
);

create table registro (
	idRegistro int auto_increment,
    fkMaquina int,
    cpuPorcentagemUso decimal (4,1),
    cpuFrequenciaAtual int,
    cpuUsoPorNucleo varchar(255), 
    cpuTemperatura Decimal (5,2),
    ramDisponivel int,
    ramUsada int,
    ramPercentualUso decimal(4,1),
    discoEspacoUsado int,
    discoEspacoLivre int,
    discoPercentualUso decimal(4,1),
    downloadRede bigint,
    uploadRede bigint,
    statusCpu varchar(10),
    statusRam varchar(10),
    statusDisco varchar(10),
    statusGeral varchar(10),
    dtRegistro datetime,
	constraint pkComposta primary key (idRegistro, fkMaquina),
    constraint fkMaquinaRegistro foreign key (fkMaquina) references maquina(id)
);

create table cargo (
	id int primary key auto_increment,
    titulo varchar (45)
);

create table funcionario (
	id int primary key auto_increment,
    nome varchar (45),
    email varchar (45),
    senha varchar (45),
    fkEmpresa int, 
    fkCargo int, 
    constraint fkEmpresaFuncionario foreign key (fkEmpresa) references empresa (id),
    constraint fkCargoFuncionario foreign key (fkCargo) references cargo (id)
);
