
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

INSERT INTO GROUPEMUSICAL VALUES
    (1, "The Beatles", 1, "rock"),
    (2, "Led Zeppelin", 2, "rock"),
    (3, "Pink Floyd", 3, "rock"),
    (4, "Queen", 4, "rock"),
    (5, "The Rolling Stones", 5, "rock"),
    (6, "AC/DC", 6, "rock"),
    (7, "Metallica", 7, "rock"),
    (8, "Nirvana", 8, "rock"),
    (9, "Guns N' Roses", 9, "rock"),
    (10, "Red Hot Chili Peppers", 10, "rock");
    
INSERT INTO HEBERGEMENT VALUES
    (1, "Hôtel", 100),
    (2, "Auberge de jeunesse", 50),
    (3, "Camping", 200),
    (4, "Gîte", 50),
    (5, "Chambre d'hôte", 50);

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



