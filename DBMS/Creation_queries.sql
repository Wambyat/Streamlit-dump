create table creator(cid int primary key,cname varchar(50), gname(50), budget int, gid int);

create table games(id int primary key, name varchar(50), rating smallint, Creator varchar(50), length smallint, image blob);

create table extra_det(age_range smallint,size smallint, space smallint, specs varchar(50), engine varchar(50), gid int, primary key(gid), foreign key (gid) refrences games(id));

create table genre(gid int,genres primary key(gid), foreign key (gid) refrences games(id));

create table user_a(UID int, uname varchar(50), password varchar(50), role varchar(50), uemail varchar(50), primary key(UID));

create table roles_a(role varchar(20) primary key, tableacc varchar(20));

create table perms(UID int, role varchar(20),primary key(UID), foreign key (UID) references user_a(UID),foreign key (role) references roles_a(role));