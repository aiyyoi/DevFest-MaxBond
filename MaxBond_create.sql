-- Created by Vertabelo (http://vertabelo.com)
-- Script type: create
-- Scope: [tables, references, sequences, views, procedures]
-- Generated at Fri Feb 06 23:00:19 UTC 2015




-- tables
-- Table Tag
CREATE TABLE Tag (
    tid int    NOT NULL ,
    name varchar(255)    NOT NULL ,
    category int    NOT NULL ,
    CONSTRAINT Tag_pk PRIMARY KEY (tid)
);

-- Table User
CREATE TABLE User (
    uid int    NOT NULL ,
    name varchar(255)    NOT NULL ,
    gender int    NOT NULL ,
    image varchar(255)    NOT NULL ,
    CONSTRAINT User_pk PRIMARY KEY (uid)
);

-- Table has_tag
CREATE TABLE has_tag (
    id int    NOT NULL ,
    Tag_tid int    NOT NULL ,
    User_uid int    NOT NULL ,
    CONSTRAINT has_tag_pk PRIMARY KEY (id)
);





-- foreign keys
-- Reference:  has_tag_Tag (table: has_tag)


ALTER TABLE has_tag ADD CONSTRAINT has_tag_Tag FOREIGN KEY has_tag_Tag (Tag_tid)
    REFERENCES Tag (tid);
-- Reference:  has_tag_User (table: has_tag)


ALTER TABLE has_tag ADD CONSTRAINT has_tag_User FOREIGN KEY has_tag_User (User_uid)
    REFERENCES User (uid);



-- End of file.

