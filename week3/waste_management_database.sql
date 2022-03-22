create table customer (
	customer_id serial unique not null,	
	house_number varchar(100) not null,
	customer_name varchar(100) not null,
	street_name varchar(100) not null,
	street_number varchar(100) not null,
	city varchar(100) not null,
	state varchar(100) not null,
	phone_number varchar(100) not null 
);


create table collection_agency(
	agency_id serial unique not null,
	agency_name varchar(100) not null,
	street_name varchar(100) not null,
	street_number varchar(100) not null,
	city varchar(100) not null,
	state varchar(100) not null,
	phone_number varchar(100) not null
);

ceate table login(
	customer_id serial FOREIGN KEY REFERENCES customer(customer_id),
	user_name varchar(100) not null,
	pass_word varchar(100) not null
);

create table booking (
	booking_id serial unique not null,
	booking_date date,
	booking_time time
);

craete table admin (
	admin_id serial not null,
	admin_name varcar(100) not null
);