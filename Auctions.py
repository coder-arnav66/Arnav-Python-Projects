import webbrowser
import random
import time
print("Welcome to Auctions created by Arnav Saket.\nDifferent types of Players,\nPut them in Your team before the computer.\nYour team will be judged by internet.\nOn google, click on ai mode to know answer.")
gk= [                                                                                #famous keepers around the world
    "Buffon",
    "Casillas",
    "Neuer",
    "Alisson",
    "Courtois",
    "De Gea",
    "Oblak",
    "Donnarumma",
    "Čech",
    "Van der Sar",
    "Yashin",
    "Banks",
    "Zoff",
    "Maier",
    "Zamora",
    "Chilavert",
    "Schmeichel",
    "Shilton",
    "Plánička",
    "Carrizo",
    "Kahn",
    "Southall",
    "Preud'homme",
    "Pfaff",
    "Dasayev",
    "Beara",
    "Combi",
    "Zenga",
    "Fillol",
    "Mazurkiewicz",
    "Gilmar",
    "Trautmann",
    "Arconada",
    "Zubizarreta",
    "Clemence",
    "Pagliuca",
    "Peruzzi",
    "Taffarel",
    "Júlio César",
    "Barthez",
    "Seaman",
    "Lehmann",
    "Illgner",
    "Ter Stegen",
    "Ederson",
    "Navas",
    "Dida",
    "Baía",
    "Lloris",
    "Martínez"
]

cb = [
    "Beckenbauer",
    "Baresi",
    "Cannavaro",
    "Hierro",
    "Koeman",                                                                      #famous defenders around the world
    "Puyol",
    "Ramos",
    "Terry",
    "Vidic",
    "Ferdinand",
    "Chiellini",
    "Thiago Silva",
    "Van Dijk",
    "Kompany",
    "Desailly",
    "Scirea",
    "Passarella",
    "Sammer",
    "Pique",
    "Nesta",
    "Stam",
    "Ayala",
    "Materazzi",
    "Godín",
    "Pepe",
    "Carvalho",
    "Marquez",
    "Lucio",
    "Aldair",
    "Córdoba",
    "Adams",
    "Butcher",
    "Bruce",
    "Campbell",
    "Keown",
    "Cannavaro",
    "Bonucci",
    "Barzagli",
    "Ruggeri",
    "Perfumo",
    "Riolfo",
    "Ruggeri",
    "Moreno",
    "Gómez",
    "Hummels",
    "Boateng",
    "Süle",
    "Alaba",
    "Varane",
    "Koundé",
    "Upamecano",
    "Saliba",
    "Gabriel",
    "Stones",
    "Maguire",
    "Evans",
    "Dier",
    "Laporte",
    "Ake",
    "De Ligt",
    "Timber",
    "Blind",
    "Reiziger",
    "Cocu",
    "Hierro",
    "Sanchís",
    "Ramos",
    "Albiol",
    "Nacho",
    "Carles Rexach",
    "Migueli",
    "Segarra",
    "Ronald Koeman",
    "Mascherano",
    "Otamendi",
    "Lisandro Martínez",
    "Romero",
    "Samuel",
    "Burdisso",
    "Ayala",
    "Domínguez"
]

rb = [
    "Cafu",
    "Alves",
    "Lahm",
    "Neville",
    "Zanetti",
    "Walker",
    "Alexander-Arnold",
    "Hakimi",
    "Maicon",
    "Salgado",
    "Sagna",
    "Lauren",
    "Bellerín",
    "Roberto",
    "Cancelo",
    "Danilo",
    "Lichtsteiner",
    "Fernandes",
    "Meunier",
    "Semedo",
    "Pereira",
    "Janmaat",
    "Trippier",
    "Wan-Bissaka",
    "James",
    "Pavard",
    "Zabaleta",
    "Johnson",
    "Florenzi",
    "Cicinho",
    "Srna",
    "Rafinha",
    "Juanfran",
    "Babbel"
]

lb = [
    "Maldini",
    "Carlos",
    "Cole",
    "Evra",
    "Marcelo",
    "Alba",
    "Alaba",
    "Robertson",
    "Hernandez",
    "Mendy",
    "Baines",
    "Irwin",
    "Camacho",
    "Lizarazu",
    "Le Saux",
    "Maxwell",
    "Sorín",
    "Ziege",
    "Favalli",
    "Rodríguez",
    "Shaw",
    "Alex Sandro",
    "Spinazzola",
    "Alonso",
    "Clichy",
    "Abidal",
    "Sylvinho",
    "Albiston",
    "Valente",
    "Tierney",
    "Monreal",
    "Cucurella",
    "Ferland Mendy",
    "Guerreiro",
    "Blind"
]

