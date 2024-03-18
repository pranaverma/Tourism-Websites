-- Database Creation:
CREATE DATABASE protravelo;
use protravelo;

-- Tables:
create table Register(
ID int auto_increment,
Name varchar(255) ,
Username varchar(255) ,
Password varchar(255),
Mobile_number varchar(255),
primary key(ID)
);

create table Customer(
ID int ,
Name varchar(255) ,
DOB varchar(255),
Gender varchar(255) ,
Country varchar(255) ,
Address varchar(255) ,
Email varchar(255) ,
Mobile_number bigint,
Alternate_mobile_number bigint,
Language varchar(255) ,
Currency varchar(255) ,
Passport_number varchar(255),
Primary key(ID),
foreign key(ID) references Register(ID)
);

create table Travel_agent(
ID int ,
Name varchar(255) ,
Rating int,
Price int,
primary key(ID)
);

insert into Travel_agent
values (0,"None",0,0),
 (1,"David",9,19000),
 (2, "Steve", 8, 19000),
 (3, "Ashley", 9, 21000),
 (4, "Ellyse", 9, 20000),
 (9, "Paul", 8, 19000),
 (10, "Xavi", 8, 19000),
 (11, "Sofia", 9, 21000),
 (12, "Scarlet", 9, 20000),
 (13, "Henry", 9, 20000),
 (14, "Jack", 9, 21000),
 (15, "Michail", 8, 20000),
 (16, "Jerome", 8, 19000),
 (17, "Varane", 8, 19000),
 (18, "Louis", 9, 21000),
 (19, "Laura", 9, 21000),
 (20, "Sarah", 9, 20000),
 (21, "Alexander", 9, 18000),
 (22, "dimitri", 8, 17000),
 (23, "christos", 8, 17000),
 (24, "petros", 9, 17000),
 (5, "Federico", 8, 18000),
 (6, "Lorenzo", 7, 17000),
 (7, "Isabella", 8, 18000),
 (8, "Gabriella", 9, 19000),
 (25, "Xiong", 7, 15000),
 (26, "Leia", 8, 16000),
 (27, "William", 9, 17000),
 (28, "Weaton", 9, 16000),
 (29, "Mansour", 7, 17000),
 (30, "Norryis", 8, 18000),
 (31, "Betsy", 8, 18000),
 (32, "Anna", 9, 19000);

create table countries(
	ID int auto_increment primary key,
    Name varchar(255)
);

insert into countries 
values (1,"Australia"),
		(2,"Italy"),
        (3,"Switzerland"),
        (4,"Mauritius"),
        (5,"France"),
        (6,"Greece"),
        (7,"Hong Kong"),
        (8,"UAE");
       

create table cities(
	ID int auto_increment primary key,
    Name varchar(255),
    Country_ID int,
    foreign key(Country_ID) references countries(ID)
);
insert into cities
values(1,"Sydney",1),
	(2,"Melbourne",1),
        (3,"Brisbane",1),
        (4,"Canberra",1),
        (5,"Rome",2),
        (6,"Venice",2),
        (7,"Milan",2),
        (8,"Florence",2),
        (9,"Basel",3),
        (10,"Geneva",3),
        (11,"Lucrene",3),
        (12,"Zurich",3),
        (13,"Curepipe",4),
        (14,"Flic-En-Flac",4),
        (15,"Grand Baie",4),
        (16,"Port Louis",4),
		(17,"Paris",5),
		(18,"Cannes",5),
        (19,"Bordeaux",5),
        (20,"Corsica",5),
        (21,"Athens",6),
        (22,"Thessaloniki",6),
        (23,"Chania",6),
        (24,"Rhodes Town",6),
        (25,"Lantau Island",7),
        (26,"Tsim Sha Tsui",7),
        (27,"Kowloon",7),
        (28,"Repulse Bay",7),
        (29,"Abu Dhabi",8),
        (30,"Dubai",8),
        (31,"Fujairah",8),
        (32,"Sharjah",8)
        ;

