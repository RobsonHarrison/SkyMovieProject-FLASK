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

