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

DELIMITER|
CREATE OR REPLACE TRIGGER HabitationPlein BEFORE INSERT ON ACCUEILIR FOR EACH ROW
BEGIN
    declare nbPerson int;
    declare nbMax int;
    declare mes varchar(100);
    select nbMax into nbMax from HEBERGEMENT where idHeb=new.idHeb;
    select sum(nbPersonne) into nbPerson from ACCUEILIR where idHeb=new.idHeb and dateheureHeb=new.dateheure_heb;
    if nbPerson+new.nbPersonne > nbMax then
        set mes = concat('L hebergement ', new.idHeb, ' ne peut pas accépté autant de personne');
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if;
END |
DELIMITER ;

DELIMITER|
CREATE OR REPLACE TRIGGER CHEVAUCHEMENTACTIVITE BEFORE INSERT ON PLANIFIER FOR EACH ROW
BEGIN
    declare idActiA int;
    declare dateHA Timestamp;
    declare duree int;
    declare inter INTERVAL;
    declare fin_activite Timestamp;

    declare inter_new INTERVAL;
    declare fin_activite_new Timestamp;

    declare fini boolean default false;
    declare lesActivite cursor for 
        select idActivite, dateHeureA, dureePlanification
        from ACTIVITEANNEXE natural join PLANIFIER
        where idGroupe=new.idGroupe;
    declare continue handler for not found set fini = true;
    open lesActivite;
    while not fini then
        fetch lesActivite into idActiA, dateHA, duree;
        if not fini then
            set inter = NUMTODSINTERVAL(duree, 'HOUR');
            set fin_activite = dateHA + inter;

            set inter_new = NUMTODSINTERVAL(new.duree, 'HOUR');
            set fin_activite_new = new.dateHA + inter_new;
            if (fin_activite >= new.dateHA and fin_activite <= fin_activite_new) or (fin_activite_new >= new.dateHA and fin_activite_new <= fin_activite) then
                set mes = concat('L activité ', idActiA, ' ne peut pas être planifiée car elle chevauche une autre activité du même groupe');
            end if;
        end if;
    end while;
END |
DELIMITER ;

DELIMITER |
CREATE OR REPLACE TRIGGER CHEVAUCHEMENTCONCERT BEFORE INSERT ON CONCERT FOR EACH ROW
BEGIN
    declare idConcert int;
    declare dateHeureDebut Timestamp;
    declare duree int;
    declare dureeMontage int;
    declare dureeDemontage int;
    declare inter INTERVAL;
    declare fin_concert Timestamp;

    declare inter_new INTERVAL;
    declare fin_concert_new Timestamp;

    declare fini boolean default false;
    declare lesConcert cursor for 
        select idConcert, dateHeureDebut, dureeConcert, dureeMontage, dureeDemontage
        from CONCERT
        where idLieu=new.idLieu;
    declare continue handler for not found set fini = true;
    open lesConcert;
    while not fini do
        fetch lesConcert into idConcert, dateHeureDebut, duree, dureeMontage, dureeDemontage;
        if not fini then
            set inter = NUMTODSINTERVAL((duree + dureeMontage + dureeDemontage), 'MINUTE');
            set fin_concert = dateHeureDebut + inter;

            set inter_new = NUMTODSINTERVAL((new.dureeConcert + new.dureeMontage + new.dureeDemontage), 'MINUTE');
            set fin_concert_new = new.dateHeureDebut + inter_new;
            if (fin_concert >= new.dateHeureDebut and fin_concert <= fin_concert_new) or (fin_concert_new >= new.dateHeureDebut and fin_concert_new <= fin_concert) then
                set mes = concat('Le concert ', idConcert, ' ne peut pas être planifiée car il chevauche un autre concert pour un même lieu');
            end if;
        end if;
    end while;
END |
DELIMITER ;
