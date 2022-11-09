CREATE DATABASE skymovie_christmas;

use skymovie_christmas;

create table movies(
film_id int UNIQUE NOT NULL auto_increment,
film_title varchar(50) NOT NULL,
film_synopsis varchar(255) default "Spynosis not available",
film_year int(4) NOT NULL,
film_cert varchar(5) NOT NULL,
Primary key (film_id));

insert into movies(film_title, film_synopsis, film_year, film_cert) Values("8 Bit Christmas", "In 1980s Chicago, a young boy begins a quest to get the latest and greatest video game system for Christmas. Neil Patrick Harris stars.", 2021, "PG");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("A Frozen Christmas: Santa's Return", "Spend some quality time with Santa and his elf pals as they celebrate finishing the Christmas run by telling some classic festive tales. Animated fun.", 2017, "U");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("Arthur Christmas", "When Father Christmas inadvertently overlooks one small child on Christmas Eve his accident-prone son Arthur must step into the breach and deliver that last present. ", 2011, "U");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("The Muppet Christmas Carol", "Michael Caine guests as Ebenezer Scrooge in this Muppet version of the classic tale of an old miser's redemption on Christmas Eve. ", 1992, "U");
select * from movies;

insert into movies(film_title, film_synopsis, film_year, film_cert) Values("Bad Santa", "The crotchety Willie T. Soke (Billy Bob Thornton) and his partner (Tony Cox) reunite once a year for a holiday con. Posing as a mall Santa and his elf, they rip off shopping outlets on Christmas Eve. ", 2003, "15");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("The Grinch", "The Grinch and his loyal dog, Max, live a solitary existence inside a cave on Mount Crumpet. His main source of aggravation comes during Christmastime when his neighbours in Whoville celebrate the holidays with a bang.  ", 2018, "U");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("Fred Claus", "When Fred's criminal ways finally land him in big trouble, Nicholas bails him out and brings him to the North Pole to work off the debt by making toys. ", 2007, "PG");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("Home Alone", "A young boy is forgotten when his large family rushes to catch a plane for Paris at Christmas. ", 1990, "PG");
insert into movies(film_title, film_synopsis, film_year, film_cert) Values("Home Alone 2: Lost in New York", "After youth Kevin McCallister (Macaulay Culkin) loses track of his father at the airport, he mistakenly gets on a plane headed for New York City -- while the rest of the McCallisters fly to Florida. ", 1992, "PG"),("Jack Frost", "A father passes away but comes back to life in the form of a snowman. ", 1998, "PG"),("Die Hard", "Die Hard follows New York City police detective John McClane (Willis) who is caught up in a terrorist takeover ", 1988, "18"),("The Holiday", "Two women swap homes at Christmastime after bad breakups with their boyfriends. Each woman finds romance and romantic comedy ensues, Starring Kate Winslet, Cameron Diaz, Jude Law and Jack Black. ", 2006, "PG");

ALTER TABLE movies ADD COLUMN title_imsge varchar(255) default "Image not available";

DESCRIBE movies;

ALTER TABLE movies ADD COLUMN run_Time varchar(20) not null;

SELECT * from movies;

ALTER TABLE movies rename COLUMN title_imsge to title_image;

ALTER TABLE movies add column sky_store varchar(255) default "Movie not available for purchase or rent";

UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_C47E8B5A-5764-42D5-AE8A-C7C3591751F5_2022-5-18-T15-7-10.jpg?s=260x371", sky_store="https://www.skystore.com/product/8-bit-christmas/c47e8b5a-5764-42d5-ae8a-c7c3591751f5" WHERE film_id=1;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_E08EC132-DE4C-4E7F-831E-D1ED8A6ECDE3_2022-2-14-T12-19-28.jpg?s=260x371", sky_store="https://www.skystore.com/product/a-frozen-christmas-santas-return/e08ec132-de4c-4e7f-831e-d1ed8a6ecde3" WHERE film_id=2;

UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_79F25D59-C4A1-4171-B7A9-41563B93ABF8_2021-8-11-T15-53-3.jpg?s=260x371", sky_store="https://www.skystore.com/product/arthur-christmas/79f25d59-c4a1-4171-b7a9-41563b93abf8" WHERE film_id=3;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_B3A7EC49-1B68-4C1F-A787-E8595724DAA0_2022-6-22-T11-9-2.jpg?s=260x371", sky_store="https://www.skystore.com/product/the-muppet-christmas-carol/b3a7ec49-1b68-4c1f-a787-e8595724daa0" WHERE film_id=4;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_1C904387-E6E3-4AFB-A7CC-8F21FF570D40_2020-7-2-T12-1-19.jpg?s=260x371", sky_store="https://www.skystore.com/product/bad-santa/1c904387-e6e3-4afb-a7cc-8f21ff570d40" WHERE film_id=5;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_917BE252-FD02-49AA-B1D7-45CBD96CE066_2019-11-15-T14-6-16.jpg?s=260x371", sky_store="https://www.skystore.com/product/the-grinch-2018/917be252-fd02-49aa-b1d7-45cbd96ce066" WHERE film_id=6;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_42CB8F56-5D3E-4713-BC48-B5425EF22659_2022-5-16-T21-52-36.jpg?s=260x371", sky_store="https://www.skystore.com/product/fred-claus/42cb8f56-5d3e-4713-bc48-b5425ef22659" WHERE film_id=7;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_91E9473B-1530-47E1-9A63-33AC42A4BDFF_2022-8-28-T11-48-55.jpg?s=260x371", sky_store="https://www.skystore.com/product/home-alone/91e9473b-1530-47e1-9a63-33ac42a4bdff" WHERE film_id=8;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_E2BA6C74-7F07-4B04-ABA1-F243AC1C97D9_2022-9-14-T2-23-16.jpg?s=260x371", sky_store="https://www.skystore.com/product/home-alone-2-lost-in-new-york/e2ba6c74-7f07-4b04-aba1-f243ac1c97d9" WHERE film_id=9;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_7E3E75DB-5A13-4AE6-92CE-12707AA85A48_2022-6-16-T11-9-33.jpg?s=260x371", sky_store="https://www.skystore.com/product/jack-frost-1998/7e3e75db-5a13-4ae6-92ce-12707aa85a48" WHERE film_id=10;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_CF81A8D9-BBC0-40CA-89DE-49EF761A83B9_2022-8-15-T21-50-6.jpg?s=260x371", sky_store="https://www.skystore.com/product/die-hard/cf81a8d9-bbc0-40ca-89de-49ef761a83b9" WHERE film_id=11;
UPDATE movies SET title_image="https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_A73FBA93-AE4D-4124-8029-AFFCC95C33B9_2020-12-18-T11-21-59.jpg?s=260x371", sky_store="https://www.skystore.com/product/the-holiday/a73fba93-ae4d-4124-8029-affcc95c33b9" WHERE film_id=12;

UPDATE movies SET film_cert="12" WHERE film_id=12;