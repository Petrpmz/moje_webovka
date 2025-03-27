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


# import re
# text = "Toto je pokusný TEXT pro regulární Výrazy."

#vrátí seznam všech vyhovujících podřetězců (na jeden průchod)
# vys = re.findall(r"T\w{1}",text)
# vys = re.findall(r"\s{1}\w*\s{1}",text) #tady je vidět, jak pracuje s těmi mezerami
# print(vys)

# match() testuje, zda řetězec odpovídá formátu, když ano, 
# vrací Match object, jinak vrací None
# search() vyhledává první výskyt řetězce, který odpovídá 
# formátu, když ano, vrací Match object, jinak vrací None
import re

text = "Text obsahující <data> v ostrých závorkách."
text = "<data>"

vys = re.match(r"<\w+>",text)
# vys = re.search(r"<\w+>",text)

print(vys.group(0))  #vrátí nalezenou skupinu znaků
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
1) Řetězec, ve kterém je "a" a po něm žádné nebo více "b". (findall)
"""
import re
retezec = "ab abb aabbbbb abbb"
vysledky = re.findall(r"(ab*)", retezec)
print(vysledky)
"""
2) Řetězec, ve kterém je "a" a po něm jedno nebo více "b".
"""
import re
retezec = "ab abb aabbbbb abbb"
vysledky = re.findall(r"(ab+)", retezec)
print(vysledky)
"""
3) Řetězec, ve kterém je "a" a po něm nula nebo jedno "b".
"""

"""
4) Řetězec, ve kterém je "a" a po něm třikrát "b"
"""
import re
retezec = "ab abb aabbbbb abbb"
vysledky = re.findall(r"abbb", retezec)
print(vysledky)
"""
5) Najděte v řetězci (první) slovo, ve kterém je "z". (search)

"""
import re

text = "hghfgh fghgd hazlo asdasdas hzth."

z = re.search(r'\b\w*z\w*\b', text)

if z:
    print(z.group(0))
else:
    print("Není žádné.")

"""
6) Najděte v řetězci všechna slova, ve kterých je "z". (findall)
"""
import re

text = "hghfgh fghgd hazlo asdasdas hzth."

z = re.findall(r'\b\w*z\w*\b', text)

if z:
    print(z)
else:
    print("Není žádné.")


"""
7) Vypište pouze jména, končící na "ová" z řetězce: 
   "Brom Pešková Forstová Turek Ježek Gergelitsová Holan" (findall)
"""
import re

text = "Brom Pešková Forstová Turek Ježek Gergelitsová Holan"

x = re.findall(r'\b\w+ová\b', text)

print(x)

"""
8) Z následujícího řetězce vypište všechna slova končící otazníkem (findall)
"""
import re

text = "Řetězec obsahuje slova s otazníkem? Anebo dva?"

y = re.findall(r'\b\w+\?', text)

print(y)

"""
9) Zjistěte, jestli řetězec odpovídá studentskému číslu (match)
   na naší škole.\

"""
studentske_cislo = " her41064"
  
u= re.match(r"^[a-z]{3}\d{5}$", studentske_cislo)
if u:
    print(u.group())
else:
    print("None.")


"""
10) Zjistěte, zda je na vstupu desetinné číslo. (match)
"""
import re

vstup = input("Zadejte číslo: ")

k= re.match(r"\d+\.\d+", vstup)

if k:
    print("číslo je desetinne",k.group())
else:
    print("Vstup není desetinné číslo.")
"""

5) Všechna trojiferná čísla z řetězce. Pozor "1234" není trojciferné!
"""
import re

text= "123 568 965 445465465 45646 123 45465465"

cisla = re.findall(r'\b\d{3}\b', text)

print(cisla)
"""

Navíc:
8) Z řetězce: "Isaac Newton, fyzik" vypište pomocí match a group postupně "Isaac Newton", "Isaac", "Newton"
9) Odstraňte z emailu, co tam nepatří: klara@tohle_prycemail.cz
  použijte search a .start() a .end()
10) Vypište jméno a příjmení z "Klára Pešková". Použijte pojmenované skupiny (?P<jmeno>...), (?P<prijmeni>...)
""" 

