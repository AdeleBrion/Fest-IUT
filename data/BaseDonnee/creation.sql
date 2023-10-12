DROP TABLE IF EXISTS DOCUMENT;
DROP TABLE IF EXISTS PHOTO;
DROP TABLE IF EXISTS VIDEO;
DROP TABLE IF EXISTS JOUER;
DROP TABLE IF EXISTS APPARTIENT;
DROP TABLE IF EXISTS ARTISTE;
DROP TABLE IF EXISTS TYPEINSTRUMENT;
DROP TABLE IF EXISTS ACTIVITEANNEXE;
DROP TABLE IF EXISTS PLANIFIER;
DROP TABLE IF EXISTS ACCUEILIR;
DROP TABLE IF EXISTS INSCRIRE;
DROP TABLE IF EXISTS HEBERGEMENT;
DROP TABLE IF EXISTS FAVORISER;
DROP TABLE IF EXISTS CONCERT;
DROP TABLE IF EXISTS GROUPEMUSICAL;
DROP TABLE IF EXISTS STYLE;
DROP TABLE IF EXISTS BILLET;
DROP TABLE IF EXISTS SPECTATEUR;
DROP TABLE IF EXISTS LIEU;

create table LIEU(
    id_lieu int not null primary key,
    nom_lieu varchar(30) not null,
    capacite_max int not null,
    adresse varchar(30) not null,
    photo_lieu blob
);

create table SPECTATEUR(
    id_spectateur int not null primary key,
    nom varchar(30),
    prenom varchar(30),
    email varchar(50),
    mot_de_passe varchar(50),
    adresse varchar(50),
    autres_informations varchar(150)
);

create table BILLET (
    id_billet int not null primary key,
    id_spectateur int,
    duree int not null, -- en jours
    prix int not null,
    date_valide DATE,
    foreign key (id_spectateur) references SPECTATEUR(id_spectateur)
);

create table STYLE(
    id_style int not null primary key,
    nom_style varchar(30)
);

create table GROUPEMUSICAL(
    id_groupe int not null primary key,
    id_style int,
    nom_groupe varchar(70),
    descritpion varchar(70),
    reseaux varchar(100),
    foreign key (id_style) references STYLE(id_style)
);

create table CONCERT(
    id_concert int not null primary key,
    id_lieu int,
    id_groupe int,
    nom_concert varchar(50) not null,
    dateheure_debut Timestamp not null,
    duree_concert int not null, -- en minutes
    duree_demontage int not null, -- en minutes
    duree_montage int not null, -- en minutes
    place_restante int not null,
    ouvert boolean not null,
    foreign key (id_lieu) references LIEU(id_lieu),
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe)
);

create table INSCRIRE(
    id_concert int,
    id_spectateur int,
    primary key(id_concert,id_spectateur),
    foreign key (id_concert) references CONCERT(id_concert),
    foreign key (id_spectateur) references SPECTATEUR(id_spectateur)
);

create table FAVORISER(
    id_spectateur int not null,
    id_concert int not null,
    primary key(id_spectateur, id_concert),
    foreign key  (id_spectateur) references SPECTATEUR(id_spectateur),
    foreign key  (id_concert) references CONCERT(id_concert)
);

create table HEBERGEMENT(
    id_Heb int not null primary key,
    nom_hebergement varchar(30) not null,
    nb_Max int not null
);
create table ACCUEILIR(
    id_groupe int,
    id_Heb int,
    dateheure_heb Timestamp, -- JJ/MM/YYYY
    nb_personne int,
    primary key (id_groupe,id_Heb,dateheure_heb),
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe),
    foreign key (id_Heb) references HEBERGEMENT(id_Heb)
);

create table PLANIFIER(
    id_groupe int not null,
    id_activite int not null,
    primary key (id_groupe,id_activite),
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe),
    foreign key (id_activite) references ACTIVITE(id_activite)
);

create table ACTIVITEANNEXE(
    id_activite int not null primary key,
    descriptionA varchar(80) not null,
    dateheure_activite Timestamp,
    access boolean not null
);

create table TYPEINSTRUMENT(
    id_type_instrument int not null primary key,
    nom_type_instrument varchar(30) not null
);

create table ARTISTE(
    id_artiste int not null primary key,
    nom_artiste varchar(30) not null
);

create table JOUER(
    id_type_instrument int,
    id_artiste int,
    primary key(id_type_instrument,id_artiste),
    foreign key (id_type_instrument) references TYPEINSTRUMENT(id_type_instrument),
    foreign key (id_artiste) references ARTISTE(id_artiste)
);

create table APPARTIENT(
    id_groupe int,
    id_artiste int,
    primary key (id_artiste,id_groupe),
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe),
    foreign key (id_artiste) references ARTISTE(id_artiste)
);

create table PHOTO(
    id_Photo int not null primary key,
    id_groupe int,
    file_path_photo varchar(50)
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe)
);

create table PHOTO(
    id_Photo int not null primary key,
    id_groupe int,
    file_path_photo varchar(50)
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe)
);

create table VIDEO(
    id_video int not null primary key,
    id_groupe int,
    file_path_video varchar(50)
    foreign key (id_groupe) references GROUPEMUSICAL(id_groupe)
);



