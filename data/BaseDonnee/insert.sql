
INSERT INTO SPECTATEUR VALUES
    (1, "DUPONT", "Jean", "dupont.jean@gmail.com", "1234", "1 rue de la paix", "rien à signaler"),
    (2, "MARTIN", "Lucie", "lucie.martin@gmail.com", "5678", "2 rue de la liberté", "fan de rock"),
    (3, "DURAND", "Pierre", "pierre.durand@gmail.com", "9012", "3 rue de la république", "amateur de jazz"),
    (4, "LEFEVRE", "Sophie", "sophie.lefevre@gmail.com", "3456", "4 rue de la gare", "fan de musique classique"),
    (5, "MOREAU", "Antoine", "antoine.moreau@gmail.com", "7890", "5 rue de la poste", "amateur de blues"),
    (6, "ROUSSEAU", "Marie", "marie.rousseau@gmail.com", "1357", "6 rue de la mairie", "fan de pop"),
    (7, "GIRARD", "Thomas", "thomas.girard@gmail.com", "2468", "7 rue de l'église", "amateur de musique électronique"),
    (8, "BERNARD", "Julie", "julie.bernard@gmail.com", "3690", "8 rue de la plage", "fan de reggae"),
    (9, "PETIT", "Nicolas", "nicolas.petit@gmail.com", "1478", "9 rue de la forêt", "amateur de hip-hop"),
    (10, "ROUX", "Céline", "celine.roux@gmail.com", "2580", "10 rue de la montagne", "fan de métal");

INSERT INTO BILLET VALUES 
    (1, 1, 10, 10, "2020-01-01"),
    (2, 2, 20, 10, "2020-01-02"),
    (3, 3, 30, 10, "2020-01-03"),
    (4, 4, 40, 10, "2020-01-04"),
    (5, 5, 50, 10, "2020-01-05"),
    (6, 7, 60, 10, "2020-01-06"),
    (7, 7, 70, 10, "2020-01-07"),
    (8, 8, 80, 10, "2020-01-08"),
    (9, 9, 90, 10, "2020-01-09");

INSERT INTO STYLE VALUES
    (1, "rock"),
    (2, "jazz"),
    (3, "musique classique"),
    (4, "blues"),
    (5, "pop");

INSERT INTO GROUPEMUSICAL VALUES
    (1, 1, "The Rolling Stones", "Groupe de rock britannique", "https://www.facebook.com/therollingstones/"),
    (2, 1, "Led Zeppelin", "Groupe de rock britannique", "https://www.facebook.com/ledzeppelin/"),
    (3, 2, "Miles Davis", "Trompettiste et compositeur de jazz américain", "https://www.facebook.com/milesdavis/"),
    (4, 3, "Ludwig van Beethoven", "Compositeur allemand de musique classique", "https://www.facebook.com/LudwigvanBeethoven/"),
    (5, 4, "B.B. King", "Guitariste et chanteur de blues américain", "https://www.facebook.com/bbking/"),
    (6, 5, "Michael Jackson", "Chanteur, danseur et compositeur américain de pop", "https://www.facebook.com/michaeljackson/"),
    (7, 1, "The Beatles", "Groupe de rock britannique", "https://www.facebook.com/thebeatles/"),
    (8, 2, "John Coltrane", "Saxophoniste de jazz américain", "https://www.facebook.com/JohnColtrane/"),
    (9, 4, "Stevie Ray Vaughan", "Guitariste et chanteur de blues américain", "https://www.facebook.com/StevieRayVaughan/"),
    (10, 5, "Prince", "Chanteur, musicien et compositeur américain de pop et de funk", "https://www.facebook.com/prince/"),
    (11, 3, "Johann Sebastian Bach", "Compositeur allemand de musique classique", "https://www.facebook.com/JohannSebastianBach/");
    