cm = [
    "Xavi", "Iniesta", "Modric", "Kroos", "Pirlo",
    "Scholes", "Lampard", "Gerrard", "Seedorf", "Riquelme",
    "Busquets", "Casemiro", "Kante", "De Bruyne", "Vieira",
    "Keane", "Gattuso", "Essien", "Falcao", "Redondo",
    "Makelele", "Toure", "Fabregas", "Ozil", "Pjanic",
    "Veron", "Deco", "Xhaka", "Thiago", "Arthur",                                        #famous midfielders around the world
    "Milner", "Henderson", "Pogba", "Matic", "Fernandinho",
    "Gundogan", "Mount", "Pedri", "Gavi", "Valverde",
    "Locatelli", "Tonali", "Bellingham", "Rice", "Phillips",
    "Zielinski", "Eriksen", "Witsel", "Nainggolan", "Banega"
]

lw = [
    "Giggs", "Overmars", "Nedved", "Ronaldinho", "Ribery",
    "Hazard", "Salah", "Mane", "Neymar", "Mbappe",
    "Di Maria", "Zola", "Stoichkov", "Kostic", "Perisic",
    "Insigne", "Sané", "Grealish", "Rashford", "Vinicius",                                #famous wingers around the world
    "Martial", "Pires", "Pedro", "Willian", "Trossard",
    "Chiesa", "Gakpo", "Barnes", "Kvaratskhelia", "Son"
]

rw = [
    "Figo", "Beckham", "Best", "Garrincha", "Robben",
    "Sterling", "Sancho", "Mahrez", "Saka", "Bale",
    "Pepe", "Coman", "Bernardo", "Kulusevski", "Dembele",
    "Ziyech", "Hazard T.", "Shaqiri", "Under", "Politano",
    "Chiesa F.", "Pedro R.", "Willian J.", "Pires R.", "Navas",
    "Mkhitaryan", "Ocampos", "Rodrygo", "Asensio", "Diaz"
]

st = [
    "Pele", "Maradona", "R9", "Cristiano", "Eusebio",
    "Van Basten", "Shevchenko", "Henry", "Drogba", "Lewandowski",
    "Suarez", "Benzema", "Kane", "Haaland", "Rooney",
    "Villa", "Torres", "Aguero", "Tevez", "Batistuta",                                   #famous strikers around the world
    "Klose", "Inzaghi", "Del Piero", "Trezeguet", "Vieri",
    "Rivaldo", "Stoichkov", "Romario", "Baggio", "Lineker",
    "Klinsmann", "Papin", "Weah", "Sanchez", "Hugo",
    "Giroud", "Morata", "Immobile", "Lukaku", "Dzeko",
    "Osimhen", "Martinez", "Griezmann", "Mbappe", "Rashford",
    "Nunez", "Isak", "Felix", "Jesus", "Firmino"
]

ugk = []
ucb = []
urb = []
ulb = []
ucm = []
ulw = []                                                                               #empty lists
urw = []
ust = []


cgk = []
ccb = []
crb = []
clb = []
ccm = []
clw = []
crw = []
cst = []


def auction(pos, plist, u_t, c_t):                                                     #defining the game
    for i in range(5):
        player = random.choice(plist)
        print("You have 5 chance. choose or play without them.")
        user = input(f"{pos} : {player}. Yes/no: ")
        if(user == "yes"):
            print(f"You chose: {player}")
            u_t.append(player)
            c = random.choice(plist)
            while c == player:
                c = random.choice(plist)
            print(f"Computer chose: {c}")
            c_t.append(c)
            print(pos, "chosen.")
            return
        

auction("goalkeeper", gk, ugk, cgk)
auction("center back", cb, ucb, ccb)
auction("center back#2", cb, ucb, ccb)
auction("left back", lb, ulb, clb)
auction("right back", rb, urb, crb)                                                 #function call with different parameters
auction("center midfielder", cm, ucm, ccm)
auction("center midfielder#2", cm, ucm, ccm)
auction("left wing", lw, ulw, clw)
auction("right wing", rw, urw, crw)
auction("striker", st, ust, cst)
auction("striker#2", st, ust, cst)

ct = cgk + ccb+crb+clb+ccm+clw+crw+cst
ut = ugk + ucb + urb + ulb + ucm + ulw + urw + ust

print("Your team:", ut)
print("Computer's team", ct)                                                       #team overview
print("Internet searching process starting...")
time.sleep(10)

webbrowser.open(f"https://www.google.com/search?q=me+and+my+friend+were+playing+auctions+and+my+team+is+{ut}+and+my+friend's+team+is+{ct}+based+on+the+team+tell+who+won+in+brief")
                                                                                   #result using webbrowser


