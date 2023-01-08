import sqlite3, datetime, random, os


def createbase():
    try:
        table_pelatis = """CREATE TABLE Πελάτης (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Όνομα string,
                            Επώνυμο string,
                            Email string,
                            Κωδικός string,
                            Τηλέφωνο integer
                    );"""

        table_sxolio = """CREATE TABLE Σχόλιο (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Αξιολόγηση float,
                            Περιγραφή string
                    );"""

        table_paragelia = """CREATE TABLE Παραγγελία (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Συνολική_Αξία float,
                            Ημερομηνία datetime
                    );"""

        table_dieu = """CREATE TABLE Διεύθυνση (
                            IDpelatis integer,
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Πόλη string,
                            ΤΚ integer,
                            Οδός string,
                            Όροφος string,
                            Λεπτομέρειες string,
                            FOREIGN KEY (IDpelatis) REFERENCES Πελάτης(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_dianomeas = """CREATE TABLE Διανομέας (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Όνομα string,
                            Επώνυμο string,
                            Τηλέφωνο integer,
                            ΑΦΜ integer
                    );"""

        table_magazi = """CREATE TABLE Μαγαζί (
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Όνομα string,
                            ΑΦΜ integer,
                            Τηλέφωνο integer,
                            Πόλη string,
                            ΤΚ integer,
                            Οδός string,
                            Είδος_Κουζίνας string
                    );"""

        table_proion = """CREATE TABLE Προϊόν (
                            IDmagazi integer,
                            ID integer PRIMARY KEY AUTOINCREMENT,
                            Όνομα string,
                            Τιμή float,
                            Περιγραφή string,
                            Διαθεσιμότητα boolean,
                            FOREIGN KEY (IDmagazi) REFERENCES Μαγαζί(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_sxoliazei = """CREATE TABLE Σχολιάζει (
                            IDpelatis integer,
                            IDsxolio integer,
                            PRIMARY KEY (IDpelatis, IDsxolio),
                            FOREIGN KEY (IDpelatis) REFERENCES Πελάτης(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDsxolio) REFERENCES Σχόλιο(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_stelnei = """CREATE TABLE Στέλνει (
                            IDpelati integer,
                            IDparagelia integer,
                            IDdieu integer,
                            PRIMARY KEY (IDpelati, IDparagelia, IDdieu),
                            FOREIGN KEY (IDpelati) REFERENCES Πελάτης(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDdieu) REFERENCES Διεύθυνση(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_plhrwnei = """CREATE TABLE Πληρώνει (
                            IDpelatis integer,
                            IDparagelia integer,
                            Τρόπος_Πληρωμής string,
                            PRIMARY KEY (IDpelatis, IDparagelia),
                            FOREIGN KEY (IDpelatis) REFERENCES Πελάτης(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_paralambanei = """CREATE TABLE Παραλαμβάνει (
                            IDparagelia integer,
                            IDdianom integer,
                            PRIMARY KEY (IDparagelia, IDdianom),
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDdianom) REFERENCES Διανομέας(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_paradidei = """CREATE TABLE Παραδίδει (
                            IDdieu integer,
                            IDparagelia integer,
                            IDdianom integer,
                            Χρόνος_Παράδοσης integer,
                            PRIMARY KEY (IDdieu, IDparagelia, IDdianom),
                            FOREIGN KEY (IDdieu) REFERENCES Διεύθυνση(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDdianom) REFERENCES Διανομέας(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_sxoliazetai = """CREATE TABLE Σχολιάζεται (
                            IDsxolio integer,
                            IDmagazi integer,
                            PRIMARY KEY (IDsxolio, IDmagazi),
                            FOREIGN KEY (IDsxolio) REFERENCES Σχόλιο(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDmagazi) REFERENCES Μαγαζί(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_dexetai = """CREATE TABLE Δέχεται (
                            IDmagazi integer,
                            IDparagelia integer,
                            PRIMARY KEY (IDmagazi, IDparagelia),
                            FOREIGN KEY (IDmagazi) REFERENCES Μαγαζί(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        table_periexei = """CREATE TABLE Περιέχει (
                            IDproion integer,
                            IDparagelia integer,
                            Ποσότητα integer,
                            PRIMARY KEY (IDproion, IDparagelia),
                            FOREIGN KEY (IDproion) REFERENCES Προϊόν(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (IDparagelia) REFERENCES Παραγγελία(ID)
                            ON DELETE CASCADE ON UPDATE CASCADE
                    );"""

        conn.execute(table_pelatis)
        conn.execute(table_sxolio)
        conn.execute(table_paragelia)
        conn.execute(table_dieu)
        conn.execute(table_dianomeas)
        conn.execute(table_magazi)
        conn.execute(table_proion)
        conn.execute(table_sxoliazei)
        conn.execute(table_stelnei)
        conn.execute(table_plhrwnei)
        conn.execute(table_paralambanei)
        conn.execute(table_paradidei)
        conn.execute(table_sxoliazetai)
        conn.execute(table_dexetai)
        conn.execute(table_periexei)
        conn.commit
        
        loaddata()
        i = 0
        while i!=50:
            generate_random_order()
            i = i+1
    except:
        return

def loaddata():
    
    data_pelates = """INSERT INTO `Πελάτης` (`Όνομα`,`Επώνυμο`,`Email`,`Κωδικός`,`Τηλέφωνο`)
                        VALUES
                          ("Griffin","Frederick","fringilla.euismod@hotmail.org","GXY87RLN4UQ","2107229352"),
                          ("Ora","Hewitt","sed.diam.lorem@protonmail.net","FPT41ZPV3WC","2610886937"),
                          ("Orlando","Dotson","enim.mi@protonmail.ca","XTE45JMU6KJ","2610215458"),
                          ("Hop","Hendrix","turpis@outlook.ca","SDU49IAD8OU","2105612667"),
                          ("Victoria","Green","rutrum.lorem@google.net","CKK99SKT2BF","2106541399"),
                          ("Olga","Carney","nunc@hotmail.com","URI70TOY6BZ","2104633584"),
                          ("Alexander","Kelley","magna.a.tortor@aol.org","TSA84EIN0JE","2610523886"),
                          ("Aurora","Chapman","hendrerit.consectetuer@hotmail.com","CDD34HCL2WR","2610040726"),
                          ("Harper","Preston","pede@protonmail.org","QRP55CRG8YQ","2103127462"),
                          ("Haley","Vincent","purus.nullam.scelerisque@google.net","VAC31YUN3KI","2101617746"),
                          ("Giacomo","David","dui.cras@icloud.ca","CEV10XUM1BG","2610019358"),
                          ("Tamara","Callahan","pellentesque.ut.ipsum@outlook.com","RZT25HXS6YX","2102533785"),
                          ("Briar","Saunders","elit.dictum@icloud.com","GVN29UJP3XS","2610264712"),
                          ("Luke","Burks","fusce.aliquet@outlook.net","RSG26WXC6KW","2610833910"),
                          ("Tarik","Wilkins","cursus.integer@aol.couk","MCS44OVQ0AD","2107222175"),
                          ("Lilah","Pate","massa@aol.ca","GTA16QHE5EM","2610987653"),
                          ("Calista","Gallagher","sit.amet.ultricies@icloud.com","PMY49BOC1JM","2103171876"),
                          ("Chandler","Golden","non.vestibulum@icloud.ca","QIR55AJN8QH","2101366363"),
                          ("Austin","Emerson","placerat.orci@icloud.net","GJC68MDO8OH","2610777193"),
                          ("Karina","Kennedy","donec@outlook.ca","NPG78LJB5ET","2610741843"),
                          ("Nayda","Holcomb","bibendum@hotmail.org","KJY87LFD7LN","2101298982"),
                          ("Olympia","Adkins","tempor@outlook.edu","VVP95KIT9FI","2610654173"),
                          ("Shaeleigh","Mercer","lorem.ac@outlook.edu","BDJ76UGG7TP","2107238576"),
                          ("Dolan","Spence","egestas.urna@icloud.org","QCI30TNR5RS","2610321368"),
                          ("Allistair","Brock","velit.eu@google.net","WPF27KIE8BL","2610837443"),
                          ("Ulysses","Downs","magna.cras.convallis@yahoo.couk","HCM35MYY0NY","2107221071"),
                          ("Guinevere","Ford","mi.pede@icloud.couk","CQG02HMM3OR","2610445414"),
                          ("Steven","Holcomb","malesuada@protonmail.ca","VEU62ROH8RH","2109832832"),
                          ("Orla","Slater","vestibulum.neque.sed@google.com","AYL11HHU4FD","2108955683"),
                          ("Irene","Holder","penatibus.et@outlook.ca","CCT86NIN1JK","2610628225"),
                          ("Omar","Goff","duis.dignissim.tempor@yahoo.com","HFQ78IKG6UK","2106664886"),
                          ("Madaline","Valencia","facilisi.sed.neque@google.net","DUV62FFL7WS","2610772948"),
                          ("Addison","Bender","morbi.accumsan@yahoo.com","ZQW71CXT4WI","2102293925"),
                          ("Mollie","Parrish","cum.sociis@yahoo.edu","LBG16KIR3SW","2610762046"),
                          ("Imelda","Boyle","tristique@yahoo.edu","OML17ILC4IG","2103660746"),
                          ("Ebony","Rhodes","et.rutrum.eu@aol.couk","MQL95EUH3JM","2610789880"),
                          ("Mira","Rodgers","nascetur.ridiculus.mus@hotmail.net","RWP79AEH3HY","2102165744"),
                          ("Jasper","Randall","penatibus.et.magnis@hotmail.couk","DHR45HSP8BW","2610170445"),
                          ("Olivia","Salazar","sollicitudin@yahoo.com","WFI88SIB8KN","2610760217"),
                          ("Austin","Roy","est@aol.ca","TBG16RYS0MR","2108729558"),
                          ("Nicole","Barrett","aliquam.adipiscing.lacus@google.edu","BYG32UGV8SV","2610791327"),
                          ("Lawrence","Frank","mollis.duis.sit@yahoo.net","PVY63UWO2FN","2102348345"),
                          ("Odessa","Le","elit.etiam@protonmail.ca","JSA01VEQ5XJ","2610869642"),
                          ("Finn","Strickland","neque.sed@google.ca","UMU67CSU8FX","2610588167"),
                          ("Harrison","Keith","lorem.vehicula@icloud.ca","CMK48OJO1QO","2104188630"),
                          ("Sonya","Wade","ligula.aliquam@yahoo.org","ITX57CTC3VN","2107531834"),
                          ("Jada","Vasquez","nulla.tempor@hotmail.net","TSW25QGM6CT","2108233461"),
                          ("Yvonne","Hester","scelerisque.neque@hotmail.net","QJQ04UYP3UY","2610415296"),
                          ("Dominic","Rowe","egestas@icloud.org","MMQ75RBK3PS","2610258687"),
                          ("Piper","Marshall","hendrerit.consectetuer.cursus@protonmail.ca","BPH45YGJ8SN","2102627171");
                        """
    data_dieu = """INSERT INTO `Διεύθυνση` (`IDpelatis`,`Πόλη`,`ΤΚ`,`Οδός`,`Όροφος`,`Λεπτομέρειες`)
                    VALUES
                      (29,"Αθήνα","5352","694-1429 Maecenas Rd.",2,"Δεν έχει κουδούνι"),
                      (5,"Αθήνα","828767","3700 Lacus Avenue",1,""),
                      (24,"Αθήνα","441242","Ap #514-8943 Curabitur Rd.",2,""),
                      (7,"Πάτρα","32322","601-6820 Enim Av.",2,""),
                      (9,"Πάτρα","2467","Ap #925-5706 Sit Street",2,"Δεν έχει κουδούνι"),
                      (27,"Αθήνα","684014","P.O. Box 750, 9383 Mauris St.",4,""),
                      (24,"Αθήνα","6147 CI","2928 Vulputate Ave",3,""),
                      (41,"Πάτρα","22675","363-8683 Lectus Street",1,""),
                      (4,"Αθήνα","J1T 3WR","736-7966 Senectus Road",2,""),
                      (8,"Πάτρα","20304","Ap #265-1783 Lectus. Ave",3,""),
                      (17,"Πάτρα","675667","Ap #361-6327 Nullam Street",3,""),
                      (3,"Πάτρα","37773","513-7861 Mi Rd.",3,""),
                      (40,"Πάτρα","545048","8031 Non, Road",1,""),
                      (29,"Αθήνα","257728","Ap #916-5267 Id St.",1,""),
                      (44,"Αθήνα","7671","Ap #678-9117 Venenatis St.",4,""),
                      (36,"Αθήνα","3053","9792 Mauris Av.",0,""),
                      (38,"Αθήνα","58754-435","Ap #825-2197 Odio Rd.",3,""),
                      (23,"Αθήνα","32M 2K8","Ap #279-7281 Fusce Avenue",4,""),
                      (27,"Αθήνα","711268","Ap #440-7370 Ut St.",3,""),
                      (20,"Πάτρα","8628","Ap #512-8576 Lorem. Rd.",3,""),
                      (6,"Πάτρα","2572","647-6935 Vestibulum St.",2,""),
                      (14,"Πάτρα","28777","Ap #299-8351 Non Street",2,""),
                      (26,"Αθήνα","24431","P.O. Box 835, 6297 Pede. St.",3,""),
                      (50,"Πάτρα","12174","468-9729 Semper Ave",2,""),
                      (45,"Πάτρα","15V 7W6","Ap #598-5572 Et Road",1,"Δεν έχει κουδούνι"),
                      (7,"Πάτρα","19254","Ap #824-3755 Semper Ave",2,""),
                      (20,"Πάτρα","1628","5316 Nisl. Avenue",2,""),
                      (16,"Πάτρα","95-428","Ap #785-5754 Ipsum Ave",0,""),
                      (41,"Πάτρα","3739","494-3009 Sollicitudin Ave",4,""),
                      (24,"Πάτρα","255152","P.O. Box 936, 8950 Vivamus Ave",3,""),
                      (16,"Αθήνα","R3W 0S8","Ap #841-200 Porttitor Rd.",2,""),
                      (11,"Πάτρα","59476","Ap #545-1218 Ac Street",1,"Το πάνω πάνω"),
                      (37,"Πάτρα","45474","P.O. Box 218, 8078 Porttitor St.",2,""),
                      (8,"Αθήνα","41506","P.O. Box 365, 8550 Non Road",1,""),
                      (15,"Αθήνα","4936","4446 Orci, Av.",2,""),
                      (11,"Πάτρα","773775","Ap #912-1161 Primis Ave",2,""),
                      (35,"Πάτρα","73-23","5853 Parturient Avenue",3,""),
                      (19,"Αθήνα","309152","Ap #646-8960 Ligula Rd.",3,""),
                      (13,"Αθήνα","1241","Ap #243-2179 Dui, Rd.",1,""),
                      (25,"Αθήνα","V6I 3PO","448-6778 Aliquam Rd.",1,""),
                      (19,"Πάτρα","5154-1358","Ap #873-1213 Imperdiet St.",2,""),
                      (3,"Πάτρα","8740-7917","P.O. Box 845, 5247 Risus. Avenue",4,""),
                      (49,"Αθήνα","33S 4Y8","Ap #542-2628 Mattis St.",2,""),
                      (43,"Αθήνα","22527-636","Ap #484-736 Sed Road",2,""),
                      (46,"Αθήνα","13085","Ap #482-8674 Magna. St.",2,"Χτυπήστε Κόρνα"),
                      (4,"Πάτρα","412589","8724 Vel Road",0,""),
                      (50,"Πάτρα","40411","Ap #384-6393 At, Rd.",2,""),
                      (7,"Πάτρα","585437","Ap #879-1421 Quam, Av.",2,""),
                      (20,"Πάτρα","45-201","Ap #615-7213 Morbi Rd.",1,""),
                      (33,"Πάτρα","581265","566-9820 Tristique Street",2,"Χτυπήστε Κόρνα"),
                      (33,"Αθήνα","31614","7256 Vel, St.",4,""),
                      (39,"Πάτρα","64633","Ap #866-6037 Lobortis Avenue",2,""),
                      (6,"Αθήνα","N2R 5X3","1456 Neque Road",4,""),
                      (3,"Αθήνα","51J 3W5","P.O. Box 870, 2811 Nec Rd.",1,""),
                      (21,"Αθήνα","339361","5281 Donec Ave",0,"");
                    """

    data_magazia = """INSERT INTO `Μαγαζί` (`Όνομα`,`ΑΦΜ`,`Τηλέφωνο`,`Πόλη`,`ΤΚ`,`Οδός`,`Είδος_Κουζίνας`)
                        VALUES
                          ("El Greco","299848858","2104134628","Αθήνα","9923","Ap #690-2968 Donec Rd.","Ιταλική"),
                          ("Frankys","532818713","2610777258","Αθήνα","187152","Ap #110-6993 Aliquam St.","Ιταλική"),
                          ("Asia Food","250853540","2610218812","Πάτρα","603963","P.O. Box 832, 6028 Scelerisque Av.","Κινέζικο"),
                          ("Η Γωνιά Του Μπάμπη","442896134","2610733718","Πάτρα","622687","P.O. Box 469, 3766 Ipsum. Rd.","Ψητά"),
                          ("Ψητόπολις","685816388","2610645335","Αθήνα","53728","4319 Et Rd.","Σουβλάκια"),
                          ("Πίτσα στον Ξυλόφουρνο","515442821","2610123745","Αθήνα","624582","P.O. Box 190, 278 Amet Street","Πίτσες"),
                          ("Πίτσα Παραδοσιακή","123757455","2100761377","Πάτρα","2617 CV","Ap #125-9585 Leo Ave","Πίτσες"),
                          ("Πίτσες Μπλε","225901459","2610024785","Πάτρα","6883-2688","123-5385 Sollicitudin Rd.","Πίτσες"),
                          ("Αχαικό Χωριάτικο","604522279","2610570051","Αθήνα","50718","4334 Malesuada Street","Καφές"),
                          ("Domino's Pizza","882327526","2610463011","Αθήνα","3462-2760","Ap #387-2751 Ut Ave","Πίτσες"),
                          ("Aya Sushi Bar","737443737","2610457684","Πάτρα","1252-2547","411-9590 Eu Road","Sushi"),
                          ("Black Sheep Coffee","741185573","2105717288","Πάτρα","19166","Ap #916-8999 Maecenas Rd.","Καφές"),
                          ("Volcano","712512515","2610052737","Αθήνα","1277-1686","Ap #392-1185 Laoreet St.","Σουβλάκια"),
                          ("East Food","693786164","2610521861","Αθήνα","824028","291-684 Tempus Ave","Sushi"),
                          ("Danielle Tratoria","624214282","2103735796","Πάτρα","09410","Ap #127-8196 Ut Road","Ιταλική"),
                          ("Χοιροποίητο","643154070","2107215327","Πάτρα","443016","497-5211 Pede. Av.","Σουβλάκια"),
                          ("Στάβλος","267753478","2104323319","Αθήνα","23875-96993","440-9868 Et, Avenue","Σουβλάκια"),
                          ("Pizza Fan","935214238","2610231493","Αθήνα","33824632","799-4401 Ipsum. Street","Πίτσες"),
                          ("Constantino","878564867","2610313596","Πάτρα","533352","Ap #783-5959 Ut Rd.","Κρέπες"),
                          ("Factory Flavors","485397356","2610855270","Πάτρα","775850","Ap #669-4009 Sed Ave","Κρέπες"),
                          ("Ο Μπαρμπαγιάννης","425121613","2102509587","Αθήνα","7187","589-2942 Mus. Road","Σουβλάκια"),
                          ("Segnore","767576384","2610567892","Αθήνα","5418","Ap #228-3200 Pede. Rd.","Ιταλική"),
                          ("Ali Baba","437311197","2610154567","Πάτρα","8670-5657","Ap #180-3083 Magna St.","Ινδικό"),
                          ("Ο Χρυσός Δράκος","721269484","2108749834","Πάτρα","67407-372","6318 Sem, Ave","Κινέζικο"),
                          ("Μεσημεριανά Μαγειρέματα","171597161","2610543125","Αθήνα","171912","P.O. Box 550, 8994 Dui Rd.","Μαγειρευτά");
                        """

    data_proionta = """INSERT INTO `Προϊόν` (`IDmagazi`,`Τιμή`,`Περιγραφή`,`Διαθεσιμότητα`,`Όνομα`)
                        VALUES
                          (13,"8.58","","Yes","Σκεπαστή Κοτόπουλο"),
                          (12,"4.70","","Yes","Cappuchino"),
                          (8,"8.30","","No","Πίτσα Παραδοσιακή"),
                          (2,"9.88","","No","Καρμπονάρα"),
                          (8,"10.39","","Yes","Πίτσα Αλλαντικών"),
                          (10,"8.72","","Yes","Πίτσα Σπέσιαλ"),
                          (7,"8.14","","Yes","Πίτσα Παραδοσιακή"),
                          (21,"7.57","","Yes","Πίτα Κλαμπ Κοτόπουλο"),
                          (4,"9.17","","No","Μερίδα Γύρο Χοιρινό"),
                          (11,"8.33","","No","California Rolls"),
                          (17,"10.88","","Yes","Μερίδα Γύρος Χοιρινό"),
                          (16,"8.61","","Yes","2+1 Πίτες"),
                          (3,"9.56","","No","Noodles με καρύδα"),
                          (3,"5.61","","No","Noodles με γλυκόξινη"),
                          (4,"4.18","","No","Πίτα Κλαμπ Κοτόπουλο"),
                          (22,"8.31","","Yes","Πίτσα Προσούτο"),
                          (4,"12.27","","Yes","Μπριζόλα Χοιρινή"),
                          (20,"4.80","","Yes","Κρέπα Nuggets Bacon"),
                          (22,"0.36","","No","Νερό"),
                          (20,"5.67","","Yes","Κρέπα Γιαννίωτικη"),
                          (21,"7.79","","No","Πίτα Κλαμπ Χοιρινό"),
                          (22,"14.47","","No","Πιατέλα Αλλαντικών"),
                          (5,"5.59","","Yes","Μερίδα Γύρο Κοτόπουλο"),
                          (18,"8.92","","Yes","Πίτσα Αλλαντικών"),
                          (3,"4.32","","No","Τηγανιτό Ρύζι"),
                          (23,"3.98","","Yes","Tikka Massala"),
                          (15,"6.73","","Yes","Καρμπονάρα"),
                          (20,"5.21","","No","Κρέπα Σοκολάτα Μπισκότο"),
                          (8,"6.70","","Yes","Πίτσα Πεπερόνι"),
                          (17,"6.85","","No","Μερίδα Γύρος Χοιρινό"),
                          (9,"8.25","","Yes","3+1 Καφέδες"),
                          (22,"2.40","","Yes","Coca Cola"),
                          (14,"7.86","","No","California Rolls"),
                          (8,"5.73","","Yes","Πίτσα Μαργαρίτα"),
                          (2,"8.38","","No","Μπολονέζ"),
                          (16,"8.12","","No","Πίτα Κλαμπ Μιξ"),
                          (20,"9.19","","Yes","Κρέπα Deluxe Γλυκιά"),
                          (14,"2.00","","No","Coca Cola"),
                          (6,"4.99","","Yes","Πίτσα Ζαμπόν"),
                          (3,"10.36","","No","Spring Rolls"),
                          (23,"6.55","","No","Tadouri"),
                          (19,"4.78","","Yes","Κρέπα Γιαννιώτικη"),
                          (19,"5.91","","Yes","Κρέπα Hungry"),
                          (4,"4.99","","Yes","Κοντοσούβλι"),
                          (18,"7.71","","No","Φτερούγες Κοτόπουλο"),
                          (13,"6.15","","No","1+1 Πίτα Γύρο Χοιρινό"),
                          (13,"5.93","","No","1+1 Πίτα Γύρο Κοτόπουλο"),
                          (9,"10.47","","No","Pancakes με Merenda"),
                          (8,"10.71","","No","Πίτσα Σκεπαστή"),
                          (25,"4.76","","Yes","Παστίτσιο"),
                          (1,"3.15","","Yes","Καρμπονάρα"),
                          (2,"7.83","","No","Καρπάτσιο"),
                          (20,"9.49","","No","Κρέπα Deluxe Αλμυρή"),
                          (24,"12.22","","No","Mix Sushi Combo"),
                          (22,"8.40","","Yes","Πίτσα 4 Εποχές"),
                          (23,"6.79","","No","Κοτόπουλο Με Κάρυ"),
                          (9,"2.24","","Yes","Φρέντο Εσπρέσσο"),
                          (15,"12.10","","No","Πίτσα Προσούτο"),
                          (23,"4.67","","No","Ρύζι Με Κάρυ"),
                          (13,"6.67","","No","Σαλάτα Ceasars"),
                          (23,"7.91","","No","Μιξ Σπεσιαλ"),
                          (21,"6.36","","No","Μερίδα Γύρος Κοτόπουλο"),
                          (16,"6.72","","No","Μερίδα Γύρος Κοτόπουλο"),
                          (11,"8.34","","No","Inside Out"),
                          (18,"6.76","","Yes","Πίτσα Μαργαρίτα"),
                          (7,"8.45","","No","Πίτσα Σπέσιαλ"),
                          (12,"5.31","","Yes","Latte Machiato"),
                          (16,"5.57","","No","Μερίδα Γύρος Χοιρινό"),
                          (21,"6.28","","Yes","Μερίδα Γύρος Χοιρινό"),
                          (14,"6.04","","Yes","Inside Out"),
                          (18,"9.99","","Yes","Πίτσα Γίγας Μαργαρίτα"),
                          (5,"7.52","","Yes","Πίτα Κλαμπ Χοιρινό"),
                          (19,"5.15","","Yes","Κρέπα Nuggets Bacon"),
                          (12,"4.35","","Yes","Φρέντο Εσπρέσσο"),
                          (21,"7.85","","No","Πίτα Κλαμπ Μιξ");
                        """

    data_sxolia = """INSERT INTO `Σχόλιο` (`Αξιολόγηση`,`Περιγραφή`)
                    VALUES
                      (3,""),
                      (4,"Πολύ Νόστιμο"),
                      (2,"Καμένο"),
                      (2,""),
                      (3,""),
                      (3,""),
                      (2,"Το φαγητό ήταν κρύο"),
                      (2,""),
                      (5,"Τέλειο"),
                      (3,""),
                      (3,""),
                      (3,""),
                      (4,""),
                      (2,"Λάθος Παραγγελία"),
                      (2,""),
                      (3,"Μέτριο"),
                      (3,""),
                      (2,""),
                      (2,""),
                      (5,""),
                      (2,"Λάθος Παραγγελία"),
                      (2,""),
                      (3,""),
                      (4,"Πολύ Καλό"),
                      (2,"Άργησε Πολύ!")
                      """

    data_sxoliazetai = """INSERT INTO `Σχολιάζεται` (`IDsxolio`,`IDmagazi`)
                        VALUES
                          (1,21),
                          (2,16),
                          (3,23),
                          (4,10),
                          (5,8),
                          (6,6),
                          (7,21),
                          (8,23),
                          (9,24),
                          (10,25),
                          (11,12),
                          (12,10),
                          (13,12),
                          (14,9),
                          (15,4),
                          (16,6),
                          (17,3),
                          (18,15),
                          (19,23),
                          (20,8),
                          (21,3),
                          (22,6),
                          (23,3),
                          (24,18),
                          (25,16);
                        """

    data_sxoliazei = """INSERT INTO `Σχολιάζει` (`IDsxolio`,`IDpelatis`)
                        VALUES
                          (1,38),
                          (2,13),
                          (3,5),
                          (4,42),
                          (5,47),
                          (6,21),
                          (7,11),
                          (8,40),
                          (9,16),
                          (10,38),
                          (11,13),
                          (12,38),
                          (13,47),
                          (14,26),
                          (15,42),
                          (16,32),
                          (17,18),
                          (18,39),
                          (19,33),
                          (20,43),
                          (21,9),
                          (22,33),
                          (23,6),
                          (24,41),
                          (25,24);
                        """

    data_dianomeis = """INSERT INTO `Διανομέας` (`Όνομα`,`Επώνυμο`,`Τηλέφωνο`,`ΑΦΜ`)
                        VALUES
                          ("Blaze","Norris","6945213787","020214877"),
                          ("Calista","Fuller","6926422188","214044920"),
                          ("Chloe","Stone","6935288486","480516143"),
                          ("Jolie","Mullins","6953421677","677647133"),
                          ("Carly","Frederick","6904685826","226745257"),
                          ("Malcolm","Bailey","6920969239","335089778"),
                          ("Lysandra","Garrison","6929645762","824764466"),
                          ("Chastity","Blair","6931845388","537559415"),
                          ("Fitzgerald","Hobbs","6901761423","025778655"),
                          ("Fritz","Hutchinson","6947096228","637621638"),
                          ("Freya","Perez","6973838446","653714987"),
                          ("Quemby","Salazar","6934702238","746416732"),
                          ("Edward","Miles","6982582711","765661275"),
                          ("Brian","Talley","6918227808","692432542"),
                          ("Mallory","Mccarty","6964788978","445277838"),
                          ("Ralph","Flowers","6961153241","132241914"),
                          ("Patrick","Humphrey","6944856482","784308311"),
                          ("Zeph","Brown","6937642299","358776610"),
                          ("Alisa","Harvey","6915726275","314176875"),
                          ("Olympia","Medina","6994536002","057631531");
                        """

    conn.execute(data_pelates)
    conn.execute(data_dieu)
    conn.execute(data_magazia)
    conn.execute(data_proionta)
    conn.execute(data_sxolia)
    conn.execute(data_sxoliazetai)
    conn.execute(data_sxoliazei)
    conn.execute(data_dianomeis)
    conn.commit()

def paragelia():
    c = conn.cursor()
    #1: Επιλογή Πελάτη
    try:
        first_name = str(input("\nΕισάγετε το όνομα του Πελάτη: "))
        last_name = str(input("\nΕισάγετε το επώνυμο του Πελάτη: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        IDpel = int(data[0][0])
    except:
        print("\nΔεν υπάρχει ο χρήστης")
        return


    #2: Επιλογή Διεύθυνσης
    c.execute("SELECT ID, Οδός FROM Διεύθυνση WHERE IDpelatis == (?)", (IDpel,))
    data = c.fetchall()
    if data == []:
        print("\nΟ Πελάτης αυτός δεν έχει διευθύνσεις στον λογαριασμό του. Παρακαλώ προσθέστε μια πρωτού κάνετε παραγγελία.\n")
        return
    
    print("\nΟ πελάτης αυτός έχει τις εξείς διευθύνσεις: \n")
    style = "{:<2} {:<20}"
    i=1
    for t in data:
        print(style.format(i,t[1]))
        i=i+1
    try:
        address = int(input("\nΣε ποια από τις διευθύνσεις θα θέλατε να πάει(Επιλέξτε τον αριθμό από την λίστα): "))
        IDdieu = data[address-1][0]                
    except:
        print("Ο αριθμός που επιλέξατε είναι εκτός λίστας")
        return
    
    #2.5: Επιλογή τρόπου πληρωμής
    tropos_plir = str(input("\nΠως θα πληρώσετε (Κάρτα/Paypal/Μετρητά)? "))
    
    
    #3: Επιλογή Μαγαζιού
    try:
        store = str(input("\nΕισάγετε το όνομα του Μαγαζιού: "))
        c.execute("SELECT ID FROM Μαγαζί WHERE Όνομα == (?)", (store,))
        data = c.fetchall()
        IDmagazi = data[0][0]
    except:
        print("\nΔεν υπάρχει το μαγαζί")
        return


    #4: Επιλογή Προιόντος
    print("Το μαγαζί αυτό έχει τα εξής προϊόντα: \n")
    c.execute("SELECT Όνομα, Τιμή FROM Προϊόν WHERE IDmagazi == (?)", (IDmagazi,))
    data = c.fetchall()
    style = "{:<20} {:<5}"
    for t in data:
        print(style.format(t[0],t[1]))
    i = 0
    itemlist = []
    while(True):
        try:
            item = str(input("\nΕισάγετε το όνομα του Προιόντος: "))
            c.execute("SELECT ID, Διαθεσιμότητα, Τιμή FROM Προϊόν WHERE IDmagazi == (?) AND Όνομα == (?)", (IDmagazi, item))
            data = c.fetchall()
            IDproion = data[0][0]
            itemprice = data[0][2]
            
            if data[0][1] == "No":
                print("\nΑυτό το Προιον δεν είναι διαθέσιμο. ")
            else:   
                itemlist.append(IDproion) #Θέση 0+i*3
                itemlist.append(itemprice) #Θέση 1+i*3
                #Επιλογή Ποσότητας
                itemlist.append(int(input("\nΠόσα τεμάχια θα θέλατε για αυτό το προιόν: "))) #Θέση 2+i*3

            more = str(input("\nΘα θέλατε κάτι άλλο(Y/N): "))
            if more == "N":
                break
            
        except:
            print("\nΔεν υπάρχει το προιόν στο συγκεκριμένο μαγαζί")
    totalvalue = 0
    for j in range(int(len(itemlist)/3)):
         totalvalue = totalvalue + itemlist[1+j*3]*itemlist[2+j*3]
        
    
    #5: Προσθήκη Μιας παραγγελίας με Ημερομηνία
    conn.execute("INSERT INTO Παραγγελία ('Συνολική_Αξία', 'Ημερομηνία') VALUES (?,?)",(float(totalvalue), datetime.datetime.now().strftime("%x")))
    conn.commit()
    
    c.execute("SELECT ID FROM Παραγγελία WHERE Συνολική_Αξία == (?) AND Ημερομηνία == (?) ORDER BY ID DESC",(float(totalvalue), datetime.datetime.now().strftime("%x")))
    data = c.fetchall()
    IDparagelia = data[0][0]
    
    #6: Προσθήκη Διανομέα
    IDdianom = random.randint(1,20)


    #7: Προσθήκη όλων των σχέσεων
    conn.execute("INSERT INTO Στέλνει ('IDpelati','IDparagelia','IDdieu') VALUES (?,?,?)",(IDpel, IDparagelia, IDdieu)) #Στέλνει
    conn.execute("INSERT INTO Πληρώνει ('IDpelatis','IDparagelia','Τρόπος_Πληρωμής') VALUES (?,?,?)",(IDpel, IDparagelia, tropos_plir)) #Πληρώνει
    conn.execute("INSERT INTO Δέχεται ('IDmagazi','IDparagelia') VALUES (?,?)",(IDmagazi, IDparagelia)) #Δέχεται
    conn.execute("INSERT INTO Παραλαμβάνει ('IDparagelia','IDdianom') VALUES (?,?)",(IDparagelia, IDdianom)) #Παραλαμβάνει
    conn.execute("INSERT INTO Παραδίδει ('IDdieu','IDparagelia','IDdianom', 'Χρόνος_Παράδοσης') VALUES (?,?,?,?)",(IDdieu, IDparagelia, IDdianom, random.randint(20,50))) #Παραδίδει

    for j in range(int(len(itemlist)/3)):
        conn.execute("INSERT INTO Περιέχει ('IDproion','IDparagelia','Ποσότητα') VALUES (?,?,?)",(itemlist[0+j*3], IDparagelia, itemlist[2+j*3])) #Περιέχει

    print("\nΗ παραγγελία ολοκληρώθηκε\n")
    conn.commit()


def generate_random_order():
    c = conn.cursor()
    IDpelati = random.randint(1,50)

    c.execute("SELECT ID FROM Διεύθυνση WHERE IDpelatis == (?)", (IDpelati,))
    data = c.fetchall()
    if data == []:
        return
    else:
        dieunum = random.randint(0,int(len(data)-1))
        IDdieu = data[dieunum][0]
        
    plir = ["Μετρητά","Κάρτα","Paypal"]
    tropos_plir = plir[random.randint(0,2)]
    
    IDmagazi = random.randint(1,25)

    c.execute("SELECT ID FROM Προϊόν WHERE IDmagazi == (?)", (IDmagazi,))
    data = c.fetchall()
    if data == []:
        return
    else:
        IDproion = data[random.randint(0,int(len(data)-1))][0]
        c.execute("SELECT Διαθεσιμότητα, Τιμή FROM Προϊόν WHERE ID == (?)", (IDproion,))
        data = c.fetchall()
        if data[0][0] == "NO":
            return
        posotita = random.randint(1,5)
        totalvalue = data[0][1]*posotita

    IDdianom = random.randint(1,20)

    date = datetime.datetime(random.randint(2020,2022), random.randint(1,12), random.randint(1,28))

    conn.execute("INSERT INTO Παραγγελία ('Συνολική_Αξία', 'Ημερομηνία') VALUES (?,?)",(float(totalvalue), date.strftime("%x")))
    conn.commit()
    c.execute("SELECT ID FROM Παραγγελία WHERE Συνολική_Αξία == (?) AND Ημερομηνία == (?) ORDER BY ID DESC",(float(totalvalue), date.strftime("%x")))
    data = c.fetchall()
    IDparagelia = data[0][0]
    
    conn.execute("INSERT INTO Στέλνει ('IDpelati','IDparagelia','IDdieu') VALUES (?,?,?)",(IDpelati, IDparagelia, IDdieu)) #Στέλνει
    conn.execute("INSERT INTO Πληρώνει ('IDpelatis','IDparagelia','Τρόπος_Πληρωμής') VALUES (?,?,?)",(IDpelati, IDparagelia, tropos_plir)) #Πληρώνει
    conn.execute("INSERT INTO Δέχεται ('IDmagazi','IDparagelia') VALUES (?,?)",(IDmagazi, IDparagelia)) #Δέχεται
    conn.execute("INSERT INTO Παραλαμβάνει ('IDparagelia','IDdianom') VALUES (?,?)",(IDparagelia, IDdianom)) #Παραλαμβάνει
    conn.execute("INSERT INTO Παραδίδει ('IDdieu','IDparagelia','IDdianom', 'Χρόνος_Παράδοσης') VALUES (?,?,?,?)",(IDdieu, IDparagelia, IDdianom, random.randint(20,50))) #Παραδίδει
    conn.execute("INSERT INTO Περιέχει ('IDproion','IDparagelia','Ποσότητα') VALUES (?,?,?)", (IDproion, IDparagelia, posotita))
    conn.commit()
    
    

def insert():
    c = conn.cursor()
    choice=int(input("Διαλέξτε Input:\n 1 Πελάτης\n 2 Διεύθυνση\n 3 Μαγαζί\n 4 Σχόλιο\n 5 Προϊόν\n 6 Διανoμέας\n 7 Επιστροφη\n"));
    
    if int(choice) == 1: #Πελάτης
        values=[1,2,3,4,5]
        values[0]=input("\nΕισάγετε Όνομα: ");
        values[1]=input("\nΕισάγετε Επώνυμο: ");
        values[2]=input("\nΕισάγετε Email: ");
        values[3]=input("\nΕισάγετε Κωδικό: ");
        values[4]=input("\nΕισάγετε Τηλέφωνο: ");
        conn.execute('INSERT INTO Πελάτης (`Όνομα`,`Επώνυμο`,`Email`,`Κωδικός`,`Τηλέφωνο`) VALUES (?,?,?,?,?);',(str(values[0]),str(values[1]),str(values[2]),str(values[3]),int(values[4])));
        conn.commit()

    elif int(choice) == 2: #Διεύθυνση
        values=[1,2,3,4,5,6]
        first_name = str(input("\nΕισάγετε το όνομα του Πελάτη που βρίσκεται στην Διεύθυνση: "))
        last_name = str(input("\nΕισάγετε το επώνυμο του Πελάτη που βρίσκεται στην Διεύθυνση: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        IDpel = int(data[0][0])
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return
        values[0]=IDpel;
        values[1]=input("\nΕισάγετε Πόλη: ");
        values[2]=input("\nΕισάγετε ΤΚ: ");
        values[3]=input("\nΕισάγετε Οδό: ");
        values[4]=input("\nΕισάγετε Όροφο: ");
        values[5]=input("\nΕισάγετε Λεπτομέρειες: ");
        conn.execute('INSERT INTO Διεύθυνση (`IDpelatis`,`Πόλη`,`ΤΚ`,`Οδός`,`Όροφος`,`Λεπτομέρειες`) VALUES (?,?,?,?,?,?);',(int(values[0]),str(values[1]),int(values[2]),str(values[3]),str(values[4]),str(values[5])));
        conn.commit();

    elif int(choice) == 3: #Μαγαζί
        values=[1,2,3,4,5,6,7]
        values[0]=input("\nΕισάγετε Όνομα Μαγαζιού: ");
        values[1]=input("\nΕισάγετε ΑΦΜ Μαγαζιού: ");
        values[2]=input("\nΕισάγετε Τηλέφωνο Μαγαζιού: ");
        values[3]=input("\nΕισάγετε Πόλη: ");
        values[4]=input("\nΕισάγετε ΤΚ: ");
        values[5]=input("\nΕισάγετε Οδό: ");
        values[6]=input("\nΕισάγετε Είδος Κουζίνας: ");
        conn.execute('INSERT INTO Μαγαζί (`Όνομα`,`ΑΦΜ`,`Τηλέφωνο`,`Πόλη`,`ΤΚ`,`Οδός`,`Είδος_Κουζίνας`) VALUES (?,?,?,?,?,?,?);',(str(values[0]),int(values[1]),int(values[2]),str(values[3]),int(values[4]),str(values[5]),str(values[6])));
        conn.commit();

    elif int(choice) == 4: #Σχόλιο
        values=[1,2]

        first_name = str(input("\nΕισάγετε το Όνομα του Πελάτη που κάνει το Σχόλιο: "))
        last_name = str(input("\nΕισάγετε το Επώνυμο του Πελάτη που κάνει το Σχόλιο: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        IDpel = int(data[0][0])

        shop_name = str(input("\nΕισάγετε το Όνομα του Μαγαζιού στο οποίο γίνεται το Σχόλιο: "))
        c.execute("SELECT ID FROM Μαγαζί WHERE Όνομα == (?) ", (shop_name))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return
        IDshop = int(data[0][0])
        
        values[0]=input("\nΕισάγετε Αξιολόγηση 1.0 ως 5.0 : ");
        values[1]=input("\nΕισάγετε Περιγραφή: ");
        conn.execute('INSERT INTO Σχόλιο (`Αξιολόγηση`,`Περιγραφή`) VALUES (?,?);',(float(values[0]),str(values[1])));
        
        conn.commit()

        c.execute("SELECT ID FROM Σχόλιο WHERE Αξιολόγηση == (?) AND Περιγραφή == (?) ORDER BY ID DESC", (float(values[0]),str(values[1])))
        data = c.fetchall()
        IDcomm = int(data[0][0])

        conn.execute('INSERT INTO Σχολιάζει (`IDpelatis`,`IDsxolio`) VALUES (?,?);',(IDpel,IDcomm));
        conn.execute('INSERT INTO Σχολιάζεται (`IDsxolio`,`IDmagazi`) VALUES (?,?);',(IDcomm,IDshop));
        conn.commit()


    elif int(choice) == 5: #Προϊόν
        values=[1,2,3,4,5]
        shop_name_1 = str(input("\nΕισάγετε το Όνομα του Μαγαζιού του Προϊόντος: "))
        c.execute("SELECT ID FROM Μαγαζί WHERE Όνομα == (?) ", (shop_name_1,))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει το Μαγαζί")
            return
        IDshop_1 = int(data[0][0])
        values[0]=IDshop_1;
        values[1]=input("\nΕισάγετε Τιμή: ");
        values[2]=input("\nΕισάγετε Περιγραφή: ");
        values[3]=input("\nΕισάγετε Διαθεσιμότητα Yes ή No: ");
        values[4]=input("\nΕισάγετε Όνομα Προϊόντος: ");
        conn.execute('INSERT INTO Προϊόν (`IDmagazi`,`Τιμή`,`Περιγραφή`,`Διαθεσιμότητα`,`Όνομα`) VALUES (?,?,?,?,?);',(int(values[0]),float(values[1]),str(values[2]),bool(values[3]),str(values[4])));
        conn.commit()

    elif int(choice) == 6: #Διανομέας
        values=[1,2,3,4]
        values[0]=input("\nΕισάγετε Όνομα: ");
        values[1]=input("\nΕισάγετε Επώνυμο: ");
        values[2]=input("\nΕισάγετε Τηλέφωνο: ");
        values[3]=input("\nΕισάγετε ΑΦΜ: ");
        conn.execute('INSERT INTO Διανομέας (`Όνομα`,`Επώνυμο`,`Τηλέφωνο`,`ΑΦΜ`) VALUES (?,?,?,?);',(str(values[0]),str(values[1]),int(values[2]),int(values[3])));
        conn.commit()

    else:
        return


def update():
    c = conn.cursor()
    choice=int(input("Διαλέξτε Update:\n 1 Πελάτης\n 2 Διεύθυνση\n 3 Μαγαζί\n 4 Σχόλιο\n 5 Προϊόν\n 6 Διανoμέας\n 7 Επιστροφη\n"));
    
    if int(choice) == 1: #Πελάτης
        first_name = input("\nΕισάγετε Όνομα: ");
        last_name = input("\nΕισάγετε Επώνυμο: ");
        
        values=[1,2,3,4,5]
        values[0]=input("\nΕισάγετε Νέο Όνομα: ");
        values[1]=input("\nΕισάγετε Νέο Επώνυμο: ");
        values[2]=input("\nΕισάγετε Νέο Email: ");
        values[3]=input("\nΕισάγετε Νέο Κωδικό: ");
        values[4]=input("\nΕισάγετε Νέο Τηλέφωνο: ");
        conn.execute('UPDATE Πελάτης SET Όνομα = (?), Επώνυμο = (?), Email = (?), Κωδικός = (?), Τηλέφωνο = (?) WHERE Όνομα == (?) AND Επώνυμο == (?);',(str(values[0]),str(values[1]),str(values[2]),str(values[3]),int(values[4]),str(first_name),str(last_name)));
        conn.commit()

    elif int(choice) == 2: #Διεύθυνση
        values=[1,2,3,4,5,6]
        first_name = str(input("\nΕισάγετε το όνομα του Πελάτη που βρίσκεται στην Διεύθυνση: "))
        last_name = str(input("\nΕισάγετε το επώνυμο του Πελάτη που βρίσκεται στην Διεύθυνση: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return
        IDpel = int(data[0][0])

        odo=input("\nΕισάγετε Οδό: ");
        
        values[0]=IDpel;
        values[1]=input("\nΕισάγετε Νέα Πόλη: ");
        values[2]=input("\nΕισάγετε Νέο ΤΚ: ");
        values[3]=input("\nΕισάγετε Νέα Οδό: ");
        values[4]=input("\nΕισάγετε Νέο Όροφο: ");
        values[5]=input("\nΕισάγετε Νέο Λεπτομέρειες: ");
        conn.execute('UPDATE Διεύθυνση SET Πόλη = (?),ΤΚ = (?),Οδός = (?),Όροφος = (?),Λεπτομέρειες = (?) WHERE IDpelatis == (?) AND Οδός == (?);',(str(values[1]),int(values[2]),str(values[3]),str(values[4]),str(values[5]), IDpel, odo));
        conn.commit();

    elif int(choice) == 3: #Μαγαζί
        name=input("\nΕισάγετε Όνομα Μαγαζιού: ");
        thl=input("\nΕισάγετε Τηλέφωνο Μαγαζιού: ");
        
        values=[1,2,3,4,5,6,7]
        values[0]=input("\nΕισάγετε Νέο Όνομα Μαγαζιού: ");
        values[1]=input("\nΕισάγετε Νέο ΑΦΜ Μαγαζιού: ");
        values[2]=input("\nΕισάγετε Νέο Τηλέφωνο Μαγαζιού: ");
        values[3]=input("\nΕισάγετε Νέα Πόλη: ");
        values[4]=input("\nΕισάγετε Νέο ΤΚ: ");
        values[5]=input("\nΕισάγετε Νέα Οδό: ");
        values[6]=input("\nΕισάγετε Νέο Είδος Κουζίνας: ");
        conn.execute('UPDATE Μαγαζί SET Όνομα = (?),ΑΦΜ = (?),Τηλέφωνο = (?),Πόλη = (?),ΤΚ = (?),Οδός = (?),Είδος_Κουζίνας = (?) WHERE Όνομα == (?) AND Τηλέφωνο == (?);',(str(values[0]),int(values[1]),int(values[2]),str(values[3]),int(values[4]),str(values[5]),str(values[6]),str(name),int(thl)));
        conn.commit();

    elif int(choice) == 4: #Σχόλιο
        first_name = str(input("\nΔώστε Όνομα του Πελάτη: "))
        last_name = str(input("\nΔώστε Επώνυμο: "))
        phone = int(input("\nΔώστε το Τηλέφωνο του πελάτη: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return
        IDpel = int(data[0][0])

        c.execute ("""SELECT Σχόλιο.ID,Μαγαζί.Όνομα, Αξιολόγηση, Περιγραφή
        FROM Σχόλιο JOIN Σχολιάζεται ON Σχόλιο.ID == Σχολιάζεται.IDsxolio
        JOIN Μαγαζί ON IDmagazi == Μαγαζί.ID
        JOIN Σχολιάζει ON Σχολιάζει.IDsxolio == Σχόλιο.ID
        WHERE IDpelatis == (?)
        ORDER BY Μαγαζί.Όνομα ASC""", (IDpel,))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει Σχόλιο")
            return
        
        style="{:<2} {:<20} {:<5} {:<20}"
        i=1
        for t in data:
            print(style.format(i, t[1], t[2], t[3]))
            i=i+1
            
        ch = int(input("\nΕπιλέξτε Αριθμό Σχολίου για Επεξεργασία: "))
        IDsxolio = data[ch-1][0]

        aksiol = float(input("\nΕισάγετε Νέα Αξιολόγηση 1.0 ως 5.0 : "))
        perigr = str(input("\nΕισάγετε Νέα Περιγραφή: "))
        
        conn.execute("UPDATE Σχόλιο SET Αξιολόγηση = (?), Περιγραφή = (?) WHERE ID==(?)", (aksiol, perigr, IDsxolio,));
        conn.commit();


    elif int(choice) == 5: #Προϊόν
        values=[1,2,3,4,5]
        shop_name_1 = str(input("\nΕισάγετε το Όνομα του Μαγαζιού του Προϊόντος: "))
        c.execute("SELECT ID FROM Μαγαζί WHERE Όνομα == (?) ", (shop_name_1,))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει το Μαγαζί")
            return
        IDshop_1 = int(data[0][0])
        values[0]=IDshop_1;

        name = input("\nΕισάγετε Όνομα Προϊόντος: ");
        
        values[4]=input("\nΕισάγετε Νέο Όνομα Προϊόντος: ");
        values[1]=input("\nΕισάγετε Νέα Τιμή: ");
        values[2]=input("\nΕισάγετε Νέα Περιγραφή: ");
        values[3]=input("\nΕισάγετε Νέα Διαθεσιμότητα Yes ή No: ");
        
        conn.execute('UPDATE Προϊόν SET IDmagazi = (?),Τιμή = (?),Περιγραφή = (?),Διαθεσιμότητα = (?),Όνομα = (?) WHERE Όνομα == (?) AND IDmagazi == (?);',(int(values[0]),float(values[1]),str(values[2]),bool(values[3]),str(values[4]), str(name), int(IDshop_1)));
        conn.commit()

    elif int(choice) == 6: #Διανομέας
        first_name=input("\nΕισάγετε Όνομα: ");
        last_name=input("\nΕισάγετε Επώνυμο: ");
        phone=input("\nΕισάγετε Τηλέφωνο: ");

        values=[1,2,3,4]
        values[0]=input("\nΕισάγετε Όνομα: ");
        values[1]=input("\nΕισάγετε Επώνυμο: ");
        values[2]=input("\nΕισάγετε Τηλέφωνο: ");
        values[3]=input("\nΕισάγετε ΑΦΜ: ");
        conn.execute('UPDATE Διανομέας SET Όνομα = (?),Επώνυμο = (?),Τηλέφωνο = (?),ΑΦΜ = (?) WHERE Όνομα == (?) AND Επώνυμο == (?) AND Τηλέφωνο == (?);',(str(values[0]),str(values[1]),int(values[2]),int(values[3]),str(first_name),str(last_name),int(phone)));
        conn.commit()

    else:
        return

def delete():
    c = conn.cursor()
    choice=int(input("Διαλέξτε Delete:\n 1 Πελάτης\n 2 Διεύθυνση\n 3 Μαγαζί\n 4 Σχόλιο\n 5 Προϊόν\n 6 Διανομέας\n 7 Έξοδος\n"));

    if choice == 1:
        Pel_Fname = str(input("\nΔώστε Όνομα Πελάτη για Διαγραφή: "));
        Pel_Lname = str(input("\nΔώστε Επώνυμο: "));
        Pel_Thl = int(input("\nΔώστε Τηλέφωνο: "));
        conn.execute("DELETE FROM Πελάτης WHERE Όνομα==(?) AND Επώνυμο==(?) AND Τηλέφωνο==(?)", (Pel_Fname,Pel_Lname,Pel_Thl));
        conn.commit();
        
    elif choice == 2:
        first_name = str(input("\nΔώστε Όνομα του Πελάτη: "))
        last_name = str(input("\nΔώστε Επώνυμο: "))
        phone = int(input("\nΔώστε το Τηλέφωνο του πελάτη"))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?) AND Τηλέφωνο==(?)", (first_name, last_name, phone))
        data = c.fetchall()
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return
        IDpel = int(data[0][0])
        Tk = int(input("Δώστε Τ.Κ.: "));
        Rt = str(input("Δώστε Οδό : "));
        conn.execute("DELETE FROM Διεύθυνση WHERE IDpelatis==(?) AND ΤΚ==(?) AND Οδός==(?)", (IDpel,Tk,Rt));
        conn.commit();

    elif choice == 3:
        ShopName = str(input("\nΔώστε Όνομα Μαγαζιού: "));
        Phone = int(input("\nΔώστε Τηλέφωνο Μαγαζιού: "));
        conn.execute("DELETE FROM Μαγαζί WHERE Όνομα==(?) AND Τηλέφωνο==(?)", (ShopName,Phone));
        conn.commit();

    elif choice == 4:
        first_name = str(input("\nΔώστε Όνομα του Πελάτη: "))
        last_name = str(input("\nΔώστε Επώνυμο: "))
        phone = int(input("\nΔώστε το Τηλέφωνο του πελάτη: "))
        c.execute("SELECT ID FROM Πελάτης WHERE Όνομα == (?) AND Επώνυμο == (?)", (first_name, last_name))
        data = c.fetchall()
        IDpel = int(data[0][0])
        if data == [] :
            print("\nΔεν Υπάρχει Πελάτης")
            return

        c.execute ("""SELECT Σχόλιο.ID,Μαγαζί.Όνομα, Αξιολόγηση, Περιγραφή
        FROM Σχόλιο JOIN Σχολιάζεται ON Σχόλιο.ID == Σχολιάζεται.IDsxolio
        JOIN Μαγαζί ON IDmagazi == Μαγαζί.ID
        JOIN Σχολιάζει ON Σχολιάζει.IDsxolio == Σχόλιο.ID
        WHERE IDpelatis == (?)
        ORDER BY Μαγαζί.Όνομα ASC""", (IDpel,))
        data = c.fetchall()
        if data == [] :
            print("Δεν Υπάρχει Σχόλιο")
            return
        
        style="{:<2} {:<20} {:<5} {:<20}"
        i=1
        for t in data:
            print(style.format(i, t[1], t[2], t[3]))
            i=i+1
            
        ch = int(input("\nΕπιλέξτε Αριθμό Σχολίου για Διαγραφή: "))
        IDsxolio = data[ch-1][0]
        conn.execute("DELETE FROM Σχόλιο WHERE ID==(?)", (IDsxolio,));
        conn.commit();
        
        
    elif choice == 5:
        shop_name = str(input("\nΕισάγετε Όνομα Μαγαζιού: "))
        c.execute("SELECT ID FROM Μαγαζί WHERE Όνομα == (?) ", (shop_name,))
        data = c.fetchall()
        IDshop = int(data[0][0])
        if data == [] :
            print("\nΔεν Υπάρχει το Μαγαζί")
            return
        name = str(input("\nΔώστε Προϊόν για Διαγραφή: "));
        conn.execute("DELETE FROM Προϊόν WHERE Όνομα==(?) AND IDmagazi==(?)", (name,IDshop));
        conn.commit();

    elif choice == 6:
        D_Fname = str(input("\nΔώστε Όνομα Διανομέα για Διαγραφή: "));
        D_Lname = str(input("\nΔώστε Επώνυμο: "));
        D_Thl = int(input("\nΔώστε Τηλέφωνο: "));
        conn.execute("DELETE FROM Διανομέας WHERE Όνομα==(?) AND Επώνυμο==(?) AND Τηλέφωνο==(?)", (D_Fname,D_Lname,D_Thl));
        conn.commit();

    else:
        return


def firstmenu():
    choice = int(input("Επιλέξτε τι θέλετε να κάνετε:\n  1)Προσθήκη Παραγγελίας \n  2)Προσθήκη άλλου Στοιχείου\n  3)Επεξεργασία Στοιχείου\n  4)Διαγραφή Στοιχείου\n  5)Κλείσιμο\n"))
    
    while(choice != 5):
        match choice:
            case 1:
                paragelia()
            case 2:
                insert()
            case 3:
                update()
            case 4:
                delete()
            case _:
                break
        os.system('cls')
        choice = int(input("Επιλέξτε τι θέλετε να κάνετε:\n  1)Προσθήκη Παραγγελίας \n  2)Προσθήκη άλλου Στοιχείου\n  3)Επεξεργασία Στοιχείου\n  4)Διαγραφή Στοιχείου\n  5)Κλείσιμο\n"))
        
    
if __name__ == "__main__":
    global conn
    conn = sqlite3.connect("project.db");
    conn.execute("PRAGMA foreign_keys = ON")

    #Create Database with Data
    createbase()

    #Edit Database
    firstmenu()
    
    conn.close()
