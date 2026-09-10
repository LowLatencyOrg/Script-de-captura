create database grupo10;

-- drop database grupo10;

use grupo10;

create table empresa (
	id int primary key auto_increment,
    nomeFantasia varchar (45) not null,
    telefone char (11) not null,
    cnpj char (14) not null,
    razaoSocial varchar (45) not null,
    email varchar (45) not null,
    codigoAtivacao char (5) not null
);

create table maquina (
	id int primary key auto_increment,
    nome varchar(45) not null,
    nucleosFisicos int not null,
    nucleosLogicos int not null,
    capacidadeTotal bigint not null,
    ramTotal bigint not null,
    dtCadastro datetime not null,
    fkEmpresa int,
    constraint fkMaquinaEmpresa foreign key (fkEmpresa) references empresa(id)
);

create table registro (
	idRegistro int auto_increment,
    fkMaquina int not null,
    cpuPorcentagemUso decimal (4,1) not null,
    cpuFrequenciaAtual int not null,
    cpuUsoPorNucleo varchar(255) not null, 
    cpuTemperatura Decimal (5,2),
    ramDisponivel int not null,
    ramUsada int not null,
    ramPercentualUso decimal(4,1) not null,
    discoEspacoUsado int not null,
    discoEspacoLivre int not null,
    discoPercentualUso decimal(4,1) not null,
    downloadRede bigint not null,
    uploadRede bigint not null,
    statusCpu varchar(10) not null,
    statusRam varchar(10) not null,
    statusDisco varchar(10) not null,
    statusGeral varchar(10) not null,
    dtRegistro datetime not null,
	constraint pkComposta primary key (idRegistro, fkMaquina),
    constraint fkMaquinaRegistro foreign key (fkMaquina) references maquina(id)
);

create table cargo (
	id int primary key auto_increment,
    titulo varchar (45) not null
);

create table funcionario (
	id int primary key auto_increment,
    nome varchar (45) not null,
    email varchar (45) not null,
    senha varchar (45) not null,
    fkEmpresa int, 
    fkCargo int, 
    constraint fkEmpresaFuncionario foreign key (fkEmpresa) references empresa (id),
    constraint fkCargoFuncionario foreign key (fkCargo) references cargo (id)
);
