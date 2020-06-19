CREATE TABLE CONTACT(
    contact_name VARCHAR2(40),
    PHONE VARCHAR2(40),
    EMAIL VARCHAR2(40),
    ADDR VARCHAR2(40)
);
alter table contact rename column name to contact_name;
delete from CONTACT where NAME = '¤²¤²¤²';
