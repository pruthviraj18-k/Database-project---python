import sqlite3

connection = sqlite3.connect("adhar.db")
print("\nData base opened")

cursor = connection.cursor()

connection.execute("""CREATE TABLE IF NOT EXISTS adhar_details(
    ADHAR_NUMBER PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    MOBILE_NUMBER NUMBER NOT NULL)""")
print("\nTable Created")

def insert_data (ADHAR_NUMBERs,NAMEs,MOBILE_NUMBERs):
    connection.execute("""INSERT OR IGNORE INTO adhar_details (ADHAR_NUMBER,NAME,MOBILE_NUMBER)
    VALUES (?,?,?)""",(ADHAR_NUMBERs,NAMEs,MOBILE_NUMBERs))

insert_data(102788238398,"Mantesh",1482091122 )
insert_data(461180192340,"Chandra shekar",9660329253 )
insert_data(508120424203,"Vinod rai",5568155252 )
insert_data(979040241497,"Kantirav",9164130386 )
insert_data(105922621845,"Mohan Kumar",1861984470  )
insert_data(943653785109,"Ganguly",3961549845 )
insert_data(823740664288,"Akshata",3551616091 )
insert_data(733783571727,"Manmohan D",4985309369 )
insert_data(181948610202,"Manjunath",3026759619 )
insert_data(865017263570,"Gurushekar",2763350866 )
insert_data(982275045163,"Vikranth",7071127937 )
insert_data(248114878850,"Soumya",3185245218 )
insert_data(181553145163,"Kumar Senthil",9268292196 )
insert_data(733725079267,"Pruthviraj K",3483656379 )

connection.commit()

connection.execute("""CREATE TABLE IF NOT EXISTS adhar_with_vaccine_details(
    ADHAR_NUMBER PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    MOBILE_NUMBER NUMBER NOT NULL,
    DOSAGE STRING(10) NOT NULL)""")
print("\nadhar_with_vaccine_details Table Created")

def insert_data2 (adhar_no,adhar_name,mob_no,dosage):
    connection.execute("""INSERT OR IGNORE INTO adhar_with_vaccine_details (ADHAR_NUMBER,NAME,MOBILE_NUMBER,DOSAGE)
    VALUES (?,?,?,?)""",(adhar_no,adhar_name,mob_no,dosage))

try:
    should_continue = True
    while should_continue:
        print("\nWelcome to Covid vaccine update page")
        update = input("\nWould you like to update your vaccine details ? (Type 'Yes' to continue or 'No' to exit) : ") 
        if update.lower() == "yes":
            adhar_no = int(input("\nPlease enter your 12 digit adhar number : "))
            cursor.execute("SELECT * FROM adhar_details WHERE ADHAR_NUMBER = ?", (adhar_no,))
            db_result=cursor.fetchall()
            if len(db_result)!=0:
                print("\nYour adhar number is verified")
                for i in db_result:
                    adhar_name = input("\nPlease enter your name as per the adhar card : ").lower()
                    if i[1].lower() == adhar_name.lower():
                        print("\nYour adhar name is verified")
                        mob_no = int(input("\nPlease enter your mobile number as per the adhar card : "))
                        if i[2] == mob_no:
                            print("\nyour phone number linked to adhar card is verified ")
                            dosage = input("\nplease enter your number of vaccine doses taken (0,1,2,'booster') : ")
                            insert_data2(adhar_no,adhar_name,mob_no,dosage)
                            cursor.execute ("select * from adhar_with_vaccine_details")
                            
                            print("\nYour Vaccine details are updated.")
                            if (dosage) == "0":
                                print("\nCorona Virus is spreading faster and taking so many lives of people, Kindly take vaccine to fight against the virus.")
                                should_continue = False
                            elif (dosage) == "1":
                                print("\nKindly remember to take subsequent doses to fight against the virus.")
                                should_continue = False
                            elif (dosage) == "BOOSTER".lower():
                                print("\nYou vaccine status is up to date.")
                                should_continue = False
                            else :  
                                print("\nKindly remember to take subsequent doses to fight against virus, Now booster doses are available.")
                                should_continue = False
                                
                            print(f"\nYour updated details {cursor.fetchall()}\n")
                        else: 
                            print("\nInvalid mobile number try again.\n")
                    else:
                        print("\nInvalid name please try again.\n")
            else:
                print("\nInvalid Adhar Number - Record not found try again.\n")   
        elif update.lower() == "no":
            print("\nExit")
            should_continue = False
        else:
            print("\nPlease type proper key as shown in screen")
               

except ValueError:
    print("\nError occured : You have Entered wrong data, Please enter valid data and try again.")

finally:
    print("\nThank you.\n")       
