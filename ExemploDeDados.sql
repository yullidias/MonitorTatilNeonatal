insert into responsaveis(cpf,rg, nome_responsavel) values('136.254.456.58','MG123123', 'Maria');
insert into responsaveis(cpf,rg, nome_responsavel) values('111.000.123-98','MG534453', 'Joao');

insert into neonatos(id_neonato,nome_neonato,data_nascimento, cpf) values(1,'Valentina','2018-05-20', '111.000.123-98');
insert into neonatos(id_neonato,nome_neonato,data_nascimento, cpf) values(2,'Enzo','2018-05-22', '136.254.456.58');

insert into incubadoras values (1, 'incubadora1');
insert into incubadoras values (2, 'incubadora2');
insert into incubadoras values (3, 'incubadora3');

insert into neonatos_incubadoras(idNeonato,id_incubadora,data_entrada) values(1,1,'2018-05-21');
insert into neonatos_incubadoras(idNeonato,id_incubadora,data_entrada) values(2,2,'2018-05-23');

insert into dispositivos(mac,nome_dispositivo, ip_dispositivo) values ('74:d0:2b:81:fe:e6','PC Yulli', '10.0.122.26');
insert into dispositivos(mac,nome_dispositivo, ip_dispositivo) values ('b8:27:eb:5e:86:87','Interface', '10.0.127.118'); 
insert into dispositivos(mac,nome_dispositivo, ip_dispositivo) values ('b8:27:eb:93:7b:12','Sensor Temperatura', '10.0.121.12'); 
insert into dispositivos(mac,nome_dispositivo, ip_dispositivo) values ('b8:27:eb:c3:60:7e','Sensor ECG', '10.0.124.203');
insert into dispositivos(mac,nome_dispositivo, ip_dispositivo) values ('b8:27:eb:20:da:45','Sensor Spo2', '10.0.123.5');


insert into incubadoras_dispositivos(id_incubadora, mac, data_conexao) values(1,'74:d0:2b:81:fe:e6', '2018-06-15');
insert into incubadoras_dispositivos(id_incubadora, mac, data_conexao) values(1,'b8:27:eb:5e:86:87', '2018-06-15');
insert into incubadoras_dispositivos(id_incubadora, mac, data_conexao) values(1,'b8:27:eb:93:7b:12', '2018-06-15');
insert into incubadoras_dispositivos(id_incubadora, mac, data_conexao) values(1,'b8:27:eb:c3:60:7e', '2018-06-15');	
insert into incubadoras_dispositivos(id_incubadora, mac, data_conexao) values(1,'b8:27:eb:20:da:45', '2018-06-15'); 

insert into portas(num_porta, desc_sinal) values (8081, 'Temperatura');
insert into portas(num_porta, desc_sinal) values (8082, 'Umidade');
insert into portas(num_porta, desc_sinal) values (8083, 'Frequencia');
insert into portas(num_porta, desc_sinal) values (8084, 'SpO2');
insert into portas(num_porta, desc_sinal) values (8085, 'display umidade');

insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:5e:86:87',8081,FALSE, TRUE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:5e:86:87',8082,FALSE, TRUE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:5e:86:87',8083,FALSE, TRUE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:5e:86:87',8084,FALSE, TRUE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:5e:86:87',8085,FALSE, TRUE);

insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:93:7b:12',8081,TRUE, FALSE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:c3:60:7e',8083,TRUE, FALSE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('b8:27:eb:20:da:45',8084,TRUE, FALSE);

insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('74:d0:2b:81:fe:e6',8082,TRUE, FALSE);
insert into dispositivos_portas(mac, num_porta, envia, recebe) values ('74:d0:2b:81:fe:e6',8085,TRUE, FALSE);


