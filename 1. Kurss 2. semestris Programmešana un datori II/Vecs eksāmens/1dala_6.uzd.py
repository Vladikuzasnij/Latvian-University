"""
объяснить разницу 
пояснить разницу

kopa un viendimensijas masīvs – viendimensijas masīvs var saturēt jebkādus elementus, arī tādus, kas atkārtojas, 
taču kopā katrs elements parādās tikai vienu reizi, piemēram, viendimensijas masīvs var būt 1,1,1 bet kopa sastāvēs tikai no elementa 1

ieraksts (struktūra) un masīvs – ierakstā nav noteikts elementu skaits, taču definējot masīvu ir jāzina, cik elementu tajā būs. 
Ierakstā katram objektam ir vairākas īpašības, šos ierakstus var ievietot masīvā, tādējādi katram masīva elementam būs ne tikai tā nosaukums, bet arī citas īpašības

steks, rinda un saraksts – stekam var peikļūt tikai pirmajam un pēdējam elementam, rindai visiem elementiem, taču, ja notiek pārbīde, tad uzreiz nomainās arī attiecīgā elementa atrašanās vieta, bet sarakstam arī var piekļūt visiem elementiem, taču elementu numerācija nemainās


"""

"""
Kopa - ir nesakārtots elementu kopums, kas nesatur vienādus elementus. (Tāpat kā matemātikā).
Viendimensijas masīvs var saturēt tādus elementus kas atkartojas, bet kopā katrs elements ir unikāls.
Arī viendimensijas masīva visi elementi ir indeksēti ([0], [1], [2], [3], [4]). Tātad ir svarīga secība.
bet kopa nav indeksācijas un mēs nevaram iet pa indeksiem. Kopai nav secībās.

numpy.array([2,2,2,1,3,4,6,2,2,2]) - viendimensijas masīvs un tas satur elementus, kuras skaitliskas vērtības ir vienādas, bet tie skaitās kā dazādi ar dažādiem indeksiem.
set((2,2,2,3,4)) - tas kopa ir ekvivalenta kopai set((2,3,4)), un nevar indeksēt, jo kopai nav secībās.

kopas ir lai ja nepieciešams glabāt unikālus elementus, bet masīvi ir ja nepieciešams glabāt un operēt ar secīgiem elementiem, kurus mēs var piekļūt, izmantojot indeksāciju.

----------------------

Ieraksti (struktūras) ir datu struktūras, kas ļauj grupēt dažāda veida atribūtus vienā objektā.
Ierakstā nav noteikts elementu skaits, bet masīva ir jāzina, cik elementu tajā būs. 

Ieraksts piemērs:
cilveks = types.SimpleNamespace()
cilveks.name = "John"
cilveks.age = 25

tas ir ieraksts (klase, kur ir tikai __init__ un atribūti).

masīvi ir datu struktūras, kas ļauj glabāt un operēt ar vairākiem elementiem, kas var būt vienāda vai atšķirīga datu tipa. 
Ieraksti ir nepieciešāmi lai organizēt un grupēt daudzus atribūtus vienā objektā, bet masīvi ir piemēroti, ja nepieciešams glabāt un operēt ar vairākiem elementiem secīgi.
Ierakstā katram objektam ir vairākas definētas īpašības. 
Ierakstus var ievietot masīvā, tad katram elementam būs ne tikai tā nosaukums (un kāda vertība), bet arī citas īpašības, kas tika noteiktas ierakstā.

Steks - var dabūt tikai pirmo un pedēju elementu. Pēdējais elements, kas tiek pievienots stekam, ir pirmais elements, kas būs izņemts no steka.
Steku analoģija ir grāmatu kaudze (nevar dabūt vidējo grāmatu neizņēmot visus kas bijušas virs tas grāmatas).
Rinda - datu struktūra, pirmāis elements, kas tiek pievienots rindai, ir pirmais elements, kas būs izņemts no rindas.
Rindas analoģija ir rindas veikalā reāla dzīve. Kas pirmais atnāca, tas pirmais aiziet arā no rindas.

Galvenā atšķirība starp steku, rindu un sarakstu ir to secība, ar kādu tiek pievienoti un izņemti elementi.
Stekā pēdējais elements, kas tiek pievienots, ir pirmais, kas būs izņemts. Nevar piekļūt "vidējam" elementam uzreiz, vajadzēs secīgi no pirmā elementa vai pedēja iet.
Rindā pirmais elements, kas tiek pievienots, ir pirmais, kas būs izņemts. Bet rindā var piekļūt jebkūram elementam (iesprausties).
Saraksts glabā elementus pēc kārtas (pēc indeksācijas) un piekļuve notiek pēc konkrēta indeksa.

"""
