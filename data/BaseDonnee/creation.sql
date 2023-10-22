create table LIEU(
    idLieu int not null primary key,
    nomLieu varchar(100) not null,
    capaciteMax int not null,
    adresse varchar(200) not null,
    photoLieu blob
);

create table SPECTATEUR(
    idSpectateur int not null primary key,
    nomSpectateur varchar(30) not null,
    prenom varchar(30) not null,
    email varchar(50) not null,
    motDePasse varchar(50) not null,
    adresse varchar(50) not null,
    infoAnnexes varchar(150)
);

create table BILLET (
    idBillet int not null primary key,
    idSpectateur int,
    duree int not null, -- en jours
    prix int not null,
    dateValidite DATE,
    foreign key (idSpectateur) references SPECTATEUR(idSpectateur)
);

create table STYLE(
    idStyle int not null primary key,
    nomStyle varchar(30)
);

create table SOUSSTYLE(
    idStyle int,
    sousStyle int,
    foreign key (idStyle) references STYLE(idStyle),
    foreign key (sous_style) references STYLE(idStyle)
);

create table GROUPEMUSICAL(
    idGroupe int not null primary key,
    idStyle int,
    nomGroupe varchar(70) not null,
    descriptionGroupe varchar(70) not null,
    foreign key (idStyle) references STYLE(idStyle)
);

create table RESEAUX(
    idReseau int not null primary key,
    idGroupe int,
    x varchar(100),
    instagram varchar(100),
    tiktok varchar(100),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe)
);

create table CONCERT(
    idConcert int not null primary key,
    idLieu int,
    idGroupe int,
    nomConcert varchar(50) not null,
    dateHeureDebut Timestamp not null,
    dureeConcert int not null, -- en minutes
    dureeMontage int not null, -- en minutes
    dureeDemontage int not null, -- en minutes
    placesRestantes int not null,
    ouvertATous boolean not null,
    foreign key (idLieu) references LIEU(idLieu),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe)
);

create table INSCRIRE(
    idConcert int,
    idSpectateur int,
    primary key(idConcert,idSpectateur),
    foreign key (idConcert) references CONCERT(idConcert),
    foreign key (idSpectateur) references SPECTATEUR(idSpectateur)
);

create table FAVORISER(
    idSpectateur int not null,
    idConcert int not null,
    primary key(idSpectateur, idConcert),
    foreign key  (idSpectateur) references SPECTATEUR(idSpectateur),
    foreign key  (idConcert) references CONCERT(idConcert)
);

create table HEBERGEMENT(
    idHebergement int not null primary key,
    nomHebergement varchar(30) not null,
    nbMax int not null
);

create table ACCUEILIR(
    idGroupe int,
    idHebergement int,
    dateHeureDeb Timestamp, -- JJ/MM/YYYY
    nbPersonne int not null,
    primary key (idGroupe,idHebergement,dateHeureDeb),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe),
    foreign key (idHebergement) references HEBERGEMENT(idHebergement)
);

create table ACTIVITEANNEXE(
    idActivite int not null primary key,
    descriptionActivite varchar(80) not null,
    dateheureActivite Timestamp,
    accessibleAuPublic boolean not null
);

create table PLANIFIER(
    idGroupe int not null,
    idActivite int not null,
    dureePlanification int not null, -- En Heures
    primary key (idGroupe,idActivite),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe),
    foreign key (idActivite) references ACTIVITEANNEXE(idActivite)
);

create table TYPEINSTRUMENT(
    idTypeInstrument int not null primary key,
    nomTypeInstrument varchar(30) not null
);

create table ARTISTE(
    idArtiste int not null primary key,
    nomArtiste varchar(30) not null
);

create table JOUER(
    idTypeInstrument int,
    idArtiste int,
    primary key(idTypeInstrument,idArtiste),
    foreign key (idTypeInstrument) references TYPEINSTRUMENT(idTypeInstrument),
    foreign key (idArtiste) references ARTISTE(idArtiste)
);

create table APPARTIENT(
    idGroupe int,
    idArtiste int,
    primary key (idArtiste,idGroupe),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe),
    foreign key (idArtiste) references ARTISTE(idArtiste)
);

create table PHOTO(
    idPhoto int not null primary key,
    idGroupe int,
    filePathPhoto varchar(100),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe)
);

create table VIDEO(
    idVideo int not null primary key,
    idGroupe int,
    filePathVideo varchar(50),
    foreign key (idGroupe) references GROUPEMUSICAL(idGroupe)
);
