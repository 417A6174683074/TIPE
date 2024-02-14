<a name="_page0_x9.91_y-1.00"></a>Simulation de la propagation d’un virus `a l’aide de![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.001.png)

syst`emes multi-agents

Mathurin de Cr´ecy 8 juin 2022

Sommaire![ref1]

1  <a name="_page1_x9.91_y-1.00"></a>[Les mod`eles `a ´equations diff´erentielles ordinaires (EDO) le mod`ele SIR](#_page1_x9.91_y-1.00)

[la variante SEIR](#_page1_x9.91_y-1.00)

2  [Les Syst`emes Multi-Agents (SMA) introduction aux SMA](#_page1_x9.91_y-1.00)

[mes mod`eles](#_page1_x9.91_y-1.00)

3  [Bilan](#_page1_x9.91_y-1.00)

Le<a name="_page2_x9.91_y-1.00"></a> mod`ele SIR![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.003.png) Le mod`ele SIR est le plus c´el`ebre mod`ele ´epidemiologique pouvant pr´edire la propagation d’un virus. Il s’agit d’un mod`ele `a ´equations diff´erentielles dans lequel la population est divis´ee en cat´egories Sains, Inf´ect´es et R´emis. Les ´echanges entre ces cat´egories

sont dSdtdtdI r==´egis−SNβSpaNβrIles ´equations suivantes:

I − γI

dRdt = γI

<a name="_page3_x9.91_y-1.00"></a>D´efinitions![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.004.png)

γ = 1/Tr β = KP R0 = β/γ

Les param`etres γ et β d´esignent respectivements le taux de gu´erison o`u Tr est le temps de gu´erison et le taux de contagion o`u P est la probabilit´e de transmission lors d’un contact et K est le nombre de contact d’une personne lors d’une journ´ee. Enfin, R0 est ce que l’on appel le taux de reproduction de la maladie, il repr´esente le nombre de personnes saines qu’un infect´e vas contaminer en une journ´ee.

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.005.png)

<a name="_page4_x9.91_y-1.00"></a>Etude d’une population de 1200 habitants avec un patient initial sur 200 jours. R0=3 (covid-19 pr´e-confinement), temps de r´emission de 8 jours. Sauf pr´ecision on reprendra ces valeurs dans les autres simulations. L’imunit´e collective intevient lorsque les param`etre N et S conduisent `a

dI ≤ 0 c’est `a dire que Sβ ≤ γ donc, S ≤ Nγ = N . Dans cet exemple, dt N β R0

cela correspond `a S= N , il faut donc que les 2/3 de la population (800

3

personnes) soient contamin´ees avant d’avoir une immunit´ee collective efficace.

Th<a name="_page5_x9.91_y-1.00"></a>´eor`eme du seuil et imunit´e collective![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.006.png)

Etude d’une population de 1200 habitants avec 5 patients initiaux sur 1000 jours. R0=1

Le th´eor`eme du seuil stipule que si R0≤1 alors l’´epidemie ne se propage pas. Ce th´eor`eme peut ˆetre facilement prouv´e `a l’aide d’une ´etude de la fonction r´egissant I sachant que β = γ.

La<a name="_page6_x9.91_y-1.00"></a> variante SEIR![ref1]



 dEdSdtdt == −SNβSNIβ−I αE![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.007.png)

dI = αE − γI − µI  dt

 dRdt = γI

- dFdt = µI

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.008.png) Ici on rajoute une cat´egorie E pour le temps d’incubation de la maladie, le coefficient α correspond `a l’inverse du temps d’incubation. F est la cat´egorie des d´ec`es, µ correspond `a la l´etalit´e de la maladie. ![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]

Les<a name="_page7_x9.91_y-1.00"></a> gestes barri`eres![ref1]

Port du masque du 50`eme au 100`eme jour

 dSdtdt = − SNNβ I

dE = (1−u)Sβ I − αE![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.015.png)

dI = αE − γI − µI

 dRdt = γI



 dt

- dF = µI

dt

Pour rendre compte de l’efficacit´e des gestes barri`eres, on multipli β par un coefficient 1-u o`u u est un param`etre (d´etermin´e exp´erimentalement) repr´esentant l’efficacit´e de cette mesure, ici u=0.2.

<a name="_page8_x9.91_y-1.00"></a>Port du masque tout au long de l’´epid´emie

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.016.png)

On constate que le port du masque tout au long de l’´epid´emie permet deretarder le pic de contamination, mais ne le diminue pas beaucoup.

Les<a name="_page9_x9.91_y-1.00"></a> faiblesses du mod`ele![ref1]

ne rends pas conte des interactions spatiales

ne consid`ere pas les comportements sociaux impossibilit´e de mener une ´etude `a l’´echelle de l’individu

Les<a name="_page10_x9.91_y-1.00"></a> Syst`emes Multi-Agents (SMA)![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.017.jpeg)

Les SMA coordonnent plusieurs entit´es informatiques appel´ees agents qui ont un but, une perception de leur environnement et des autres agents et agissent de concerts. ![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]

A<a name="_page11_x9.91_y-1.00"></a> quoi ¸ca sert?![ref1]

coordination d’entit´es informatiques gestion d’un environnement simulation de ph´enom`enes complexes

L’agent![ref1]

<a name="_page12_x9.91_y-1.00"></a>⟨P, Percept, F, I, S ⟩ Un agent est d´efini par cinq ´el´ements:

P: la fonction de perception

Percept: les cons´equences de l’environnement sur l’agent F: les possibles modifications de l’´etat de l’agent

I: les fonctions qui modifient l’´etat de l’agent

