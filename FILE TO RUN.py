import random   
import timeline as t # Information Files
import social as s 
import ott as o
import advancegraph as e # Graph Files
import socialgraph as f
import ottgraph as p

# This function prints the information about the advancement of communication
def infoadvancement():
        print("\n")
        print("-"*173)
        input_year = input("Enter a year (or 'quit' to exit): ")
        print("\n\n")
        if input_year.lower() == "quit":
            return
        if int(input_year)<500:
           print("No significant inventions were made in this timeline but",t.timeline[69])
           return
        elif int(input_year)<1450:
            print("No significant inventions were made in this timeline but",t.timeline[420])
            return
        try:
            input_year = int(input_year)
            if input_year not in t.timeline:
                print("No further advancements were made but",communication_in_year(input_year),"was the latest invention.","\n\n"+"Please input the mentioned years for information on specific inventions. ")
                return
        except ValueError:
            print("Invalid input. Please enter a year or 'quit'.")
            return
        print("\n\n"+"Year -",input_year,"\n\n")
        print(t.timeline[input_year])
        
# This function prints the information about the advancement of social media
def infosocial():
        print("\n")
        print("-"*173)
        input_year = input("Enter a year (or 'quit' to exit): ")
        if input_year.lower() == "quit":
            return
        try:
            input_year = int(input_year)
            if input_year<=2000:
                print("Social Media was developed and put into use after 19th Century, i.e. after the year 2000, Please choose a year after 2000")
                infosocial()
            if input_year>=2023:
                print("Please choose a year before 2023")
                infosocial()
            if input_year not in s.social_media:
                print("Year not found in timeline.")
                return
        except ValueError:
            print("Invalid input. Please enter a year or 'quit'.")
            infosocial()
            return
        print("\n\n"+"Year -",input_year,"\n")
        print(s.social_media[input_year])
        
# This function prints the information about the advancement of OTT PLatforms
def infoott():
        print("\n")
        print("-"*173)
        input_year = input("Enter a year (or 'quit' to exit): ")
        if input_year.lower() == "quit":
            return
        try:
            input_year = int(input_year)
            if input_year<=2000:
                print("OTT was developed and put into use after 19th Century, i.e. after the year 2000, Please choose a year after 2006")
                infoott()
            if input_year>2023:
                print("Please choose a year before 2023")
            if input_year not in o.ott:
                print("During this year, no OTT platforms were created or brought to market.")
                return
        except ValueError:
            print("Invalid input. Please enter a year or 'quit'.")
            infoott()
            return
        print("\n\n"+"Year -",input_year,"\n")
        print(o.ott[input_year])
        
# This function contains and returns information about timeline of communication between certain timelines
def communication_in_year(year):
    if year < 500:
        return "Cave Paintings "
    elif year > 500 and year < 1450:
        return "Pigeons and Messengers"
    elif year > 1450 and year < 1792:
        return "Printing Press"
    elif year > 1792 and year < 1876:
        return "Telegraph"
    elif year > 1876 and year < 1895:
        return "Telephone"
    elif year > 1895 and year < 1927:
        return "Radio or Wireless Telegraph"
    elif year > 1927 and year < 1962:
        return "Television"
    elif year > 1962 and year < 1971:
        return "Communication satellites"
    elif year > 1971 and year < 1973:
        return "Emails"
    elif year > 1973 and year < 1989:
        return "Cellular Phones"
    elif year > 1989 and year < 1992:
        return "World Wide Web"
    elif year > 1992 and year < 2000:
        return "Text messages"
    elif year > 2000 and year < 2006:
        return "Video Conferencing"
    elif year > 2006 and year < 2007:
        return "Cloud Storage"
    elif year > 2007 and year < 2009:
        return "Smartphones."
    elif year > 2009 and year < 2011:
        return "Wearable Technology"
    else:
        return "Virtual Assistants"
    
# This Function prints information about a random year communication invention
def random_communication_in_year():
    year = random.randint(400, 2010)
    print("\n\n"+"Year -",year,"\n-")
    communication = communication_in_year(year)
    print(f"In {year}, {communication}, was the latest invention")
    
# This Function prints information about a random year's social media release
def random_social_in_year():
    year = random.randint(2001, 2020)
    print("\n\n"+"Year -",year,"\n")
    try:
        if year<2000 or year>=2021:
            random_social_in_year()
        if year not in s.social_media:
            print("No particular social media was found in",year,"but social media's were founded after 2002.")
            return
    except ValueError:
        print("Invalid input. Please enter a year or 'quit'.")
        infosocial()
        return
    print(s.social_media[year])
    
# This Function prints information about a random year's OTT platform release
def random_ott_in_year():
    year = random.randint(2001, 2020)
    print("\n\n"+"Year -",year,"\n")
    try:
        if year<2000 or year>=2021:
            random_ott_in_year()
        if year not in s.social_media:
            random_ott_in_year()
    except ValueError:
        print("Invalid input. Please enter a year or 'quit'.")
        infoott()
        return
    print(s.social_media[year])

# This Function prompts the user with Menu based approach, and then calls the required functions using if,elif,else statements.
def prompt_user():
    while True:
        print("\n")
        print("-"*173)
        print("Select an option:")
        print("1. Communicational Advancement")
        print("2. Social Media")
        print("3. OTT Platforms")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("-"*173)
            print("                                                                       Communicational Advancement")
            print("-"*173)
            print("Select an option:")
            print("1. View communication timeline graph")
            print("2. Get detailed information about the communication advancement for any specific year [1450, 1792, 1876, 1895, 1927, 1962, 1971, 1973, 1989, 1992, 2000, 2006, 2007, 2009, 2011]")
            print("3. Get communication technology for any random year")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("                                                                  Communicational Timeline Graph")
                print("-"*173)
                e.timeline(e.events)
                print("-"*173)
            elif choice == "2":
                infoadvancement()
            elif choice == '3':
                random_communication_in_year()
            elif choice =='4':
                continue
            else:
                print("Please Enter a Valid Input")
        elif choice == "2":
            print("\n")
            print("-"*173)
            print("                                                                             Social Media")
            print("-"*173)
            print("Select an option:")
            print("1. View Social Media graph")
            print("2. Get detailed information about Social Media for any specific year [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]")
            print("3. Get social media release for any random year")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                    print("                                                                  Social Media Graph")
                    print("-"*173)
                    f.timeline(f.events)
                    print("-"*173)
            elif choice=='2':
                infosocial()
            elif choice == '3':
                random_social_in_year()
            elif choice == '4':
                continue
            else:
                print("Please Enter a Valid Input")
        elif choice == "3":
            print("\n")
            print("-"*173)
            print("                                                                                  OTT")
            print("-"*173)
            print("Select an option:")
            print("1. View OTT Platform graph")
            print("2. Get detailed information about OTT Platform\'s for any specific year [2004,2006,2007,2008,2011,2010,2014,2015,2017,2018,2019,2020,2021]")
            print("3. Get OTT release for any random year")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                    print("                                                                  OTT Platform Graph")
                    print("-"*173)
                    p.timeline(p.events)
                    print("-"*173)
            elif choice=='2':
                infoott()
            elif choice == '3':
                random_ott_in_year()
            elif choice == '4':
                continue
            else:
                print("Please Enter a Valid Input")
        elif choice == "4":
            print("Hope that your time was informational.")
            break
        else:
            print("Please Enter a Valid Input")
            
# Main Body
print("\n                                                                             Innovations of Communication")
prompt_user()
