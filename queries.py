import	sqlite3, os;


def querie1():
    c = conn.cursor()
    c.execute("""
        SELECT Όνομα, avg(Αξιολόγηση)
        FROM Σχόλιο JOIN Σχολιάζεται ON Σχόλιο.ID = IDsxolio JOIN
        Μαγαζί ON Μαγαζί.ID = IDmagazi 
        GROUP BY IDmagazi
        HAVING avg(Αξιολόγηση) > 2.5
        """)
    data = c.fetchall()
    style = "{:<25} {:<5}"
    for t in data:
        print(style.format(t[0], t[1]))

def querie2():
    c = conn.cursor()
    c.execute("""
        SELECT Συνολική_Αξία, Ημερομηνία, Χρόνος_Παράδοσης
        FROM Παραγγελία JOIN Παραδίδει ON Παραγγελία.ID = IDparagelia
        WHERE Χρόνος_Παράδοσης < 30
        """)
    data = c.fetchall()
    style = "{:<8} {:<15} {:<5}"
    for t in data:
        print(style.format(t[0], t[1], t[2]))
  
def querie3():
    c = conn.cursor()
    c.execute("""
        SELECT Όνομα, count(IDparagelia)
        FROM Δέχεται JOIN Παραγγελία ON Παραγγελία.ID = IDparagelia JOIN
        Μαγαζί ON Μαγαζί.ID = IDmagazi 
        GROUP BY IDmagazi
        ORDER BY count(IDparagelia) DESC
        """)
    data = c.fetchall()
    style = "{:<25} {:<5}"
    for t in data:
        print(style.format(t[0], t[1]))
  

if __name__ == "__main__":
    global conn	
    conn = sqlite3.connect("project.db");
    choice = int(input("Επιλέξτε το querie που θέλετε να κάνετε: \n1) Ποια Μαγαζιά έχουν κριτική πάνω από 2.5? \n2) Ποιες Παραγγελίες έχουν χρόνο παράδωσης κάτω από 30 λεπτά? \n3) Δείξτε πόσες Παραγγελίες έχει κάθε Μαγαζί με ελάχιστη 1. \n4) Κλείσιμο \n"))
    print("\n")
    while choice!= 4:
        match choice:
            case 1:
                querie1()
                print("\n")
            case 2:
                querie2()
                print("\n")
            case 3:
                querie3()
                print("\n")
        
        choice = int(input("Επιλέξτε το querie που θέλετε να κάνετε: \n1) Ποια Μαγαζιά έχουν κριτική πάνω από 2.5? \n2) Ποιες Παραγγελίες έχουν χρόνο παράδωσης κάτω από 30 λεπτά? \n3) Δείξτε πόσες Παραγγελίες έχει κάθε Μαγαζί με ελάχιστη 1. \n4) Κλείσιμο \n"))
        print("\n")
    conn.close();