INSERT INTO LIEU VALUES
    (1, "Salle de concert", 1000, "1 rue de la paix", null),
    (2, "Amphithéâtre", 500, "2 rue de la liberté", null),
    (3, "Salle de conférence", 200, "3 rue de la république", null),
    (4, "Salle de spectacle", 800, "4 rue de la gare", null),
    (5, "Salle de réunion", 50, "5 rue de la poste", null),
    (6, "Salle de danse", 100, "6 rue de la mairie", null),
    (7, "Salle de sport", 2000, "7 rue de l'église", null),
    (8, "Salle de cinéma", 300, "8 rue de la plage", null),
    (9, "Salle de théâtre", 500, "9 rue de la forêt", null),
    (10, "Salle d'exposition", 100, "10 rue de la montagne", null),
    (11, "Salle de fête", 500, "11 rue de la rivière", null);


INSERT INTO CONCERT VALUES
    (1, 1, 1, "Concert des Rolling Stones", "2020-01-01 20:00:00", 120, 60, 60, 1000, false),
    (2, 2, 2, "Concert de Led Zeppelin", "2020-01-02 20:00:00", 150, 100, 50, 500, false),
    (3, 3, 3, "Concert de Miles Davis", "2020-01-03 20:00:00", 90, 30, 60, 200, false),
    (4, 4, 4, "Concert de Beethoven", "2020-01-04 20:00:00", 180, 80, 100, 800, false),
    (5, 5, 5, "Concert de B.B. King", "2020-01-05 20:00:00", 120, 50, 70, 400, false),
    (6, 6, 6, "Concert de Michael Jackson", "2020-01-06 20:00:00", 200, 120, 80, 1000, true),
    (7, 7, 7, "Concert des Rolling Stones", "2020-01-07 20:00:00", 150, 80, 70, 700, true),
    (8, 8, 8, "Concert de John Coltrane", "2020-01-08 20:00:00", 120, 40, 80, 300, true),
    (9, 9, 9, "Concert de Stevie Ray Vaughan", "2020-01-09 20:00:00", 90, 30, 60, 200, true),
    (10, 10, 10, "Concert de Prince", "2020-01-10 20:00:00", 180, 100, 80, 900, true),
    (11, 11, 11, "Concert de Johann Sebastian Bach", "2020-01-11 20:00:00", 120, 60, 60, 500, true);

INSERT INTO FAVORISER VALUES
    (1, 1),
    (2, 3),
    (4, 5),
    (6, 7),
    (8, 9),
    (10, 11),
    (2, 5),
    (4, 7),
    (6, 9),
    (8, 11),
    (10, 3);

INSERT INTO HEBERGEMENT VALUES
    (1, "Hôtel", 100),
    (2, "Auberge de jeunesse", 50),
    (3, "Camping", 200),
    (4, "Gîte", 50),
    (5, "Chambre d'hôte", 50);


INSERT INTO ACCUEILIR VALUES
    (1, 1, "2020-01-01 20:00:00", 5),
    (2, 2, "2020-01-02 20:00:00", 10),
    (3, 3, "2020-01-03 20:00:00", 5),
    (4, 4, "2020-01-04 20:00:00", 10),
    (5, 5, "2020-01-05 20:00:00", 5);


INSERT INTO ACTIVITEANNEXE VALUES
    (1, "Interview radio", "2020-01-01 20:00:00", true),
    (2, "Séance de dédicaces", "2020-01-02 18:00:00", false),
    (3, "Rencontre avec les fans", "2020-01-03 17:00:00", false),
    (4, "Conférence de presse", "2020-01-04 15:00:00", true),
    (5, "Séance de photos", "2020-01-05 16:00:00", false),
    (6, "Rencontre avec les journalistes", "2020-01-06 14:00:00", true),
    (7, "Séance de dédicaces", "2020-01-07 18:00:00", false),
    (8, "Rencontre avec les fans", "2020-01-08 17:00:00", false),
    (9, "Conférence de presse", "2020-01-09 15:00:00", true),
    (10, "Séance de photos", "2020-01-10 16:00:00", false),
    (11, "Rencontre avec les journalistes", "2020-01-11 14:00:00", true);

INSERT INTO PLANIFIER VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);




