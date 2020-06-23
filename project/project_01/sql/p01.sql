CREATE TABLE buylist(
    buylist_id number,
    buylist_date date,
    buylist_totalprice number,
    constraint buyList_pk PRIMARY KEY(buylist_id)
);

create table buy(
    buy_id number,
    buylist_id number,
    buy_price number,
    buy_productname varchar2(40),
    buy_cnt number,
    constraint buy_pk PRIMARY KEY(buy_id),
    CONSTRAINT buy_fk1 FOREIGN KEY(buylist_id) REFERENCES buylist(buylist_id)
);

create sequence seq_buylist_pk;
create sequence seq_buy_pk;

