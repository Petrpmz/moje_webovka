"""
Regulární výrazy (regular expressions)
- zkráceně regex či regexp
- je speciální řetězec znaků, který představuje určitý 
  vzor (chcete-li masku) pro textové řetězce
- označením řetězců jako raw (použitím r'' nebo r"")
  se vyhneme problémům s vyhodnocováním sekvencí 
  obsahujících zpětné lomítko \

Regulární výrazy se nejčastěji používají v těchto případech:
- validace vstupů (match)
– zjištění, kde se v textu nachází hledaný podřetězec (search)
- nahrazení podřetězce v řetězci (sub)
- získání všech výskytů podřetězce (findall)

Odkazy:
https://www.regularnivyrazy.info/
https://www.regularnivyrazy.info/regularni-vyrazy-zaklady.html  
https://naucse.python.cz/2020/pyladies-ostrava-podzim-pokrocili/intro/regex/
"""
r"""
Kvantifikátory
? znamená žádný nebo 1 výskyt
* znamená žádný a více výskytů
+ znamená 1 a více výskytů
{cislo} znamená přesný počet výskytů
{min,max} počet výskytů mezi horní a dolní mezí (včetně obou mezí)
{min,} počet výskytů bude minimálně min

Zástupné znaky
. je zástupným znakem pro jakýkoli jiný znak
^ označuje začátek řetězce (případně řádku)
$ označuje konec řetězce (případně řádku)
\ escape znak pro použití speciálních znaků v řetězci

Skupiny znaků
Lze je zadat několika způsoby:
- výčtem – např. [abc]
- rozsahem – např. [a-z]
- kombinací – např. [abcx-z1-3]
- vyloučením - např. [^abc] -> vše kromě znaků [abc]
- skupinou znaků - např. (abc)
- výběrem z možností - např. Petr|Pavel
- sekvencí zastupující celou skupinu znaků:

\d - číslice – ekvivalent pro [0-9]
\D - vše kromě číslic
\s - tzv. bílé znaky – mezeru, tabulátor atp.
\S - vše kromě bílých znaků
\w - alfanumerické znaky a podtržítko – ekvivalent s [a-zA-Z0-9_]
\W - vše kromě znaků z \w
\b - začátek slova, konec slova
"""


import re
text = "Toto je pokusný TEXT pro regulární Výrazy v anketě TýTý."

#vrátí seznam všech vyhovujících podřetězců (na jeden průchod)
# vys = re.findall(r"T\w{1}",text)
# vys = re.findall(r"\s{1}\w*\s{1}",text) #tady je vidět, jak pracuje s těmi mezerami
# print(vys)

# match() testuje, zda řetězec odpovídá formátu, když ano, 
# vrací Match object, jinak vrací None
# search() vyhledává první výskyt řetězce, který odpovídá 
# formátu, když ano, vrací Match object, jinak vrací None


# text = "Text obsahující <data> v ostrých závorkách."
# text = "<data>"

# vys = re.match(r"<\w+>",text)
# vys = re.search(r"<\w+>",text)

# print(vys)
# print(vys.group(0))  #vrátí nalezenou skupinu znaků
# print(vys.start())   #vrátí index začátku této skupiny
# print(vys.end())     #vrátí index konce této skupiny






#split() rozdělí řetězec podle regulárního výrazu
# vys = re.split('\W+', 'Slova, slova; slova: slova')
# print(vys)

#sub() nahradí v řetězci podřetězce odpovídající regulárnímu výrazu
# text = "Bread  and butter and    ham  and  spam"
# vys = re.sub(r"\s+and\s+", " & ", text)
# print(vys)

#najde všechny shody a vrátí je v podobě Match objektů
# for i in re.finditer(r".y", "Naše staré hodiny bijí čtyři hodiny."):
#     print(i)


# Pozn. Regulární výraz lze zkompilovat a použít rychlejším způsobem.

"""
Cvičení:
text = "babička a prababička se učily abbb abecedu"
1) Řetězec, ve kterém je "a" a po něm žádné nebo více "b". (findall)
2) Řetězec, ve kterém je "a" a po něm jedno nebo více "b".
3) Řetězec, ve kterém je "a" a po něm nula nebo jedno "b".
4) Řetězec, ve kterém je "a" a po něm třikrát "b".
5) Všechna trojiferná čísla z řetězce. Pozor "1234" není trojciferné!
6) Najděte v řetězci (první) slovo, ve kterém je "z". (search)
7) Najděte v řetězci všechna slova, ve kterých je "z". (findall)
8) Vypište pouze jména, končící na "ová" z řetězce: 
   "Brom Pešková Forstová Turek Ježek Gergelitsová Holan" (findall)
9) Z následujícího řetězce vypište všechna slova končící otazníkem (findall)
10) Zjistěte, jestli řetězec odpovídá studentskému číslu 
   na naší škole. (match)
11) Zjistěte, zda je na vstupu desetinné číslo. (match)
"""






"""
Navíc:
8) Z řetězce: "Isaac Newton, fyzik" vypište pomocí match a group postupně "Isaac Newton", "Isaac", "Newton"
9) Odstraňte z emailu, co tam nepatří: klara@tohle_prycemail.cz
  použijte search a .start() a .end()
10) Vypište jméno a příjmení z "Klára Pešková". Použijte pojmenované skupiny (?P<jmeno>...), (?P<prijmeni>...)
"""