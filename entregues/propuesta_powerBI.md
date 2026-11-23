# Proposta Dashboard PowerBI

## A. Anàlisi de Rendiments i Corbes (Per a la Hipòtesi 1 i Regressió Polinomial)
1. Visualització: Gràfic de dispersió (scatter plot) amb una línia de tendència de regressió polinomial de grau 2.

- Eixos: marketing_spend (eix X) vs. sales_units (eix Y).
- Objectiu: Visualitzar si existeix el punt de inflexió o rendiments decreixents a partir del qual gastar més en màrqueting deixa de compensar.

### Explicació:

Títol: Despesa en màrqueting vs. vendes, per canal

A l’ecommerce, les vendes creixen lleugerament amb la despesa i s’aplanen a partir d’uns 4.000-5.000 €, cosa que apunta a rendiments decreixents en aquest canal. A la botiga, en canvi, les vendes creixen amb més força a mesura que augmenta la despesa i no s’observa aplanament. Hi ha molta dispersió, així que cal interpretar-ho amb cautela.

Conclusió per a la hipòtesi 1:

La hipòtesi es compleix només en part: hi ha indicis de rendiments decreixents a l’ecommerce, però no a la botiga.

Dos detalls
Les xifres (4.000-5.000 €, 102-115, 130) són aproximades, llegides del gràfic. Si les poses a l’informe, diga-ho com a “aproximadament”.
Pel que fa a la dispersió, l’aplanament d’ecommerce és suau i els punts estan molt escampats. Millor dir “indicis” i no “demostra”.

## B. Impacte dels Descomptes (Per a la Hipòtesi 2)
2. Visualització: Gràfic de línies o barres agrupades.

- Eixos: avg_discount (trams de descompte) vs. mitjana de sales_units.
- Objectiu: Comprovar si un descompte més elevat incrementa les vendes de manera lineal o si s'estanca, avaluant l'efecte real sobre el volum.

Títol: Descompte vs. vendes mitjanes, per canal

Les vendes mitjanes tendeixen a augmentar amb el descompte, tant a la botiga com a l’ecommerce, però la pujada és irregular: hi ha trams intermedis on les vendes baixen abans de tornar a créixer. L’ecommerce ven més que la botiga amb descomptes baixos i mitjans, i només s’igualen als descomptes més alts.

Conclusió per a la hipòtesi 2:

Un descompte més elevat s’associa amb més vendes, però no de manera lineal ni constant. No s’observa que l’efecte s’estanque, però la irregularitat de la corba aconsella interpretar-ho amb cautela.

## C. Desglossament per Canal, Regió i Línia de Producte (Baseline i Context)
3. Visualització: Gràfic de barres horitzontals o mapa de calor (heatmap).

- Eixos: Combinació de canal $\times$ regió $\times$ línia de producte enfront de les vendes totals (sales_units).
- Objectiu: Mostrar com aquests factors estructurals expliquen gran part de les vendes de base abans d'aïllar l'efecte del màrqueting.

Títol: Vendes totals per canal, línia de producte i regió

Les vendes de base depenen en bona part de l’estructura comercial. L’ecommerce ven més que la botiga, i en tots dos canals la línia urban és la que més ven i electric la que menys. Per regió, metro i coast concentren més vendes que inland. Aquestes diferències existeixen abans de tindre en compte el màrqueting.

Conclusió per a la secció C:

Canal, línia de producte i regió expliquen una part important del volum de vendes de base, per la qual cosa cal tenir-los en compte per aïllar l’efecte real del màrqueting.

## D. Embut de Conversió / Mecanisme del Màrqueting (Per a la Hipòtesi 3)
4. Visualització: Diagrama de dispersió o gràfic de relació multivariable.

- Eixos: marketing_spend vs. website_sessions (color o mida segons sales_units).
- Objectiu: Validar si el màrqueting impacta primer en l'augment de sessions web i com aquestes es tradueixen finalment en vendes, especialment a l'e-commerce.

Títol: Màrqueting, sessions web i vendes, per canal

La despesa en màrqueting s’associa clarament amb més sessions web, tant a l’ecommerce com a la botiga, i la relació és forta i regular. L’ecommerce té molt més trànsit que la botiga per a la mateixa despesa. Les vendes (mida de les boles) tendeixen a ser més altes quan hi ha més sessions, sobretot a l’ecommerce, però aquesta relació és més feble.

Conclusió per a la hipòtesi 3:

Les dades recolzen que el màrqueting actua primer sobre les sessions web, i que estes es tradueixen en vendes, especialment a l’ecommerce, tot i que el pas de sessions a vendes és menys evident que el de màrqueting a sessions.

## E.
Títol: Sessions web vs. vendes, per canal

Les vendes augmenten amb les sessions web tant a l’ecommerce com a la botiga, tot i que amb bastanta dispersió. L’ecommerce acumula molt més trànsit, i és on es donen les vendes més altes. Això indica que l’increment de visites a la web es tradueix, en part, en més vendes.

Hipòtesi 3 completa

Amb el gràfic D i aquest, ja tens el mecanisme sencer:

Les dades recolzen que el màrqueting actua primer sobre les sessions web (relació forta i regular), i que estes es tradueixen en vendes (relació positiva però més dispersa), tant a l’ecommerce com a la botiga.