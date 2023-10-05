DROP TABLE IF EXISTS DOCUMENT;
DROP TABLE IF EXISTS ARTISTE;
DROP TABLE IF EXISTS INSTRUMENT;
DROP TABLE IF EXISTS ACTIVITEANNEXE;
DROP TABLE IF EXISTS PLANIFIER;
DROP TABLE IF EXISTS ACCUEILIR;
DROP TABLE IF EXISTS HEBERGEMENT;
DROP TABLE IF EXISTS FAVORISER;
DROP TABLE IF EXISTS CONCERT;
DROP TABLE IF EXISTS GROUPEMUSICAL;
DROP TABLE IF EXISTS STYLE;
DROP TABLE IF EXISTS BILLET;
DROP TABLE IF EXISTS SPECTATEUR;
DROP TABLE IF EXISTS LIEU;

create table LIEU (
    idLieu int not null primary key,
    nom varchar(30) not null,
    capaciteMax int not null,
    adresse varchar(30) not null,
    photo blob
);
create table SPECTATEUR(
    idSpectateur int not null primary key,
    nom varchar(30),
    prenom varchar(30),
    email varchar(50),
    mdp varchar(50),
    adresse varchar(50),
    infoAnnexes varchar(150)
);

create table BILLET (
    idBillet int not null primary key,
    idSpectateur int,
    duree int not null, -- en jours
    prix int not null,
    dateValidite DATE,
    foreign key(idSpectateur) references SPECTATEUR(idSpectateur)
);

create table STYLE(
    idStyle int not null primary key,
    nomStyle varchar(30)
);

create table GROUPEMUSICAL(
    idGroupe int not null primary key,
    idStyle int,
    nom varchar(70),
    descritpion varchar(70),
    reseaux varchar(100),
    foreign key(idStyle) references STYLE(idStyle)
);

create table CONCERT(
    idConcert int not null primary key,
    idLieu int,
    idGroupe int,
    nom varchar(50) not null,
    dateHeureDebut Timestamp not null,
    dureeConcert int not null, -- en minutes
    dureeMontage int not null, -- en minutes
    dureeDemontage int not null, -- en minutes
    placeRestante int not null,
    ouvertATous boolean not null,
    foreign key(idLieu) references LIEU(idLieu),
    foreign key(idGroupe) references GROUPEMUSICAL(idGroupe)
);

create table FAVORISER(
    idSpectateur int not null,
    idConcert int not null,
    primary key(idSpectateur, idConcert),
    foreign key(idSpectateur) references SPECTATEUR(idSpectateur),
    foreign key (idConcert) references CONCERT(idConcert)
);

create table HEBERGEMENT(
    idHeb int not null primary key,
    nom varchar(30) not null,
    capaciteMax int not null
);
create table ACCUEILIR(
    idGroupe int,
    idHeb int,
    dateHeureDebut Timestamp,
    nbPersonne int,
    primary key (idGroupe,idHeb,dateHeureDebut),
    foreign key(idGroupe) references GROUPEMUSICAL(idGroupe),
    foreign key(idHeb) references HEBERGEMENT(idHeb)
);

create table PLANIFIER(
    idGroupe int not null,
    idActivite int not null
);

create table ACTIVITEANNEXE(
    idActivite int not null primary key,
    descriptionA varchar(80) not null,
    dateHeureA Timestamp,
    accessibleAuPublic boolean not null
);

create table INSTRUMENT(
    idInstrument int not null primary key,
    nom varchar(30) not null,
    idArtiste int
);

create table ARTISTE(
    idArtiste int not null primary key,
    nom varchar(30) not null,
    idInstrument int,    -- ça devrait dégager
    foreign key (idInstrument) references INSTRUMENT(idInstrument)   --et du coup ça aussi, ça devrait dégager
);

create table DOCUMENT(
    idDocument int not null primary key,
    nom varchar(30) not null,
    -- il manque le type
    idGroupe int,
    filePath varchar(150),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe)
);

