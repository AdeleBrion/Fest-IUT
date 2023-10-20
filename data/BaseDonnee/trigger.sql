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