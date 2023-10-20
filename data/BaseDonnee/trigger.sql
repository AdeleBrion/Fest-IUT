DELIMITER|
CREATE OR REPLACE TRIGGER ConcertPlein BEFORE INSERT ON INSCRIRE FOR EACH ROW
BEGIN
    declare nbSpec int;
    declare nbMax int;
    declare mes varchar(100);
    select count(idSpectateur) into nbSpec from INSCRIRE where idConcert=new.idConcert;
    select placeRestante into nbMax from CONCERT where idConcert=new.idConcert;
    if nbSpec+1 > nbMax then
        set mes = concat('Le concert ', new.idConcert, ' ne peut pas accepté');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
END |
DELIMITER ;