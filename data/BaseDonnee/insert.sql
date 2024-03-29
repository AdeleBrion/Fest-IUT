INSERT INTO ROLE (idRole, nomRole) VALUES
    (1, 'Spectateur'),
    (2, 'Administrateur');

INSERT INTO SPECTATEUR (idSpectateur, nomSpectateur, prenom, email, motDePasse, adresse, infoAnnexes, idRole) VALUES
    (1, "DUPONT", "Jean", "dupont.jean@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "1 rue de la paix", "rien à signaler",1),
    (2, "MARTIN", "Lucie", "lucie.martin@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "2 rue de la liberté", "fan de rock",1),
    (3, "DURAND", "Pierre", "pierre.durand@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "3 rue de la république", "amateur de jazz",1),
    (4, "LEFEVRE", "Sophie", "sophie.lefevre@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "4 rue de la gare", "fan de musique classique",1),
    (5, "MOREAU", "Antoine", "antoine.moreau@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "5 rue de la poste", "amateur de blues",1),
    (6, "ROUSSEAU", "Marie", "marie.rousseau@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "6 rue de la mairie", "fan de pop",1),
    (7, "GIRARD", "Thomas", "thomas.girard@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "7 rue de l'église", "amateur de musique électronique",1),
    (8, "BERNARD", "Julie", "julie.bernard@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "8 rue de la plage", "fan de reggae",1),
    (9, "PETIT", "Nicolas", "nicolas.petit@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "9 rue de la forêt", "amateur de hip-hop",1),
    (10, "ROUX", "Céline", "celine.roux@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "10 rue de la montagne", "fan de métal",1),
    (11, "CHIDLOVSKY", "Léopold", "leopold.chidlovsky@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "11 avenue des figuiers", "fan de rock",1),
    (12, "DEMARET", "Sullivan", "sullivan.demaret@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "12 boulevard de la délinquance", "amateur de k-pop",1),
    (13, "MOREIRA", "Daniel", "daniel.moreira@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "13 rue du repas", "fan de j-pop",1),
    (14, "BRION", "Adèle", "adele.brion@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "14 rue de l'agonie", "fan de k-pop",2),
    (15, "LUDMANN", "Dorian", "dorian.ludmann@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "15 rue du Hibou", "fan de deathfonk",1),
    (16, "GRUSON--DELANNOY", "Jules", "jules.gruson-delannoy@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "16 impasse de la réussite", "amateur de j-pop",1),
    (17, "LALLIER", "Anna", "anna.lallier@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "17 impasse du retard", "fan de rock",1),
    (18, "DUBOIS", "Tom", "tom.dubois@gmail.com", "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "18 avenue de Couasnon", "fan de classique",1),
    (19, "MAUPOU", "Cassandra", "cassandra.maupou@gmail.com","f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9", "19 boulevard du 50/50", "fan de rap américain",1);

INSERT INTO TYPEBILLET(idTypeBillet, intitule, description, prix, duree) VALUES
    (1, "Day'ut", "Vous voulez assister au festival pour un jour ? \n Ce billet est fait pour vous ! Vous pourrez profiter toute la journée des concerts de vos artistes favoris. \n Le ticket est valable pour le jour séléctionné de l'ouverture du festival jusqu'à sa fermeture.", 25, 1),
    (2, "Four'ut", "Vous voulez assister au festival pour quelques jours ? \n Ce billet est fait pour vous ! Vous pourrez profiter toute la journée des concerts de vos artistes favoris. \n Le ticket est valable pour le jour séléctionné de l'ouverture du festival jusqu'à sa fermeture.", 60, 4),
    (3, "Week'ut", "Vous voulez assister au festival pour un jour ? \n Ce billet est fait pour vous ! Vous pourrez profiter toute la journée des concerts de vos artistes favoris. \n Le ticket est valable pour le jour séléctionné de l'ouverture du festival jusqu'à sa fermeture.", 120, 7);
    

INSERT INTO BILLET (idBillet, idSpectateur, idTypeBillet, dateDebut) VALUES
    (1, 1, 1, "2023-12-21"),
    (2, 1, 1, "2023-12-18"),
    (3, 2, 2, "2023-12-11"),
    (4, 2, 1, "2023-12-18"),
    (5, 3, 2, "2023-12-12"),
    (6, 4, 1, "2023-12-12"),
    (7, 4, 2, "2023-12-18"),
    (8, 5, 2, "2023-12-14"),
    (9, 6, 3, "2023-12-20"),
    (10, 7, 1, "2023-12-14"),
    (11, 7, 3, "2023-12-18"),
    (12, 8, 2, "2023-12-08"),
    (13, 9, 1, "2023-12-14"),
    (14, 9, 3, "2023-12-18");

INSERT INTO STYLE (idStyle, nomStyle, imageStyle) VALUES
    (1, "rock", "rock.jpg"),
    (2, "jazz", "jazz.jpg"),
    (3, "musique classique", "classique.jpg"),
    (4, "blues", null),
    (5, "pop", "pop.jpg"),
    (6, "k-pop", "k-pop.jpg"),
    (7, "rap", "rap.jpg"),
    (8, 'techno', "techno.jpg"),
    (9, "grunge", null),
    (10, "j-pop", null);

INSERT INTO SOUSSTYLE (idStyle, sousStyle) VALUES
    (1, 9),
    (5, 6),
    (5, 10);

INSERT INTO GROUPEMUSICAL (idGroupe, idStyle, nomGroupe, descriptionGroupe) VALUES
    -- ROCK (1.6)
    (1, 1, "The Rolling Stones", "Groupe de rock britannique"),
    (2, 1, "Waterparks", "Groupe de Electro-Rock américain"),
    (3, 1, "Bring Me The Horizon", "Groupe de Metal britannique"),
    (4, 1, "Spirit Box", "Groupe de Metal canadien"),
    (5, 1, "Muse", "Groupe de Rock britannique"),
    (6, 1, "Red Hot Chili Peppers", "Groupe de Fusion américain"),
    -- JAZZ(7.12)
    (7, 2, "Essaïe Cid", "Saxophoniste et clarinetiste Espagnol"),
    (8, 2, "Xenos", "Groupe de jazz né en Bosnie, grandi en Grèce et désormais Parisien"),
    -- MUSIQUE CLASSIQUE(13.18)
    (13, 3, "Hahn & Taraud", "Duo international violon + piano"),
    (14, 3, "Yochen", "Duo asiatique violon + violoncelle"),
    -- BLUES(19.24)
    (19, 4, "Polyphia", "Groupe de Blues, originaire de Dallas"),
    -- POP(25.30)
    (25, 5, "Twenty One Pilots", "Duo de pop-music originaire de Colombus"),
    -- K-POP(31.36)
    (31, 6, "Itzy", "Groupe de musique coréenne composé de 5 membres"),
    (32, 6, "BlackPink", "Groupe de musique coréene composé de 4 membres"),
    (33, 6, "Xdinary Heroes", "Groupe de musique coréene composé de 6 membres"),
    -- RAP(37.42)
    (37, 7, "Bigflo et Oli", "Deux frères rappeurs français"),
    (38, 7, "Masked Wolf", "Légende du rap en Australie"),
    (39, 7, "Casseurs Flowters", "Duo de rappeurs originaires du Calvados"),
    -- TECHNO (43.47)
    (43, 8, "Dimitri Vegas & Like Mike", "Groupe de disc jockeys belges"),
    (44, 8, "The Chainsmokers", "Duo américain de disc jockeys et producteurs");


    
INSERT INTO LIEU (idLieu, nomLieu, capaciteMax, adresse, photoLieu) VALUES
    (1, "Place du Martroi", 1000, "place du Martroi", null),
    (2, "L'Institut", 500, "3 rue du Colombier", null),
    (3, "Parc Louis Pasteur", 200, "2 rue Eugène Vignat", null),
    (4, "Musée des beaux arts", 800, "1 rue Fernand Rabier", null),
    (5, "Parvis de la Collégiale Saint Pierre le Puellier", 50, "13 Cloître St Pierre le Puellier", null),
    (6, "Zenith Orléans", 6900, "1 rue du Président Robert Schuman", null),
    (7, "CO'Met, Palais des Congrès", 2000, "Rue du Président Robert Schuman", null),
    (8, "CO'Met, Parc des Expositions", 300, "Rue du Président Robert Schuman", null),
    (9, "CO'Met, Aréna", 10000, "Rue du Président Robert Schuman", null);


INSERT INTO CONCERT (idConcert, idLieu, idGroupe, nomConcert, dateHeureDebut, dureeConcert, dureeMontage, dureeDemontage, placesRestantes, ouvertATous) VALUES
    (1, 1, 1, "Concert des Rolling Stones", "2023-12-01 20:00:00", 120, 60, 60, 746, false),
    (2, 2, 2, "Concert de Waterparks", "2023-12-02 22:00:00", 150, 100, 50, 15, false),
    (3, 6, 3, "Concert de Bring Me The Horizon", "2023-12-03 20:00:00", 90, 30, 60, 5, false),
    (4, 3, 4, "Concert de Spirit Box", "2023-12-04 20:00:00", 180, 80, 100, 26, false),
    (5, 6, 5, "Concert de Muse", "2023-12-03 18:00:00", 120, 50, 70, 213, false),
    (6, 1, 6, "Concert de Red Hot Chilli Peppers", "2023-12-05 20:00:00", 200, 120, 80, 214, true),
    (7, 4, 37, "Concert de Bigflo et Oli", "2023-12-02 21:00:00", 120, 45, 45, 150, false),
    (8, 5, 43, "DJ Set du duo Dimitri Vegas & Like Mike", "2023-12-06 21:00:00", 180, 60, 70, 333, true),
    (9, 7, 31, "Concert de Itzy", "2023-12-05 15:00:00", 90, 180, 200, 800, true),
    (10, 8, 32, "Concert de BlackPink", "2023-12-06 15:00:00", 100, 160, 180, 900, true),
    (11, 9, 33, "Concert de Xdinary Heroes", "2023-12-04 15:00:00", 70, 170, 180, 850, true),
    (12, 9, 25, "The Icy Tour | Twenty One Pilots", "2023-12-01 15:00:00", 100, 120, 130, 830, true);

-- Pour testée le trigger CHEVAUCHEMENTCONCERT
-- INSERT INTO CONCERT (idConcert, idLieu, idGroupe, nomConcert, dateHeureDebut, dureeConcert, dureeMontage, dureeDemontage, placesRestantes, ouvertATous) VALUES
--     (8, 4, 33, "Concert", "2023-12-10 22:00:00", 120, 40, 50, 1345, false);

INSERT INTO FAVORISER (idSpectateur, idGroupe) VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4);

INSERT INTO HEBERGEMENT (idHebergement, nomHebergement, nbMax) VALUES
    (1, "Hôtel : suite 12A", 8),
    (2, "Hôtel : suite 13A", 10),
    (3, "Hôtel : suite 14A", 6),
    (4, "Hôtel : suite 15A", 18),
    (5, "Hôtel : suite 16A", 20),
    (6, "Hôtel : suite 22B", 15);


INSERT INTO ACCUEILIR (idGroupe, idHebergement, dateheureHeb, nbPersonne) VALUES
    (1, 1, "2023-12-01 16:00:00", 5),
    (2, 2, "2023-12-02 16:00:00", 10),
    (3, 3, "2023-12-18 20:00:00", 5),
    (4, 4, "2023-12-04 20:00:00", 10),
    (5, 5, "2023-12-18 15:00:00", 15),
    (6, 6, "2023-12-06 16:00:00", 10);


INSERT INTO ACTIVITEANNEXE (idActivite, descriptionActivite, dateheureActivite, accessibleAuPublic) VALUES
    (1, "Interview radio", "2023-12-01 16:00:00", true),
    (2, "Séance de dédicaces", "2023-12-02 18:00:00", false),
    (3, "Rencontre avec les fans", "2023-12-18 17:00:00", false),
    (4, "Conférence de presse", "2023-12-18 15:00:00", true),
    (5, "Séance de photos", "2023-12-04 16:00:00", false),
    (6, "Rencontre avec les journalistes", "2023-12-06 14:00:00", true),
    (7, "Séance de dédicaces", "2023-12-07 18:00:00", false),
    (8, "Rencontre avec les fans", "2023-12-08 17:00:00", false),
    (9, "Conférence de presse", "2023-12-09 15:00:00", true),
    (10, "Séance de photos", "2023-12-10 16:00:00", false),
    (11, "Rencontre avec les journalistes", "2023-12-11 14:00:00", true);

-- Pour testée le trigger CHEVAUCHEMENTACTIVITE
-- INSERT INTO ACTIVITEANNEXE (idActivite, descriptionActivite, dateheureActivite, accessibleAuPublic) VALUES
--     (12, "Rencontre avec la fan-base", "2023-12-01 17:00:00", true);

INSERT INTO PLANIFIER (idGroupe, idActivite, dureePlanification) VALUES
    (1, 1, 3),
    (2, 2, 1),
    (3, 3, 4),
    (4, 5, 2),
    (5, 4, 1);

-- Pour testée le trigger CHEVAUCHEMENTACTIVITE
-- INSERT INTO PLANIFIER (idGroupe, idActivite, dureePlanification) VALUES
--     (1, 12, 3);

INSERT INTO RESEAUX (idReseau, idGroupe, x, instagram, tiktok) VALUES
    (1, 1, "", "https://www.instagram.com/rollingstone/", ""),
    (2, 2, "", "https://www.instagram.com/waterparks/?hl=fr", ""),
    (3, 3, "", "https://www.instagram.com/bringmethehorizon/?hl=fr", ""),
    (4, 4, "", "https://www.instagram.com/spiritboxmusic/?hl=fr", ""),
    (5, 5, "", "https://www.instagram.com/muse/?hl=fr", ""),
    (6, 6, "", "https://www.instagram.com/chilipeppers/", ""),
    (7, 19, "", "https://www.instagram.com/polyphia/", ""),
    (8, 25, "", "https://www.instagram.com/twentyonepilots/", ""),
    (9, 31, "", "https://www.instagram.com/itzy.all.in.us/", ""),
    (10, 32, "", "https://www.instagram.com/blackpink/", ""),
    (11, 33, "", "https://www.instagram.com/xdinaryheroes_official/", ""),
    (12, 37, "", "https://www.instagram.com/bigfloetoli/", ""),
    (13, 38, "", "https://www.instagram.com/maskedwolf/", ""),
    (14, 39, "", "https://www.instagram.com/casseursflowtersinfinity/?hl=fr", ""),
    (15, 43, "", "https://www.instagram.com/dimitrivegasandlikemike/", ""),
    (16, 44, "", "https://www.instagram.com/thechainsmokers/?hl=fr", "");

INSERT INTO INSCRIRE (idConcert, idSpectateur) VALUES
    (3,2),
    (3,1),
    (3,3),
    (3,4),
    (3,5);

-- Pour test le trigger
-- INSERT INTO INSCRIRE (idConcert, idSpectateur) VALUES
--     (3,6);

INSERT INTO TYPEINSTRUMENT (idTypeInstrument, nomTypeInstrument) VALUES
    (1, "Guitare éléctrique"),
    (2, "Piano à queue"),
    (3, "Clavier"),
    (4, "Batterie"),
    (5, "Micro"),
    (6, "Harmonica"),
    (7, "Violon"),
    (8, "Violoncelle"),
    (9, "Guitare basse"),
    (10, "Trompette"),
    (11, "Piano"),
    (12, "Ukulele"),
    (13, "Platine");

INSERT INTO ARTISTE (idArtiste, nomArtiste) VALUES
    (1, "Mick Jagger"),
    (2, "Keith Richards"),
    (3, "Ronnie Wood"),
    (4, "Awsten Knight"),
    (5, "Otto Wood"),
    (6, "Geoff Wigington"),
    (7, "Oliver Sykes"),
    (8, "Matt Kean"),
    (9, "Jordan Fish"),
    (10, "Matt Nicholls"),
    (11, "Courtney LaPlante"),
    (12, "Mike Stinger"),
    (13, "Zev Rosenberg"),
    (14, "Josh Gilbert"),
    (15, "Matthew Bellamy"),
    (16, "Christopher Wolstenholme"),
    (17, "Dominic Howard"),
    (18, "Anthony Kiedis"),
    (19, "Flea"),
    (20, "Chad Smith"),
    (21, "John Frusciante"),
    (22, "Hilary Hahn"),
    (23, "Alexandre Tharaud"),
    (24, "Ray Chen"),
    (25, "Yo-Yo Ma"),
    (26, "Biglo"),
    (27, "Oli"),
    (28, "Masked Wolf"),
    (29, "Tyler Joseph"),
    (30, "Josh Dun"),
    (31, "Dimitri Vegas"),
    (32, "Like Mike"),
    (33, "Andrew Taggart"),
    (34, "Alex Pall"),
    (35, "Tim Henson"),
    (36, "Scott LePage"),
    (37, "Clay Gober"),
    (38, "Clay Aeschliman"),
    (39, "Orelsan"),
    (40, "Gringe"),
    (41, "Hwang Yeji"),
    (42, "Lia"),
    (43, "Ryujin"),
    (44, "Chaeryeong"),
    (45, "Yuna"),
    (46, "Jennie"),
    (47, "Lisa"),
    (48, "Jisoo"),
    (49, "Rose"),
    (50, "Kwak Ji Seok"),
    (51, "Jooyen"),
    (52, "Jun Han"),
    (53, "Gun-il"),
    (54, "Jungsu"),
    (55, "O.de");

INSERT INTO JOUER (idTypeInstrument, idArtiste) VALUES
    (6, 1),
    (5, 1),
    (1, 2),
    (9, 3),
    (1, 4),
    (5, 4),
    (1, 5),
    (4, 6),
    (5, 7),
    (9, 8),
    (3, 9),
    (4, 10),
    (5, 11),
    (1, 12),
    (4, 13),
    (9, 14),
    (5, 15),
    (9, 16),
    (1, 17),
    (5, 18),
    (9, 19),
    (10, 19),
    (11, 19),
    (4, 20),
    (1, 21),
    (7, 22),
    (11, 23),
    (7, 24),
    (8, 25),
    (5, 26),
    (5, 27),
    (5, 28),
    (4, 29),
    (11, 30),
    (5, 30),
    (9, 30),
    (12, 30),
    (13, 31),
    (13, 32),
    (13, 33),
    (13, 34),
    (1, 35),
    (1, 36),
    (9, 37),
    (4, 38),
    (5, 39),
    (5, 40),
    (5, 41),
    (5, 42),
    (5, 43),
    (5, 44),
    (5, 45),
    (5, 46),
    (5, 47),
    (5, 48),
    (5, 49),
    (5, 50),
    (1, 50),
    (5, 51),
    (9, 51),
    (5, 52),
    (1, 52),
    (5, 53),
    (4, 53),
    (5, 54),
    (3, 54),
    (5, 55),
    (13, 55);


INSERT INTO APPARTIENT (idGroupe, idArtiste) VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 11),
    (4, 12),
    (4, 13),
    (4, 14),
    (5, 15),
    (5, 16),
    (5, 17),
    (6, 18),
    (6, 19),
    (6, 20),
    (6, 21),
    (13, 22),
    (13, 23),
    (14, 24),
    (14, 25),
    (37, 26),
    (37, 27),
    (38, 28),
    (25, 29),
    (25, 30),
    (43, 31),
    (43, 32),
    (44, 33),
    (44, 34),
    (19, 35),
    (19, 36),
    (19, 37),
    (19, 38),
    (39, 39),
    (39, 40),
    (31, 41),
    (31, 42),
    (31, 43),
    (31, 44),
    (31, 45),
    (32, 46),
    (32, 47),
    (32, 48),
    (32, 49),
    (33, 50),
    (33, 51),
    (33, 52),
    (33, 53),
    (33, 54),
    (33, 55);

--INSERT INTO PHOTO (idPhoto, idGroupe, filePathPhoto) VALUES;

--INSERT INTO VIDEO (idVideo, idGroupe, filePathVideo) VALUES;
