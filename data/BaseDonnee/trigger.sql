DELIMITER |
CREATE OR REPLACE TRIGGER ConcertPlein BEFORE INSERT ON INSCRIRE FOR EACH ROW
BEGIN
    declare nbSpec int;
    declare nbMax int;
    declare mes varchar(100);
    select count(idSpectateur) into nbSpec from INSCRIRE where idConcert=new.idConcert;
    select placesRestantes into nbMax from CONCERT where idConcert=new.idConcert;
    if nbSpec+1 > nbMax then
        set mes = concat('Le concert ', new.idConcert, ' ne peut pas accepté');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
END |
DELIMITER ;

DELIMITER |
CREATE OR REPLACE TRIGGER CHEVAUCHEMENTACTIVITE BEFORE INSERT ON PLANIFIER FOR EACH ROW
BEGIN
    declare idActiA int;
    declare dateHA Timestamp;
    declare duree int;
    declare fin_activite Timestamp;
    declare fin_activite_new Timestamp;
    declare debut_activite Timestamp;
    declare mes varchar(100);
    DECLARE fini boolean default FALSE;
    
    declare lesActivite cursor for 
        select idActivite, dateheureActivite, dureePlanification
        from ACTIVITEANNEXE natural join PLANIFIER
        where idGroupe = new.idGroupe;
    declare continue handler for not found set fini = TRUE;

    SELECT dateheureActivite INTO debut_activite FROM ACTIVITEANNEXE WHERE idActivite = NEW.idActivite;

    open lesActivite;
    while not fini DO
        fetch lesActivite into idActiA, dateHA, duree;
        if not fini then
            set fin_activite = TIMESTAMPADD(HOUR, duree, dateHA);
            set fin_activite_new = TIMESTAMPADD(HOUR, new.dureePlanification, debut_activite);
            if (fin_activite >= debut_activite and fin_activite <= fin_activite_new) or (fin_activite_new >= debut_activite and fin_activite_new <= fin_activite) then
                set mes = concat('L activité ', idActiA, ' ne peut pas être planifiée car elle chevauche une autre activité du même groupe');
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
            end if;
        end if;
    end while;
    CLOSE lesActivite;
END |
DELIMITER ;

DELIMITER |
CREATE OR REPLACE TRIGGER CHEVAUCHEMENTCONCERT BEFORE INSERT ON CONCERT FOR EACH ROW
BEGIN
    declare idConcertelem int;
    declare dateHeureDebutelem Timestamp;
    declare duree int;
    declare dureeMontageelem int;
    declare dureeDemontageelem int;
    declare total int;
    declare fin_concert Timestamp;
    declare debut_concert Timestamp;
    declare total_new int;
    declare fin_concert_new Timestamp;
    declare debut_concert_new Timestamp;
    declare mes varchar(100);

    declare fini boolean default false;
    declare lesConcert cursor for 
        select idConcert, dateHeureDebut, dureeConcert, dureeMontage, dureeDemontage
        from CONCERT
        where idLieu=new.idLieu;
    declare continue handler for not found set fini = true;
    open lesConcert;
    while not fini do
        fetch lesConcert into idConcertelem, dateHeureDebutelem, duree, dureeMontageelem, dureeDemontageelem;
        if not fini then
            set total = (duree + dureeDemontageelem);
            set debut_concert = TIMESTAMPADD(MINUTE, -dureeMontageelem ,dateHeureDebutelem);
            set fin_concert = TIMESTAMPADD(MINUTE, total, dateHeureDebutelem);

            set total_new = (new.dureeConcert + new.dureeDemontage);
            set fin_concert_new = TIMESTAMPADD(MINUTE, total_new, new.dateHeureDebut);
            set debut_concert_new = TIMESTAMPADD(MINUTE, -new.dureeMontage, new.dateHeureDebut);

            IF (fin_concert >= debut_concert_new AND fin_concert <= fin_concert_new) OR 
            (fin_concert_new >= debut_concert_new AND fin_concert_new <= fin_concert) OR
            (debut_concert >= debut_concert_new AND debut_concert <= fin_concert_new) OR
            (debut_concert_new >= debut_concert AND debut_concert_new <= fin_concert) then
                set mes = concat('Le concert ', idConcertelem, ' ne peut pas être planifiée car il chevauche un autre concert pour un même lieu');
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
            end if;            
        end if;
    end while;
END |
DELIMITER ;