S: les ´etats possibles de l’agent

L’environnement![ref1]

<a name="_page13_x9.91_y-1.00"></a>⟨E, , Σ, R ⟩

Un environnemnt est d´efinie par quatre ´el´ements:

E: l’espace dans lequel les agents ´evolueront

: comment les agents peuvent modifier les ´etats de l’environnement Σ: les ´etats de l’environnement R: la fa¸con dont l’environnement se modifie lui-mˆeme

Les<a name="_page14_x9.91_y-1.00"></a> relations agents-environnement![ref1]

Les fonctions des agents et de l’environnement prennent en arguments les ´etats des agents et de l’environnnement et d´efinissent ainsi leurs ´etats futures. P:Σ → Percept F:S×Percept→S I:S→ Γ R:Σ× Γ→Σ

s(t + 1) = F(s(t) ·P(σ(t)))

Ce qui se r´e´ecrit en

σ(t + 1) = R(σ(t) ·I(s(t)))

s∈S σ ∈Σ

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.018.png)

<a name="_page15_x9.91_y-1.00"></a>Exemple de communication entre deux agents sch´ematiser par un r´eseau de Petri.

La<a name="_page16_x9.91_y-1.00"></a> simulation![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.019.png) repr´esentation d’agents sains (bleu) et d’agents contagieux (rouge) dans un espace ferm´e.

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.020.png)<a name="_page17_x9.91_y-1.00"></a> Les agents se d´eplacent dans l’espace et interagissent, lorsqu’un agent infectieux rencontre un agent sains, il peut le contamin´e, il est alors en phase d’incubation (gris).

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.021.png)<a name="_page18_x9.91_y-1.00"></a> Au bout d’un certain temps, les

agents contamin´es deviennent eux-mˆemes contagieux.

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.022.png)<a name="_page19_x9.91_y-1.00"></a> Au bout du temps de gu´erison,

les agents sont gu´eris (verts).

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.023.png)<a name="_page20_x9.91_y-1.00"></a> La courbe d’´evolution

de la simulation (abscisse en demi-heures).

Simulation<a name="_page21_x9.91_y-1.00"></a> des agents![ref1]

Communaut´e de 1200 habitants sur un dur´ee de 29 jours

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.024.png)

1131 personnes contamin´ees au total, 778 dans un bus, 145 `a l’´ecole, 168 sur le lieu de travail, 39 `a domicile et 8 morts.![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]

Avec<a name="_page22_x9.91_y-1.00"></a> gestes barri`eres![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.025.png)

1078 personnes contamin´ees au total, 657 dans le bus, 166 `a l’´ecole, 212 au travail, 42 `a domicile et 9 morts.

Avec<a name="_page23_x9.91_y-1.00"></a> tests![ref1]

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.026.png)

Les tests commencent au 42eme jour

647 personnes contamin´ees au total, 382 dans le bus, 139 `a l’´ecole, 73 au travail, 52 `a domicile et 2 morts.![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]

Bilan![ref1]

<a name="_page24_x9.91_y-1.00"></a>Avantages![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.027.png)

pr´ecision des informations

adaptabilit´e du mod`ele

´etude des aspects sociaux et spatiaux du probl`eme

permet d’´evaluer l’efficacit´e de protocoles sanitaires pr´ecis et vari´es

Inconv´enients![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.028.png)

la complexit´e du mod`ele croˆıt tr`es vite en fonction de sa pr´ecision, de la population et de la p´eriode ´etudi´ee

temps de calcul

Mathurin de Cr´ecy [Simulation de la propagation d’un virus `a de syst`emes 8multi-agentsjuin 2022 ](#_page45_x9.91_y-1.00)28/47![ref8]![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]
Mo<a name="_page25_x9.91_y-1.00"></a>d`ele SIR![ref1]

Mathurin de Cr´ecy [Simulation de la propagation d’un virus `a de syst`emes 8multi-agentsjuin 2022 ](#_page0_x9.91_y-1.00)29/47![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.030.png)![ref8]![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]
Mo<a name="_page26_x9.91_y-1.00"></a>d`ele SEIR![ref1]

Mathurin de Cr´ecy [Simulation de la propagation d’un virus `a de syst`emes 8multi-agentsjuin 2022 ](#_page0_x9.91_y-1.00)30/47![ref8]![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.031.png)

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.032.png)

<a name="_page27_x9.91_y-1.00"></a>Mathurin de Cr´ecy [Simulation de la propagation d’un virus `a de syst`emes 8multi-agentsjuin 2022 ](#_page0_x9.91_y-1.00)31/47![ref8]![ref2]![ref3]![ref4]![ref5]![ref6]![ref7]

SMA<a name="_page28_x9.91_y-1.00"></a> basique![ref1]





![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.033.png)

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.034.png)

Mo<a name="_page32_x9.91_y-1.00"></a>d`ele complexe![ref1]









![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.035.png)





![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.036.png)

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.037.png)

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.038.png)

![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.039.png)
Mathurin de Cr´ecy [Simulation de la propagation d’un virus `a de syst`emes 8multi-agentsjuin 2022 ](#_page0_x9.91_y-1.00)47/47![ref8]![ref2]![](image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.040.png)![ref3]![ref4]![ref5]![ref6]![ref7]

[ref1]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.002.png
[ref2]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.009.png
[ref3]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.010.png
[ref4]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.011.png
[ref5]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.012.png
[ref6]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.013.png
[ref7]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.014.png
[ref8]: image/Aspose.Words.873a96c5-7823-42c4-b610-f8cd36f4df02.029.png