create table Hotels(
ID int,
Name varchar(255) ,
Price int,
City_ID int,
primary key (ID),
foreign key(City_ID) references cities(ID)
);
Insert into Hotels
values  (1,"QT Sydney", 16118,1),
		(2,"Fraser Suites Sydney",8841,1),
        (3,"Park Hyatt Melbourne",6564,2),
        (4,"The Langham Melbourne",20235,2),
        (5,"Crystalbrook Vincent",23923,3),
        (6,"Hyatt Regency Brisbane",31456,3),
        (7,"Midnight Hotel",6345,4),
        (8,"Hotel Realm",18459,4),
        (9,"Hotel Artemide",19657,5),
        (10,"Albergo del Senato",32741,5),
        (11,"Hotel Ai Reali",4576,6),
        (12,"Rosa Salva Hotel",23677,6),
        (13,"Lancaster Hotel",9569,7),
        (14,"43 Station Hotel",13853,7),
        (15,"Hotel Franchi",7987,8),
        (16,"Diplomat Hotel",12978,8),
        (17,"Hyperion Hotel Basel",10534,9 ),
		(18, "ibis budget Basel City",5888,9 ),
        (19,"Nash Suites Airport Hotel",8751,10),
        (20,"Warwick Geneva",11813,10),
        (21,"ibis budget Hotel Luzern",6461,11),
        (22,"AMERON Luzern Hotel Flora",12550,11),
        (23,"Crowne Plaza Zurich",9201,12),
        (24,"Central Plaza",17584,12),
        (25,"Hennessy Park Hotel",12117,13),
        (26,"Le Suffren Hotel & Marina",13871,13),
        (27,"Seastar Hotel",12563,14),
        (28,"Sofitel L'Imperial Resort and Spa",29227,14),
        (29,"Hôtel 20 Degrés Sud",39969,15),
        (30,"Mauricia Beachcomber Resort & Spa",20823,15),
        (31,"Cocotiers Hotel",5967,16),
        (32,"Labourdonnais Waterfront Hotel",16975,16),
        (33,"Hotel Malte- Astotel",19790,17),
		(34,"Hotel 34B- Astotel",11616,17),
        (35,"Hotel de Provence",7765,18),
        (36,"Hotel Martinez",5851,18),
        (37,"Hotel Cardinal Bordeaux",18964,19),
        (38,"Hotel Gambetta",11774,19),
        (39,"Hotel Tettola",6711,20),
        (40,"Hotel Bartaccia",5937,20),
        (41,"Sofitet Athens Hotel",14212,21),
        (42,"Plaka Hotel",8464,21),
        (43,"Hyatt Regency Thessaloniki",16606,22),
        (44,"Electra Hotel",6217,22),
        (45,"Hyperion City Hotel",6767,23),
        (46,"Enetiko Rooms",4753,23),
        (47,"Elites Hotel",10876,24),
        (48,"Esperia City Hotel",6539,24),
        (49,"Disney Explorers Lodge", 17178,25),
		(50,"Hong Kong Disneyland Hotel",16354,25),
        (51,"Sheraton Hong Kong Hotel & Towers",7278,26),
        (52,"InterContinental Grand Stanford",7789,26),
        (53,"The Mira Hong Kong",7071,27),
        (54,"Regal Kowloon Hotel",5521,27),
        (55,"Ocean Park Marriott Hotel",9483,28),
        (56, "The Fleming Hong Kong",8897,28),
        (57,"Traders Hotel, Abu Dhabi",8887,29),
        (58,"Southern Sun Abu Dhabi",6615,29),
        (59,"Atana Hotel",7318,30),
        (60,"Citymax Hotel Bur Dubai",3789,30),
        (61,"The White villa",99969,31),
        (62,"Ibis Fujairah",6421,31),
        (63,"Golden Sands Hotel",3847,32),
        (64, "Citymax Sharjah",2992,32);




create table Booking(
Booking_ID int auto_increment primary key,
ID int ,
Travel_agent_ID int,
HotelID int,
Number_of_people int,
Start_date varchar(255),
Number_of_days int,
Country_ID int ,
City1_ID int,
City2_ID int,
City3_ID int,
City4_ID int,
Hotel1_ID int,
Hotel2_ID int,
Hotel3_ID int,
Hotel4_ID int,
Final_price int,
Progress varchar(255),
foreign key (Travel_agent_ID) references Travel_agent(ID),
foreign key (ID) references Register(ID),
foreign key (City1_ID) references cities(ID),
foreign key (City2_ID) references cities(ID),
foreign key (City3_ID) references cities(ID),
foreign key (City4_ID) references cities(ID),
foreign key (Hotel1_ID) references Hotels(ID),
foreign key (Hotel2_ID) references Hotels(ID),
foreign key (Hotel3_ID) references Hotels(ID),
foreign key (Hotel4_ID) references Hotels(ID),
foreign key (Country_ID) references countries(ID) 
);




create table Packages(
Package_ID int auto_increment,
Package_name varchar(255),
Individual_price int,
primary key(Package_ID));

insert into Packages
values (1,"Australia Package",129799),
		(2,"Italy Package",89699),
        (3,"Switzerland Package",96799),
        (4,"Mauritius Package",77399),
        (5,"France Package",85599),
        (6,"Greece Package",72199),
        (7,"Hong-Kong Package",66699),
        (8,"U.A.E Package",55999),
        (9,"Italy and Switzerland Package",169899),
        (10,"Greece and Italy Package",135699),
        (11,"Classical Europe Package",179799),
        (12,"Fantastic Four Package",199999);

Create table Travel_agent_register ( 
Name varchar(255), 
DOB varchar(255), 
Gender varchar(255), 
Email varchar(255), 
Address varchar(255), 
Mobile_number varchar(255), 
Country varchar(255), 
Passport_number varchar(255), 
Languages_known varchar(255), 
primary key(Passport_number) );

create table Book_package(
Booking_ID int auto_increment,
ID int,
packageID int,
name varchar(255),
package_name varchar(255),
number_of_people int,
departing_date varchar(255),
Progress varchar(255),
Final_price bigint,
number_of_days int,
primary key (Booking_ID),
foreign key(ID) references Register(ID),
foreign key(packageID) references Packages(Package_ID)
);


create table Feedback(
ID int auto_increment,
BookingID_customized int,
BookingID_package int,
Travel_agent_feedback int ,
Hotel_feedback int ,
Journey_feedback int ,
Suggestions varchar(500) ,
primary key(ID),
foreign key(BookingID_customized) references Booking(Booking_ID),
foreign key(BookingID_package) references Book_package(Booking_ID)
);


create table Group_details(
Serial_No int auto_increment primary key,
ID int,
BookingID_customized int,
BookingID_package int,
Name varchar(255),
DOB varchar(255),
Gender varchar(255),
Email varchar(255),
Mobile_number bigint,
Alternate_mobile_number bigint,
Address varchar(255),
Passport_number varchar(255),
foreign key(ID) references Register(ID),
foreign key(BookingID_customized) references Booking(Booking_ID),
foreign key(BookingID_package) references Book_package(Booking_ID)
);
