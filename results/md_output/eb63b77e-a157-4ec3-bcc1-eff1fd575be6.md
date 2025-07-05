Looking  Beyond  Activity  Labels:  Mining  Context-Aware  Resource 
Profiles using Activity Instance Archetypes (Demonstration) 
 
Authors: Gerhardus van Hulzen, Niels Martin, Benoît Depaire 
 
Attribute  Description 
Phase  The phase within the process. Derived from the “concept.name” attribute, where 
the first digit of the last part expresses a phase within the process. A total of nine 
phases are present: Phase 0 – 8 
Resource  he unique identifier of the resource who executed this activity instance, e.g. 
“560462” 
Case Procedure  Either blank (no value), “Regulier” (regular), or “Uitgebreid” (comprehensive) 
Case Status  Either “G” or “O”. We filtered out “T”, because this only applied to two cases 
across all logs 
Weekday  Number indicating the day of the week, starting with “1” for Monday. Derived 
from the timestamp indicating when the activity was completed 
Case Parts  The  category/ies  the  application  relates  to.  Derived  from  the  “(case)  parts” 
attribute and transformed into dummy variables. An activity instance applies to 
at  least  one  category,  but  multiple  categories  could  be  applicable.  Some 
categories were aggregated to limit the number of variables, e.g. everything 
related  to  environment  was  bundled  into  one  dummy.  A  total  of  fourteen 
categories are present, although not every municipality dealt with all categories: 
“Aanleg” (installation), “Bouw” (construction), “Brandveilig” (fireproof), “Flora 
en fauna” (flora and fauna), “Gebiedsbescherming” (area protection), “Handelen 
in  strijd  met  regels  RO”  (acting  in  violation  of  spatial  planning  rules), 
“Inrit/uitweg” (entrance/exit), “Integraal” (integral), “Kap” (tree felling), “Milieu” 
(environment),  “Monument”  (monument),  “Reclame”  (advertisement), 
“Roerende zaken” (movable property), and “Sloop” (demolition) 
 
Amount of clusters: where the BIC bends (no significant improvement anymore) and no cluster should 
be smaller than 5% 
 
Activity instance archetypes: 
-  Phase: add until 70% 
-  Weekday: Monday+Thursday+Friday = “beginning/end of week”, Tuesday+Wednesday = 
“midweek”, Saturday+Sunday = “weekend” 
Specialism: 
-  Either 1 or two activity instance archetypes (>70%, rest < 10%) + at least one group with 50% 
-  All resources in 1 clusters should satisfy 
   

|             | Attribute      |    |                                                                                        | Description                                                                            |    |
|:------------|:---------------|:---|:---------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|:---|
| Phase       | Phase          |    |                                                                                        | The phase within the process. Derived from the “concept.name” attribute, where         |    |
|             |                |    |                                                                                        | the first digit of the last part expresses a phase within the process. A total of nine |    |
|             |                |    |                                                                                        | phases are present: Phase 0 – 8                                                        |    |
| Resource    |                |    | he unique identifier of the resource who executed this activity instance, e.g.         |                                                                                        |    |
|             |                |    | “560462”                                                                               |                                                                                        |    |
|             | Case Procedure |    |                                                                                        | Either blank (no value), “Regulier” (regular), or “Uitgebreid” (comprehensive)         |    |
| Case Status |                |    | Either “G” or “O”. We filtered out “T”, because this only applied to two cases         |                                                                                        |    |
|             |                |    | across all logs                                                                        |                                                                                        |    |
| Weekday     |                |    |                                                                                        | Number indicating the day of the week, starting with “1” for Monday. Derived           |    |
|             |                |    |                                                                                        | from the timestamp indicating when the activity was completed                          |    |
| Case Parts  |                |    | The category/ies the application relates to. Derived from the “(case) parts”           |                                                                                        |    |
|             |                |    | attribute and transformed into dummy variables. An activity instance applies to        |                                                                                        |    |
|             |                |    | at least one category, but multiple categories could be applicable. Some               |                                                                                        |    |
|             |                |    | categories were aggregated to limit the number of variables, e.g. everything           |                                                                                        |    |
|             |                |    | related to environment was bundled into one dummy. A total of fourteen                 |                                                                                        |    |
|             |                |    | categories are present, although not every municipality dealt with all categories:     |                                                                                        |    |
|             |                |    | “Aanleg” (installation), “Bouw” (construction), “Brandveilig” (fireproof), “Flora      |                                                                                        |    |
|             |                |    | en fauna” (flora and fauna), “Gebiedsbescherming” (area protection), “Handelen         |                                                                                        |    |
|             |                |    | in strijd met regels RO” (acting in violation of spatial planning rules),              |                                                                                        |    |
|             |                |    | “Inrit/uitweg” (entrance/exit), “Integraal” (integral), “Kap” (tree felling), “Milieu” |                                                                                        |    |
|             |                |    | (environment), “Monument” (monument), “Reclame” (advertisement),                       |                                                                                        |    |
|             |                |    | “Roerende zaken” (movable property), and “Sloop” (demolition)                          |                                                                                        |    |

Municipality 1 
 
7 clusters: 
 
##   Cluster     n        rel 
## 1       1  4681 0.08966402 
## 2       2  4089 0.07832433 
## 3       3  9369 0.17946213 
## 4       4  9279 0.17773819 
## 5       5 17848 0.34187641 
## 6       6  4225 0.08092940 
## 7       7  2715 0.05200552 
 
##    Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1 phase0 50.89% 31.43% 88.27% 18.89% 35.47% 28.19% 35.56% 
## 2 phase1 12.64% 11.87% 11.35%  2.95%  19.5% 11.62% 18.91% 
## 3 phase2  4.23%  6.03%     0%  1.62% 11.61%  7.65% 10.66% 
## 4 phase3  4.12%     7%     0%  1.44% 13.04%  8.86%   9.2% 
## 5 phase4 13.83% 17.22%     0% 25.73% 18.97% 25.59% 14.83% 
## 6 phase5  7.72% 15.19%  0.02% 46.04%  1.19% 16.28% 10.23% 
## 7 phase6  0.79%     0%     0%  0.05%  0.05%  0.08%     0% 
## 8 phase7  1.82%  3.45%  0.11%  0.93%  0.08%   0.4%  0.52% 
## 9 phase8  3.95%  7.81%  0.25%  2.34%  0.09%  1.33%  0.09% 
 
 
 
 
 

| ## Cluster n rel        |
|:------------------------|
| ## 1 1 4681 0.08966402  |
| ## 2 2 4089 0.07832433  |
| ## 3 3 9369 0.17946213  |
| ## 4 4 9279 0.17773819  |
| ## 5 5 17848 0.34187641 |
| ## 6 6 4225 0.08092940  |
| ## 7 7 2715 0.05200552  |

| ## Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7    |
|:-------------------------------------------------------------|
| ## 1 phase0 50.89% 31.43% 88.27% 18.89% 35.47% 28.19% 35.56% |
| ## 2 phase1 12.64% 11.87% 11.35% 2.95% 19.5% 11.62% 18.91%   |
| ## 3 phase2 4.23% 6.03% 0% 1.62% 11.61% 7.65% 10.66%         |
| ## 4 phase3 4.12% 7% 0% 1.44% 13.04% 8.86% 9.2%              |
| ## 5 phase4 13.83% 17.22% 0% 25.73% 18.97% 25.59% 14.83%     |
| ## 6 phase5 7.72% 15.19% 0.02% 46.04% 1.19% 16.28% 10.23%    |
| ## 7 phase6 0.79% 0% 0% 0.05% 0.05% 0.08% 0%                 |
| ## 8 phase7 1.82% 3.45% 0.11% 0.93% 0.08% 0.4% 0.52%         |
| ## 9 phase8 3.95% 7.81% 0.25% 2.34% 0.09% 1.33% 0.09%        |

##   CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1               35.98%   100% 93.62% 89.41% 96.65% 91.85% 94.32% 
## 2      Regulier     0%     0%  1.55%  3.44%   1.5%  0.88%  2.26% 
## 3    Uitgebreid 64.02%     0%  4.84%  7.15%  1.85%  7.27%  3.42% 
 
##   CaseStatus     X1     X2     X3     X4     X5     X6     X7 
## 1          G 81.21% 89.13% 47.62% 48.29% 50.68% 26.86% 85.43% 
## 2          O 18.79% 10.87% 52.38% 51.71% 49.32% 73.14% 14.57% 
 
##   Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1       1 21.89% 37.13% 34.57% 15.33% 22.43% 21.36% 23.15% 
## 2       2 13.52%  5.23%  8.60% 46.06% 25.89% 34.50% 36.23% 
## 3       3  6.61%  4.99%  4.60% 10.60% 14.94% 13.93% 15.31% 
## 4       4 36.85% 37.62% 40.84%  9.78% 21.32% 10.42% 13.61% 
## 5       5 21.06% 15.01% 10.93% 18.19% 15.38% 19.80% 11.69% 
## 6       6  0.04%  0.00%  0.22%  0.03%  0.03%  0.00%  0.00% 
## 7       7  0.04%  0.02%  0.24%  0.00%  0.00%  0.00%  0.02% 
 
##   Weekday           Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1 Begin/end of week 79.79% 89.76% 86.34% 43.30% 59.13% 51.58% 48.45% 
## 2 Midweek           20.13% 10.21% 13.20% 56.67% 40.83% 48.42% 51.54% 
## 3 Weekend           0.08%  0.02%  0.46%  0.03%  0.04%  0.00%  0.02% 
 
##              CasePart      X1      X2     X3      X4      X5     X6     X7 
## 1              Aanleg   0.00%   1.65%  5.60%   0.39%   0.50% 28.96%  0.00% 
## 2                Bouw  21.24%   0.00% 83.70% 100.00% 100.00% 17.49% 16.38% 
## 3         Brandveilig   0.74%   0.00%  2.96%   2.12%   0.40% 13.12%  0.00% 
## 4          FloraFauna   0.00%   0.00%  0.00%   0.00%   0.00%  0.00%  0.00% 
## 5  Gebiedsbescherming   4.81%   0.00%  0.00%   0.00%   0.00%  0.00%  0.00% 
## 6    HandelenInStrijd   5.40%   0.00% 15.43%   8.43%   7.81% 45.98%  0.49% 
## 7                 Kap   0.24% 100.00%  1.17%   1.24%   0.47%  3.72%  3.18% 
## 8         InritUitweg   0.00%   0.00%  1.54%   0.77%   0.76%  4.95%  0.00% 
## 9              Milieu 100.00%   0.00%  6.04%   5.76%   6.38%  0.84%  0.00% 
## 10           Monument   0.00%   0.00%  4.41%   9.17%   3.91%  3.97%  6.99% 
## 11            Reclame   0.00%   0.00%  1.77%   1.10%   0.85%  6.57%  0.00% 
## 12              Sloop   0.30%   0.00%  4.16%   4.39%   3.04%  0.01% 98.42% 

| ## CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7   |
|:--------------------------------------------------------------------|
| ## 1 35.98% 100% 93.62% 89.41% 96.65% 91.85% 94.32%                 |
| ## 2 Regulier 0% 0% 1.55% 3.44% 1.5% 0.88% 2.26%                    |
| ## 3 Uitgebreid 64.02% 0% 4.84% 7.15% 1.85% 7.27% 3.42%             |

| ## CaseStatus X1 X2 X3 X4 X5 X6 X7                      |
|:--------------------------------------------------------|
| ## 1 G 81.21% 89.13% 47.62% 48.29% 50.68% 26.86% 85.43% |
| ## 2 O 18.79% 10.87% 52.38% 51.71% 49.32% 73.14% 14.57% |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7   |
|:--------------------------------------------------------------|
| ## 1 1 21.89% 37.13% 34.57% 15.33% 22.43% 21.36% 23.15%       |
| ## 2 2 13.52% 5.23% 8.60% 46.06% 25.89% 34.50% 36.23%         |
| ## 3 3 6.61% 4.99% 4.60% 10.60% 14.94% 13.93% 15.31%          |
| ## 4 4 36.85% 37.62% 40.84% 9.78% 21.32% 10.42% 13.61%        |
| ## 5 5 21.06% 15.01% 10.93% 18.19% 15.38% 19.80% 11.69%       |
| ## 6 6 0.04% 0.00% 0.22% 0.03% 0.03% 0.00% 0.00%              |
| ## 7 7 0.04% 0.02% 0.24% 0.00% 0.00% 0.00% 0.02%              |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7             |
|:------------------------------------------------------------------------|
| ## 1 Begin/end of week 79.79% 89.76% 86.34% 43.30% 59.13% 51.58% 48.45% |
| ## 2 Midweek 20.13% 10.21% 13.20% 56.67% 40.83% 48.42% 51.54%           |
| ## 3 Weekend 0.08% 0.02% 0.46% 0.03% 0.04% 0.00% 0.02%                  |

| ## CasePart X1 X2 X3 X4 X5 X6 X7                                  |
|:------------------------------------------------------------------|
| ## 1 Aanleg 0.00% 1.65% 5.60% 0.39% 0.50% 28.96% 0.00%            |
| ## 2 Bouw 21.24% 0.00% 83.70% 100.00% 100.00% 17.49% 16.38%       |
| ## 3 Brandveilig 0.74% 0.00% 2.96% 2.12% 0.40% 13.12% 0.00%       |
| ## 4 FloraFauna 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%         |
| ## 5 Gebiedsbescherming 4.81% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% |
| ## 6 HandelenInStrijd 5.40% 0.00% 15.43% 8.43% 7.81% 45.98% 0.49% |
| ## 7 Kap 0.24% 100.00% 1.17% 1.24% 0.47% 3.72% 3.18%              |
| ## 8 InritUitweg 0.00% 0.00% 1.54% 0.77% 0.76% 4.95% 0.00%        |
| ## 9 Milieu 100.00% 0.00% 6.04% 5.76% 6.38% 0.84% 0.00%           |
| ## 10 Monument 0.00% 0.00% 4.41% 9.17% 3.91% 3.97% 6.99%          |
| ## 11 Reclame 0.00% 0.00% 1.77% 1.10% 0.85% 6.57% 0.00%           |
| ## 12 Sloop 0.30% 0.00% 4.16% 4.39% 3.04% 0.01% 98.42%            |

Activity instance archetypes: 
Clust  Label  Description  Size (%) 
1  Environment  Mainly occur at the beginning/end of the week, more likely  8.97% 
cases  require  a  comprehensive procedure, with  typically a  “G” 
case status 
2  Tree felling cases  Mainly occur at the beginning/end of the week, always have  7.83% 
a “blank” procedure, with typically status “G” 
3  Construction  Mainly occur at the beginning/end of the week, typically  17.95% 
cases in phase 0  have  a  “blank”  procedure,  and  are  evenly  split  between 
status “G” and “O” 
4  Construction  Occur  evenly  across  the  week,  typically  have  a  “blank”  17.77% 
cases in phase 4,5  procedure, and are evenly split between status “G” and “O” 
5  Other  Occur  evenly  across  the  week,  typically  have  a  “blank”  34.19% 
construction  procedure, and are evenly split between status “G” and “O” 
cases 
6  Other cases  Occur  evenly  across  the  week,  typically  have  a  “blank”  8.09% 
procedure with status “O” 
7  Demolition cases  Occur  evenly  across  the  week,  typically  have  a  “blank”  5.20% 
procedure with status “G” 
 
Profiles: 
 
 
 
 

|   Clust | Label              | Description                                                | Size (%)   |
|--------:|:-------------------|:-----------------------------------------------------------|:-----------|
|       1 | Environment        | Mainly occur at the beginning/end of the week, more likely | 8.97%      |
|         | cases              | require a comprehensive procedure, with typically a “G”    |            |
|         |                    | case status                                                |            |
|       2 | Tree felling cases | Mainly occur at the beginning/end of the week, always have | 7.83%      |
|         |                    | a “blank” procedure, with typically status “G”             |            |
|       3 | Construction       | Mainly occur at the beginning/end of the week, typically   | 17.95%     |
|         | cases in phase 0   | have a “blank” procedure, and are evenly split between     |            |
|         |                    | status “G” and “O”                                         |            |
|       4 | Construction       | Occur evenly across the week, typically have a “blank”     | 17.77%     |
|         | cases in phase 4,5 | procedure, and are evenly split between status “G” and “O” |            |
|       5 | Other              | Occur evenly across the week, typically have a “blank”     | 34.19%     |
|         | construction       | procedure, and are evenly split between status “G” and “O” |            |
|         | cases              |                                                            |            |
|       6 | Other cases        | Occur evenly across the week, typically have a “blank”     | 8.09%      |
|         |                    | procedure with status “O”                                  |            |
|       7 | Demolition cases   | Occur evenly across the week, typically have a “blank”     | 5.20%      |
|         |                    | procedure with status “G”                                  |            |

##    Resource Clust1 Clust2  Clust3 Clust4 Clust5 Clust6 Clust7 Archetype 
## 1  10716070  0.00%  0.00%  63.72% 35.85%  0.42%  0.00%  0.00%     3 
## 2  12941730  0.00%  0.00% 100.00%  0.00%  0.00%  0.00%  0.00%     3 
## 3    560925  3.93%  6.26%  81.64%  0.05%  0.12%  0.00%  8.00%     3 
## 4   9264148  2.22% 16.91%  80.87%  0.00%  0.00%  0.00%  0.00%     3 
## 5  11345232  0.00%  0.00%  20.00%  0.00%  0.00% 80.00%  0.00%     6 
## 6   3175153  0.00%  0.00%   0.03%  0.00%  0.00% 99.97%  0.00%     6 
## 7    560999  0.00%  0.00%   0.00%  0.00%  0.00% 99.99%  0.00%     6 
## 8  11744364  0.00%  0.00%   0.00%  0.00% 59.59% 40.41%  0.00%     5 
## 9   1898401  0.00%  0.00%   0.03%  0.00% 99.97%  0.00%  0.00%     5 
## 10  2670601  0.10%  0.33%   0.09%  0.03% 85.21% 13.02%  1.22%     5 
## 11  3273854  0.00%  0.00%   2.08%  0.01% 80.24%  5.43% 12.25%     5 
## 12   560589  0.00%  0.00%   0.00%  2.59% 97.40%  0.00%  0.00%     5 
## 13        6  0.00%  0.00%   0.01%  0.00% 99.99%  0.00%  0.00%     5 
## 14  4936828 99.99%  0.00%   0.01%  0.00%  0.00%  0.00%  0.00%     1 
## 15   560462 94.98%  2.72%   2.30%  0.00%  0.00%  0.00%  0.00%     1 
## 16   560950 98.53%  0.00%   0.00%  1.47%  0.00%  0.00%  0.00%     1 
## 17   560464  0.00%  0.00%  20.20% 22.57% 22.68%  0.00% 34.56%     7,5 
## 18   560881  0.29%  0.54%   0.37%  0.00% 53.19%  2.29% 43.31%     7,5 
## 19   560872 18.03% 29.06%  50.86%  0.00%  0.00%  0.00%  2.05%     2,3,5 
## 20  5726485  0.00% 34.17%   0.00% 12.54% 53.29%  0.00%  0.00%     2,3,5 
## 21   560890  0.17%  0.00%   0.00% 75.95%  0.00% 17.83%  6.06%     4,6 
## 22   560894  0.00%  0.00%   4.77% 44.31%  0.00% 42.38%  8.54%     4,6 
## 23   560912  5.16%  2.94%  18.62% 54.00%  4.71% 12.50%  2.08%     4,6 
 
Specialism: 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Archetype   |
|:-------------------------------------------------------------------------|
| ## 1 10716070 0.00% 0.00% 63.72% 35.85% 0.42% 0.00% 0.00% 3              |
| ## 2 12941730 0.00% 0.00% 100.00% 0.00% 0.00% 0.00% 0.00% 3              |
| ## 3 560925 3.93% 6.26% 81.64% 0.05% 0.12% 0.00% 8.00% 3                 |
| ## 4 9264148 2.22% 16.91% 80.87% 0.00% 0.00% 0.00% 0.00% 3               |
| ## 5 11345232 0.00% 0.00% 20.00% 0.00% 0.00% 80.00% 0.00% 6              |
| ## 6 3175153 0.00% 0.00% 0.03% 0.00% 0.00% 99.97% 0.00% 6                |
| ## 7 560999 0.00% 0.00% 0.00% 0.00% 0.00% 99.99% 0.00% 6                 |
| ## 8 11744364 0.00% 0.00% 0.00% 0.00% 59.59% 40.41% 0.00% 5              |
| ## 9 1898401 0.00% 0.00% 0.03% 0.00% 99.97% 0.00% 0.00% 5                |
| ## 10 2670601 0.10% 0.33% 0.09% 0.03% 85.21% 13.02% 1.22% 5              |
| ## 11 3273854 0.00% 0.00% 2.08% 0.01% 80.24% 5.43% 12.25% 5              |
| ## 12 560589 0.00% 0.00% 0.00% 2.59% 97.40% 0.00% 0.00% 5                |
| ## 13 6 0.00% 0.00% 0.01% 0.00% 99.99% 0.00% 0.00% 5                     |
| ## 14 4936828 99.99% 0.00% 0.01% 0.00% 0.00% 0.00% 0.00% 1               |
| ## 15 560462 94.98% 2.72% 2.30% 0.00% 0.00% 0.00% 0.00% 1                |
| ## 16 560950 98.53% 0.00% 0.00% 1.47% 0.00% 0.00% 0.00% 1                |
| ## 17 560464 0.00% 0.00% 20.20% 22.57% 22.68% 0.00% 34.56% 7,5           |
| ## 18 560881 0.29% 0.54% 0.37% 0.00% 53.19% 2.29% 43.31% 7,5             |
| ## 19 560872 18.03% 29.06% 50.86% 0.00% 0.00% 0.00% 2.05% 2,3,5          |
| ## 20 5726485 0.00% 34.17% 0.00% 12.54% 53.29% 0.00% 0.00% 2,3,5         |
| ## 21 560890 0.17% 0.00% 0.00% 75.95% 0.00% 17.83% 6.06% 4,6             |
| ## 22 560894 0.00% 0.00% 4.77% 44.31% 0.00% 42.38% 8.54% 4,6             |
| ## 23 560912 5.16% 2.94% 18.62% 54.00% 4.71% 12.50% 2.08% 4,6            |

 
 
##    Resource Clust1  Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Specialism 
##  1 12941730 100.00% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  2 560999   99.99%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  3 6        99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  4 4936828  99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  5 1898401  99.97%  0.03%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  6 3175153  99.97%  0.03%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  7 560950   98.53%  1.47%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  8 560589   97.40%  2.59%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  9 560462   94.98%  2.72%  2.30%  0.00%  0.00%  0.00%  0.00%  1          
## 10 2670601  85.21%  13.02% 1.22%  0.33%  0.10%  0.09%  0.03%  1          
## 11 560925   81.64%  8.00%  6.26%  3.93%  0.12%  0.05%  0.00%  1          
## 12 9264148  80.87%  16.91% 2.22%  0.00%  0.00%  0.00%  0.00%  1          
## 13 3273854  80.24%  12.25% 5.43%  2.08%  0.01%  0.00%  0.00%  1          
## 14 11345232 80.00%  20.00% 0.00%  0.00%  0.00%  0.00%  0.00%  1          
## 15 560890   75.95%  17.83% 6.06%  0.17%  0.00%  0.00%  0.00%  1          
## 16 10716070 63.72%  35.85% 0.42%  0.00%  0.00%  0.00%  0.00%  2          
## 17 11744364 59.59%  40.41% 0.00%  0.00%  0.00%  0.00%  0.00%  2          
## 18 560881   53.19%  43.31% 2.29%  0.54%  0.37%  0.29%  0.00%  2          
## 19 5726485  53.29%  34.17% 12.54% 0.00%  0.00%  0.00%  0.00%  3          
## 20 560872   50.86%  29.06% 18.03% 2.05%  0.00%  0.00%  0.00%  3          
## 21 560912   54.00%  18.62% 12.50% 5.16%  4.71%  2.94%  2.08%  4          
## 22 560894   44.31%  42.38% 8.54%  4.77%  0.00%  0.00%  0.00%  5          
## 23 560464   34.56%  22.68% 22.57% 20.20% 0.00%  0.00%  0.00%  6 
 
Specialists: cluster 1+2 (18) 
 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Specialism   |
|:--------------------------------------------------------------------------|
| ## 1 12941730 100.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1               |
| ## 2 560999 99.99% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 3 6 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                       |
| ## 4 4936828 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 5 1898401 99.97% 0.03% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 6 3175153 99.97% 0.03% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 7 560950 98.53% 1.47% 0.00% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 8 560589 97.40% 2.59% 0.00% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 9 560462 94.98% 2.72% 2.30% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 10 2670601 85.21% 13.02% 1.22% 0.33% 0.10% 0.09% 0.03% 1               |
| ## 11 560925 81.64% 8.00% 6.26% 3.93% 0.12% 0.05% 0.00% 1                 |
| ## 12 9264148 80.87% 16.91% 2.22% 0.00% 0.00% 0.00% 0.00% 1               |
| ## 13 3273854 80.24% 12.25% 5.43% 2.08% 0.01% 0.00% 0.00% 1               |
| ## 14 11345232 80.00% 20.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1              |
| ## 15 560890 75.95% 17.83% 6.06% 0.17% 0.00% 0.00% 0.00% 1                |
| ## 16 10716070 63.72% 35.85% 0.42% 0.00% 0.00% 0.00% 0.00% 2              |
| ## 17 11744364 59.59% 40.41% 0.00% 0.00% 0.00% 0.00% 0.00% 2              |
| ## 18 560881 53.19% 43.31% 2.29% 0.54% 0.37% 0.29% 0.00% 2                |
| ## 19 5726485 53.29% 34.17% 12.54% 0.00% 0.00% 0.00% 0.00% 3              |
| ## 20 560872 50.86% 29.06% 18.03% 2.05% 0.00% 0.00% 0.00% 3               |
| ## 21 560912 54.00% 18.62% 12.50% 5.16% 4.71% 2.94% 2.08% 4               |
| ## 22 560894 44.31% 42.38% 8.54% 4.77% 0.00% 0.00% 0.00% 5                |
| ## 23 560464 34.56% 22.68% 22.57% 20.20% 0.00% 0.00% 0.00% 6              |

Combination (Profile – Specialism): 
 
##   Profile Archetypes `1`   `2`   `3`   `4`   `5`   `6` 
## 1 1       3           3     1     0     0     0     0 
## 2 2       6           3     0     0     0     0     0 
## 3 3       5           5     1     0     0     0     0 
## 4 4       1           3     0     0     0     0     0 
## 5 5       7,5         0     1     0     0     0     1 
## 6 6       2,3,5       0     0     2     0     0     0 
## 7 7       4,6         1     0     0     1     1     0 
   

| ## Profile Archetypes `1` `2` `3` `4` `5` `6`   |
|:------------------------------------------------|
| ## 1 1 3 3 1 0 0 0 0                            |
| ## 2 2 6 3 0 0 0 0 0                            |
| ## 3 3 5 5 1 0 0 0 0                            |
| ## 4 4 1 3 0 0 0 0 0                            |
| ## 5 5 7,5 0 1 0 0 0 1                          |
| ## 6 6 2,3,5 0 0 2 0 0 0                        |
| ## 7 7 4,6 1 0 0 1 1 0                          |

Municipality 2 
 
8 clusters: 
 
##   Cluster    n        rel 
## 1       1 8407 0.18954322 
## 2       2 7190 0.16210488 
## 3       3 3778 0.08517834 
## 4       4 3930 0.08860531 
## 5       5 3299 0.07437886 
## 6       6 7418 0.16724534 
## 7       7 2992 0.06745728 
## 8       8 7340 0.16548677 
 
##    Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 
## 1 phase0 45.81% 49.17% 39.29% 33.25% 46.88% 32.33% 37.35% 31.48% 
## 2 phase1 11.22% 12.21% 14.41% 15.97% 11.34%  8.98%  8.59%  8.75% 
## 3 phase2  3.65%  4.65%   7.3% 12.73%  5.04%  6.51%  4.23%  6.38% 
## 4 phase3  3.82%  3.95%  5.98% 12.52%  4.43%  6.56%  4.75%  8.14% 
## 5 phase4 11.62% 14.15%    13% 21.94%  17.2% 16.06% 15.72% 18.57% 
## 6 phase5 15.31%  7.89% 13.77%  2.39%  6.89% 16.98%  17.4% 14.87% 
## 7 phase6  0.22%   1.2%  0.01%  0.02%     2%  0.03%  0.11%  0.06% 
## 8 phase7  2.45%  2.86%  2.17%   0.4%  2.32%  4.62%  3.33%  3.77% 
## 9 phase8   5.9%  3.92%  4.06%  0.78%  3.91%  7.93%   8.5%  7.97% 
 
 
 

| ## Cluster n rel       |
|:-----------------------|
| ## 1 1 8407 0.18954322 |
| ## 2 2 7190 0.16210488 |
| ## 3 3 3778 0.08517834 |
| ## 4 4 3930 0.08860531 |
| ## 5 5 3299 0.07437886 |
| ## 6 6 7418 0.16724534 |
| ## 7 7 2992 0.06745728 |
| ## 8 8 7340 0.16548677 |

| ## Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8    |
|:--------------------------------------------------------------------|
| ## 1 phase0 45.81% 49.17% 39.29% 33.25% 46.88% 32.33% 37.35% 31.48% |
| ## 2 phase1 11.22% 12.21% 14.41% 15.97% 11.34% 8.98% 8.59% 8.75%    |
| ## 3 phase2 3.65% 4.65% 7.3% 12.73% 5.04% 6.51% 4.23% 6.38%         |
| ## 4 phase3 3.82% 3.95% 5.98% 12.52% 4.43% 6.56% 4.75% 8.14%        |
| ## 5 phase4 11.62% 14.15% 13% 21.94% 17.2% 16.06% 15.72% 18.57%     |
| ## 6 phase5 15.31% 7.89% 13.77% 2.39% 6.89% 16.98% 17.4% 14.87%     |
| ## 7 phase6 0.22% 1.2% 0.01% 0.02% 2% 0.03% 0.11% 0.06%             |
| ## 8 phase7 2.45% 2.86% 2.17% 0.4% 2.32% 4.62% 3.33% 3.77%          |
| ## 9 phase8 5.9% 3.92% 4.06% 0.78% 3.91% 7.93% 8.5% 7.97%           |

##   CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 
## 1               81.06% 20.39%   100% 91.93%  0.01% 85.66%    86% 80.93% 
## 2      Regulier  1.25%     0%     0%  7.49%  2.99% 10.85%  2.75% 19.07% 
## 3    Uitgebreid 17.69% 79.61%     0%  0.59%    97%  3.49% 11.24%     0% 
 
##   CaseStatus     X1     X2     X3     X4     X5     X6     X7     X8 
## 1          G 94.79% 90.16% 90.56% 79.79% 88.68% 99.26% 89.02% 99.73% 
## 2          O  5.21%  9.84%  9.44% 20.21% 11.32%  0.74% 10.98%  0.27% 
 
##   Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 
## 1       1 29.07% 35.34% 22.14% 29.14%  13.5%  1.23% 22.91%   2.2% 
## 2       2 10.83% 25.13% 12.36% 26.44% 38.05% 46.63% 31.62% 48.31% 
## 3       3 34.62% 18.49% 29.58% 34.07% 16.65%  5.34% 13.58%  4.94% 
## 4       4  4.44%  8.89% 15.78%  10.3% 28.37% 44.15% 20.33% 39.71% 
## 5       5 20.75% 12.15% 19.92%     0%  3.41%  2.57%  11.3%  4.79% 
## 6       6  0.22%     0%  0.08%  0.02%     0%  0.07%  0.11%     0% 
## 7       7  0.07%     0%  0.15%  0.03%  0.03%  0.01%  0.15%  0.05% 
 
##   Weekday           Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 
## 1 Begin/end of week 54.25% 56.38% 57.84% 39.44% 45.27% 47.95% 54.54% 46.70% 
## 2 Midweek           45.45% 43.62% 41.94% 60.51% 54.69% 51.97% 45.20% 53.25% 
## 3 Weekend           0.30%  0.00%  0.23%  0.05%  0.03%  0.08%  0.26%  0.05% 
 
##              CasePart    X1     X2     X3     X4     X5    X6    X7     X8 
## 1              Aanleg    0%  0.92% 14.14%  3.17%  0.76% 0.21% 4.42%  5.75% 
## 2                Bouw  100% 19.06%  4.24% 95.87% 72.24%  100% 43.1%  2.16% 
## 3         Brandveilig 0.59%     0%  2.29%  0.57% 23.02% 0.18%    0%  1.04% 
## 4  Gebiedsbescherming    0%  6.18%     0%     0%     0%    0%    0%     0% 
## 5    HandelenInStrijd 6.83%  3.64%     0% 18.25% 42.66% 4.18%  100%     0% 
## 6                 Kap    0%     0%  41.5%  0.54%     0%    0%    0% 54.14% 
## 7         InritUitweg 1.35%  0.13%  7.03%  5.71%  0.98% 1.19% 0.05% 28.79% 
## 8              Milieu 6.04%   100%     0%  3.85% 22.39% 5.92%    0%  0.55% 
## 9            Monument 0.18%     0%     0%     0%  3.04%    0%    0%     0% 
## 10            Reclame 0.45%     0%  1.23%  3.15%     0% 1.31%    0%     0% 
## 11              Sloop 3.92%  1.03% 37.43%     0%     0% 5.05%    0% 13.09% 
 
 

| ## CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8   |
|:---------------------------------------------------------------------------|
| ## 1 81.06% 20.39% 100% 91.93% 0.01% 85.66% 86% 80.93%                     |
| ## 2 Regulier 1.25% 0% 0% 7.49% 2.99% 10.85% 2.75% 19.07%                  |
| ## 3 Uitgebreid 17.69% 79.61% 0% 0.59% 97% 3.49% 11.24% 0%                 |

| ## CaseStatus X1 X2 X3 X4 X5 X6 X7 X8                          |
|:---------------------------------------------------------------|
| ## 1 G 94.79% 90.16% 90.56% 79.79% 88.68% 99.26% 89.02% 99.73% |
| ## 2 O 5.21% 9.84% 9.44% 20.21% 11.32% 0.74% 10.98% 0.27%      |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8   |
|:---------------------------------------------------------------------|
| ## 1 1 29.07% 35.34% 22.14% 29.14% 13.5% 1.23% 22.91% 2.2%           |
| ## 2 2 10.83% 25.13% 12.36% 26.44% 38.05% 46.63% 31.62% 48.31%       |
| ## 3 3 34.62% 18.49% 29.58% 34.07% 16.65% 5.34% 13.58% 4.94%         |
| ## 4 4 4.44% 8.89% 15.78% 10.3% 28.37% 44.15% 20.33% 39.71%          |
| ## 5 5 20.75% 12.15% 19.92% 0% 3.41% 2.57% 11.3% 4.79%               |
| ## 6 6 0.22% 0% 0.08% 0.02% 0% 0.07% 0.11% 0%                        |
| ## 7 7 0.07% 0% 0.15% 0.03% 0.03% 0.01% 0.15% 0.05%                  |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8             |
|:-------------------------------------------------------------------------------|
| ## 1 Begin/end of week 54.25% 56.38% 57.84% 39.44% 45.27% 47.95% 54.54% 46.70% |
| ## 2 Midweek 45.45% 43.62% 41.94% 60.51% 54.69% 51.97% 45.20% 53.25%           |
| ## 3 Weekend 0.30% 0.00% 0.23% 0.05% 0.03% 0.08% 0.26% 0.05%                   |

| ## CasePart X1 X2 X3 X4 X5 X6 X7 X8                               |
|:------------------------------------------------------------------|
| ## 1 Aanleg 0% 0.92% 14.14% 3.17% 0.76% 0.21% 4.42% 5.75%         |
| ## 2 Bouw 100% 19.06% 4.24% 95.87% 72.24% 100% 43.1% 2.16%        |
| ## 3 Brandveilig 0.59% 0% 2.29% 0.57% 23.02% 0.18% 0% 1.04%       |
| ## 4 Gebiedsbescherming 0% 6.18% 0% 0% 0% 0% 0% 0%                |
| ## 5 HandelenInStrijd 6.83% 3.64% 0% 18.25% 42.66% 4.18% 100% 0%  |
| ## 6 Kap 0% 0% 41.5% 0.54% 0% 0% 0% 54.14%                        |
| ## 7 InritUitweg 1.35% 0.13% 7.03% 5.71% 0.98% 1.19% 0.05% 28.79% |
| ## 8 Milieu 6.04% 100% 0% 3.85% 22.39% 5.92% 0% 0.55%             |
| ## 9 Monument 0.18% 0% 0% 0% 3.04% 0% 0% 0%                       |
| ## 10 Reclame 0.45% 0% 1.23% 3.15% 0% 1.31% 0% 0%                 |
| ## 11 Sloop 3.92% 1.03% 37.43% 0% 0% 5.05% 0% 13.09%              |

Activity instance archetypes: 
Clust  Label  Description  Size (%) 
1  Construction  Blank  case  procedure,  status  G,  spread  over  week,  not  18.95% 
cases  in  phase  Thursday 
0,4,5 
2  Environment  Comprehensive procedure, status G, spread over week  16.21% 
cases 
3  Tree  felling  and  Blank procedure, status G, spread over week  8.52% 
demolition cases 
4  Construction  Blank procedure, status G, spread over week, not Friday  8.86% 
cases  in  phase 
0,1,4 
5  Construction  Comprehensive procedure, status G, spread over week, not  7.44% 
comprehensive  Friday 
cases 
6  Construction  Blank procedure, status G,  Tuesday and Thursday  16.72% 
cases  in  phase 
0,1,4,5 
7  Act in violation of  Blank procedure, status G, spread over week  6.75% 
spatial  planning 
cases 
8  Other cases  Blank procedure, status G,  Tuesday and Thursday  16.55% 
 
Profiles: 
 

|   Clust | Label               | Description                                              | Size (%)   |
|--------:|:--------------------|:---------------------------------------------------------|:-----------|
|       1 | Construction        | Blank case procedure, status G, spread over week, not    | 18.95%     |
|         | cases in phase      | Thursday                                                 |            |
|         | 0,4,5               |                                                          |            |
|       2 | Environment         | Comprehensive procedure, status G, spread over week      | 16.21%     |
|         | cases               |                                                          |            |
|       3 | Tree felling and    | Blank procedure, status G, spread over week              | 8.52%      |
|         | demolition cases    |                                                          |            |
|       4 | Construction        | Blank procedure, status G, spread over week, not Friday  | 8.86%      |
|         | cases in phase      |                                                          |            |
|         | 0,1,4               |                                                          |            |
|       5 | Construction        | Comprehensive procedure, status G, spread over week, not | 7.44%      |
|         | comprehensive       | Friday                                                   |            |
|         | cases               |                                                          |            |
|       6 | Construction        | Blank procedure, status G, Tuesday and Thursday          | 16.72%     |
|         | cases in phase      |                                                          |            |
|         | 0,1,4,5             |                                                          |            |
|       7 | Act in violation of | Blank procedure, status G, spread over week              | 6.75%      |
|         | spatial planning    |                                                          |            |
|         | cases               |                                                          |            |
|       8 | Other cases         | Blank procedure, status G, Tuesday and Thursday          | 16.55%     |

 
##    Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Archetype 
## 1  20987361  0.00% 99.97%  0.00%  0.00%  0.00%  0.00%  0.02%  0.01%     2 
## 2   4634935  0.22% 98.77%  0.00%  0.00%  0.00%  1.00%  0.00%  0.00%     2 
## 3    560429  0.00% 99.62%  0.00%  0.05%  0.00%  0.27%  0.03%  0.03%     2 
## 4    560598  0.00% 99.96%  0.00%  0.01%  0.00%  0.03%  0.00%  0.00%     2 
## 5  22445896  1.62%  1.24% 19.24% 28.51%  0.00% 22.44% 19.99%  6.95%     3,4,6,7 
## 6    560458 29.26% 16.08% 14.38%  0.00% 10.80% 13.37%  7.58%  8.54%     1,2,3,5,6 
## 7    560519 22.77%  1.75% 10.12% 16.89%  9.31% 21.56% 13.84%  3.76%     1,3,4,6,7 
## 8    560521  1.09%  0.63%  6.03% 75.89% 11.50%  0.00%  2.98%  1.88%     4 
## 9    560528 28.96%  0.00% 11.35%  0.03%  0.00% 59.61%  0.02%  0.02%     1,6 
## 10   560530  0.00%  0.57%  0.00%  0.00%  8.39% 33.46%  3.07% 54.52%     6,8 
## 11   560532 39.70% 37.56% 13.15%  2.73%  1.36%  0.00%  5.51%  0.00%     1,2 
 
Specialism: 
 
 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Archetype   |
|:--------------------------------------------------------------------------------|
| ## 1 20987361 0.00% 99.97% 0.00% 0.00% 0.00% 0.00% 0.02% 0.01% 2                |
| ## 2 4634935 0.22% 98.77% 0.00% 0.00% 0.00% 1.00% 0.00% 0.00% 2                 |
| ## 3 560429 0.00% 99.62% 0.00% 0.05% 0.00% 0.27% 0.03% 0.03% 2                  |
| ## 4 560598 0.00% 99.96% 0.00% 0.01% 0.00% 0.03% 0.00% 0.00% 2                  |
| ## 5 22445896 1.62% 1.24% 19.24% 28.51% 0.00% 22.44% 19.99% 6.95% 3,4,6,7       |
| ## 6 560458 29.26% 16.08% 14.38% 0.00% 10.80% 13.37% 7.58% 8.54% 1,2,3,5,6      |
| ## 7 560519 22.77% 1.75% 10.12% 16.89% 9.31% 21.56% 13.84% 3.76% 1,3,4,6,7      |
| ## 8 560521 1.09% 0.63% 6.03% 75.89% 11.50% 0.00% 2.98% 1.88% 4                 |
| ## 9 560528 28.96% 0.00% 11.35% 0.03% 0.00% 59.61% 0.02% 0.02% 1,6              |
| ## 10 560530 0.00% 0.57% 0.00% 0.00% 8.39% 33.46% 3.07% 54.52% 6,8              |
| ## 11 560532 39.70% 37.56% 13.15% 2.73% 1.36% 0.00% 5.51% 0.00% 1,2             |

 
 
##    Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Specialism 
##  1 20987361 99.97% 0.02%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  2 560598   99.96% 0.03%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  3 560429   99.62% 0.27%  0.05%  0.03%  0.03%  0.00%  0.00%  0.00%  1          
##  4 4634935  98.77% 1.00%  0.22%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  5 560521   75.89% 11.50% 6.03%  2.98%  1.88%  1.09%  0.63%  0.00%  1          
##  6 22445896 28.51% 22.44% 19.99% 19.24% 6.95%  1.62%  1.24%  0.00%  2          
##  7 560458   29.26% 16.08% 14.38% 13.37% 10.80% 8.54%  7.58%  0.00%  3          
##  8 560519   22.77% 21.56% 16.89% 13.84% 10.12% 9.31%  3.76%  1.75%  4          
##  9 560528   59.61% 28.96% 11.35% 0.03%  0.02%  0.02%  0.00%  0.00%  5          
## 10 560530   54.52% 33.46% 8.39%  3.07%  0.57%  0.00%  0.00%  0.00%  5          
## 11 560532   39.70% 37.56% 13.15% 5.51%  2.73%  1.36%  0.00%  0.00%  5 
Specialists: cluster 1 (5) 
 
Combination (Profile – Specialism): 
 
##   Profile Archetypes `1`   `2`   `3`   `4`   `5` 
## 1 1       2           4     0     0     0     0 
## 2 2       3,4,6,7     0     1     0     0     0 
## 3 3       1,2,3,5,6   0     0     1     1     0 
## 4 4       1,3,4,6,7   1     0     0     0     0 
## 5 5       4           0     0     0     0     1 
## 6 6       1,6         0     0     0     0     1 
## 7 7       1,2         0     0     0     0     1 
   

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Specialism   |
|:---------------------------------------------------------------------------------|
| ## 1 20987361 99.97% 0.02% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 2 560598 99.96% 0.03% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                   |
| ## 3 560429 99.62% 0.27% 0.05% 0.03% 0.03% 0.00% 0.00% 0.00% 1                   |
| ## 4 4634935 98.77% 1.00% 0.22% 0.00% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 5 560521 75.89% 11.50% 6.03% 2.98% 1.88% 1.09% 0.63% 0.00% 1                  |
| ## 6 22445896 28.51% 22.44% 19.99% 19.24% 6.95% 1.62% 1.24% 0.00% 2              |
| ## 7 560458 29.26% 16.08% 14.38% 13.37% 10.80% 8.54% 7.58% 0.00% 3               |
| ## 8 560519 22.77% 21.56% 16.89% 13.84% 10.12% 9.31% 3.76% 1.75% 4               |
| ## 9 560528 59.61% 28.96% 11.35% 0.03% 0.02% 0.02% 0.00% 0.00% 5                 |
| ## 10 560530 54.52% 33.46% 8.39% 3.07% 0.57% 0.00% 0.00% 0.00% 5                 |
| ## 11 560532 39.70% 37.56% 13.15% 5.51% 2.73% 1.36% 0.00% 0.00% 5                |

| ## Profile Archetypes `1` `2` `3` `4` `5`   |
|:--------------------------------------------|
| ## 1 1 2 4 0 0 0 0                          |
| ## 2 2 3,4,6,7 0 1 0 0 0                    |
| ## 3 3 1,2,3,5,6 0 0 1 1 0                  |
| ## 4 4 1,3,4,6,7 1 0 0 0 0                  |
| ## 5 5 4 0 0 0 0 1                          |
| ## 6 6 1,6 0 0 0 0 1                        |
| ## 7 7 1,2 0 0 0 0 1                        |

Municipality 3 
 
7 clusters: 
 
##   Cluster     n        rel 
## 1       1  4912 0.08230425 
## 2       2 21903 0.36700122 
## 3       3 11154 0.18689365 
## 4       4 11098 0.18595533 
## 5       5  3503 0.05869540 
## 6       6  3328 0.05576314 
## 7       7  3783 0.06338701 
 
##    Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1 phase0 51.91% 43.83% 43.85% 37.89% 48.75% 44.13% 38.48% 
## 2 phase1 12.24% 16.96%     0% 11.57%  11.3%  14.4% 12.15% 
## 3 phase2  4.64% 10.16%  0.01%  7.31%  6.54%  8.89%  8.29% 
## 4 phase3  4.97% 11.87%  0.07%  8.57%   7.1%  8.82%  8.77% 
## 5 phase4  16.4%  16.3% 18.63% 20.15% 22.41% 16.85% 19.03% 
## 6 phase5  7.67%  0.41% 37.03% 14.28%   3.2%  6.18% 13.28% 
## 7 phase6  0.33%  0.05%  0.02%  0.02%  0.02%  0.03%     0% 
## 8 phase7   0.9%  0.12%  0.04%  0.16%  0.22%  0.19%     0% 
## 9 phase8  0.94%   0.3%  0.34%  0.04%  0.47%  0.51%     0% 
 
##   CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1               37.01% 93.57% 91.82% 95.13% 58.44% 88.26% 95.78% 
## 2      Regulier  6.77%  0.33%  0.36%  4.87%  3.06%  1.41%  4.22% 
## 3    Uitgebreid 56.22%   6.1%  7.82%     0% 38.51% 10.34%     0% 

| ## Cluster n rel        |
|:------------------------|
| ## 1 1 4912 0.08230425  |
| ## 2 2 21903 0.36700122 |
| ## 3 3 11154 0.18689365 |
| ## 4 4 11098 0.18595533 |
| ## 5 5 3503 0.05869540  |
| ## 6 6 3328 0.05576314  |
| ## 7 7 3783 0.06338701  |

| ## Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7    |
|:-------------------------------------------------------------|
| ## 1 phase0 51.91% 43.83% 43.85% 37.89% 48.75% 44.13% 38.48% |
| ## 2 phase1 12.24% 16.96% 0% 11.57% 11.3% 14.4% 12.15%       |
| ## 3 phase2 4.64% 10.16% 0.01% 7.31% 6.54% 8.89% 8.29%       |
| ## 4 phase3 4.97% 11.87% 0.07% 8.57% 7.1% 8.82% 8.77%        |
| ## 5 phase4 16.4% 16.3% 18.63% 20.15% 22.41% 16.85% 19.03%   |
| ## 6 phase5 7.67% 0.41% 37.03% 14.28% 3.2% 6.18% 13.28%      |
| ## 7 phase6 0.33% 0.05% 0.02% 0.02% 0.02% 0.03% 0%           |
| ## 8 phase7 0.9% 0.12% 0.04% 0.16% 0.22% 0.19% 0%            |
| ## 9 phase8 0.94% 0.3% 0.34% 0.04% 0.47% 0.51% 0%            |

| ## CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7   |
|:--------------------------------------------------------------------|
| ## 1 37.01% 93.57% 91.82% 95.13% 58.44% 88.26% 95.78%               |
| ## 2 Regulier 6.77% 0.33% 0.36% 4.87% 3.06% 1.41% 4.22%             |
| ## 3 Uitgebreid 56.22% 6.1% 7.82% 0% 38.51% 10.34% 0%               |

 
##   CaseStatus    X1     X2     X3     X4     X5     X6    X7 
## 1          G 87.6% 97.36% 97.96% 98.28% 91.42% 93.99% 98.7% 
## 2          O 12.4%  2.64%  2.04%  1.72%  8.58%  6.01%  1.3% 
 
##   Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1       1 17.95% 22.33% 17.93% 25.45% 23.69% 19.62% 26.98% 
## 2       2 27.75% 24.88% 19.78% 17.21% 21.89% 24.94% 20.82% 
## 3       3 20.19% 26.57% 24.31% 32.48% 20.61% 23.96% 18.25% 
## 4       4 21.12% 18.55% 19.89% 16.15% 20.33% 22.92% 22.05% 
## 5       5 12.05%  6.91%  16.4%  7.78% 13.17%  7.26% 10.74% 
## 6       6  0.94%  0.73%  1.43%  0.79%  0.31%  1.15%  1.02% 
## 7       7     0%  0.03%  0.27%  0.15%     0%  0.16%  0.14% 
 
##   Weekday           Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 
## 1 Begin/end of week 51.12% 47.79% 54.22% 49.37% 57.19% 49.80% 59.77% 
## 2 Midweek           47.94% 51.46% 44.08% 49.68% 42.50% 48.90% 39.07% 
## 3 Weekend           0.94%  0.76%  1.70%  0.95%  0.31%  1.31%  1.16% 
 
##              CasePart     X1     X2     X3    X4     X5     X6     X7 
## 1              Aanleg     0%  0.36%  0.54% 1.57%  7.06%  3.28%  9.17% 
## 2                Bouw 18.81%   100% 93.52%    0% 58.06% 11.74%  0.72% 
## 3         Brandveilig     0%     0%  0.53%    0%     0% 32.98%     0% 
## 4          FloraFauna  1.89%     0%     0%    0%     0%     0%     0% 
## 5  Gebiedsbescherming  6.52%     0%     0%    0%     0%     0%     0% 
## 6    HandelenInStrijd  1.89% 10.19% 14.85% 0.36% 99.48%     0%     0% 
## 7                 Kap     0%  2.09%  1.61%  100%  0.16%  1.81%  4.42% 
## 8         InritUitweg     0%  5.74%  5.49%    0%   8.5%     0% 79.29% 
## 9              Milieu 93.38%  1.32%  0.98%    0%  3.14%     0%     0% 
## 10           Monument     0%  1.49%  1.57%    0%     0%     0%     0% 
## 11            Reclame     0%  3.96%  4.43%    0%  3.53%  7.52%     0% 
## 12     Roerende Zaken     0%     0%     0%    0%  0.34%     0%     0% 
## 13              Sloop  2.39%  8.31%  5.62% 0.02%  0.41%  45.4%     0% 
 
 
 
 
 
 
 

| ## CaseStatus X1 X2 X3 X4 X5 X6 X7                    |
|:------------------------------------------------------|
| ## 1 G 87.6% 97.36% 97.96% 98.28% 91.42% 93.99% 98.7% |
| ## 2 O 12.4% 2.64% 2.04% 1.72% 8.58% 6.01% 1.3%       |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7   |
|:--------------------------------------------------------------|
| ## 1 1 17.95% 22.33% 17.93% 25.45% 23.69% 19.62% 26.98%       |
| ## 2 2 27.75% 24.88% 19.78% 17.21% 21.89% 24.94% 20.82%       |
| ## 3 3 20.19% 26.57% 24.31% 32.48% 20.61% 23.96% 18.25%       |
| ## 4 4 21.12% 18.55% 19.89% 16.15% 20.33% 22.92% 22.05%       |
| ## 5 5 12.05% 6.91% 16.4% 7.78% 13.17% 7.26% 10.74%           |
| ## 6 6 0.94% 0.73% 1.43% 0.79% 0.31% 1.15% 1.02%              |
| ## 7 7 0% 0.03% 0.27% 0.15% 0% 0.16% 0.14%                    |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7             |
|:------------------------------------------------------------------------|
| ## 1 Begin/end of week 51.12% 47.79% 54.22% 49.37% 57.19% 49.80% 59.77% |
| ## 2 Midweek 47.94% 51.46% 44.08% 49.68% 42.50% 48.90% 39.07%           |
| ## 3 Weekend 0.94% 0.76% 1.70% 0.95% 0.31% 1.31% 1.16%                  |

| ## CasePart X1 X2 X3 X4 X5 X6 X7                             |
|:-------------------------------------------------------------|
| ## 1 Aanleg 0% 0.36% 0.54% 1.57% 7.06% 3.28% 9.17%           |
| ## 2 Bouw 18.81% 100% 93.52% 0% 58.06% 11.74% 0.72%          |
| ## 3 Brandveilig 0% 0% 0.53% 0% 0% 32.98% 0%                 |
| ## 4 FloraFauna 1.89% 0% 0% 0% 0% 0% 0%                      |
| ## 5 Gebiedsbescherming 6.52% 0% 0% 0% 0% 0% 0%              |
| ## 6 HandelenInStrijd 1.89% 10.19% 14.85% 0.36% 99.48% 0% 0% |
| ## 7 Kap 0% 2.09% 1.61% 100% 0.16% 1.81% 4.42%               |
| ## 8 InritUitweg 0% 5.74% 5.49% 0% 8.5% 0% 79.29%            |
| ## 9 Milieu 93.38% 1.32% 0.98% 0% 3.14% 0% 0%                |
| ## 10 Monument 0% 1.49% 1.57% 0% 0% 0% 0%                    |
| ## 11 Reclame 0% 3.96% 4.43% 0% 3.53% 7.52% 0%               |
| ## 12 Roerende Zaken 0% 0% 0% 0% 0.34% 0% 0%                 |
| ## 13 Sloop 2.39% 8.31% 5.62% 0.02% 0.41% 45.4% 0%           |

Clust  Label  Description  Size (%) 
1  Environment  Comprehensive procedure + sometimes blank, status G, spread  8.23% 
cases  over week 
2  Construction  Blank procedure, status G, spread over week, not Friday  36.70% 
cases in phase 
0,1,4 
3  Construction  Blank procedure, status G, spread over week  18.69% 
cases in phase 
0,5 
4  Tree  felling  Blank procedure, status G, spread over week, not Friday  18.60% 
cases 
5  Act in violation  Blank  procedure,  +  sometimes  comprehensive,  status  G,  5.87% 
of  spatial  spread over week 
planning cases 
6  Other cases  Blank procedure, status G, spread over week, not Friday  5.58% 
7  Entrance/exit  Blank procedure, status G, spread over week  6.34% 
cases 
 
Profiles: 
 
 
 

|   Clust | Label            | Description                                                 | Size (%)   |
|--------:|:-----------------|:------------------------------------------------------------|:-----------|
|       1 | Environment      | Comprehensive procedure + sometimes blank, status G, spread | 8.23%      |
|         | cases            | over week                                                   |            |
|       2 | Construction     | Blank procedure, status G, spread over week, not Friday     | 36.70%     |
|         | cases in phase   |                                                             |            |
|         | 0,1,4            |                                                             |            |
|       3 | Construction     | Blank procedure, status G, spread over week                 | 18.69%     |
|         | cases in phase   |                                                             |            |
|         | 0,5              |                                                             |            |
|       4 | Tree felling     | Blank procedure, status G, spread over week, not Friday     | 18.60%     |
|         | cases            |                                                             |            |
|       5 | Act in violation | Blank procedure, + sometimes comprehensive, status G,       | 5.87%      |
|         | of spatial       | spread over week                                            |            |
|         | planning cases   |                                                             |            |
|       6 | Other cases      | Blank procedure, status G, spread over week, not Friday     | 5.58%      |
|       7 | Entrance/exit    | Blank procedure, status G, spread over week                 | 6.34%      |
|         | cases            |                                                             |            |

##    Resource  Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Archetypes 
## 1   2013365   0.00% 78.43%  0.26%  1.78%  8.23%  7.55%  3.76%     2,6 
## 2    560454   0.00% 80.32%  0.00%  0.07%  6.98% 11.05%  1.58%     2,6 
## 3   3069866   0.00%  0.00%  0.00% 99.99%  0.00%  0.00%  0.00%     4 
## 4   3122446   0.00% 58.67%  0.15%  0.00% 21.48%  0.00% 19.70%     2,4,5,7 
## 5    560696   0.73% 42.36%  1.57% 27.72% 13.91%  3.50% 10.21%     2,4,5,7 
## 6   3148844  99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%     1 
## 7   3442724  89.59%  3.46%  3.13%  0.28%  2.95%  0.00%  0.58%     1 
## 8   5025869 100.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%     1 
## 9    560673   2.11%  0.98% 42.06% 40.24%  2.52%  4.85%  7.23%     3,4 
## 10   560741   2.84%  0.82% 53.12% 19.60%  7.44%  5.64% 10.54%     3,4 
## 11   560749  10.22%  1.41% 28.59% 42.15%  3.80%  3.57% 10.25%     3,4 
## 12   560713   0.00%  0.00%  0.00%  0.00% 99.99%  0.00%  0.00%     5 
## 13        6   0.02%  0.74%  0.00%  0.00% 99.22%  0.00%  0.01%     5 
## 14   560922  32.73%  0.00%  0.00% 21.84%  0.00%  0.00% 45.43%     1,4,7 
Specialism: 
 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Archetypes   |
|:--------------------------------------------------------------------------|
| ## 1 2013365 0.00% 78.43% 0.26% 1.78% 8.23% 7.55% 3.76% 2,6               |
| ## 2 560454 0.00% 80.32% 0.00% 0.07% 6.98% 11.05% 1.58% 2,6               |
| ## 3 3069866 0.00% 0.00% 0.00% 99.99% 0.00% 0.00% 0.00% 4                 |
| ## 4 3122446 0.00% 58.67% 0.15% 0.00% 21.48% 0.00% 19.70% 2,4,5,7         |
| ## 5 560696 0.73% 42.36% 1.57% 27.72% 13.91% 3.50% 10.21% 2,4,5,7         |
| ## 6 3148844 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 7 3442724 89.59% 3.46% 3.13% 0.28% 2.95% 0.00% 0.58% 1                 |
| ## 8 5025869 100.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1                |
| ## 9 560673 2.11% 0.98% 42.06% 40.24% 2.52% 4.85% 7.23% 3,4               |
| ## 10 560741 2.84% 0.82% 53.12% 19.60% 7.44% 5.64% 10.54% 3,4             |
| ## 11 560749 10.22% 1.41% 28.59% 42.15% 3.80% 3.57% 10.25% 3,4            |
| ## 12 560713 0.00% 0.00% 0.00% 0.00% 99.99% 0.00% 0.00% 5                 |
| ## 13 6 0.02% 0.74% 0.00% 0.00% 99.22% 0.00% 0.01% 5                      |
| ## 14 560922 32.73% 0.00% 0.00% 21.84% 0.00% 0.00% 45.43% 1,4,7           |

##    Resource Clust1  Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Specialism 
##  1 5025869  100.00% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  2 3069866  99.99%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  3 560713   99.99%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  4 3148844  99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  1          
##  5 6        99.22%  0.74%  0.02%  0.01%  0.00%  0.00%  0.00%  1          
##  6 3442724  89.59%  3.46%  3.13%  2.95%  0.58%  0.28%  0.00%  1          
##  7 560454   80.32%  11.05% 6.98%  1.58%  0.07%  0.00%  0.00%  1          
##  8 2013365  78.43%  8.23%  7.55%  3.76%  1.78%  0.26%  0.00%  1          
##  9 3122446  58.67%  21.48% 19.70% 0.15%  0.00%  0.00%  0.00%  2          
## 10 560922   45.43%  32.73% 21.84% 0.00%  0.00%  0.00%  0.00%  2          
## 11 560741   53.12%  19.60% 10.54% 7.44%  5.64%  2.84%  0.82%  3          
## 12 560696   42.36%  27.72% 13.91% 10.21% 3.50%  1.57%  0.73%  3          
## 13 560749   42.15%  28.59% 10.25% 10.22% 3.80%  3.57%  1.41%  3          
## 14 560673   42.06%  40.24% 7.23%  4.85%  2.52%  2.11%  0.98%  3 
Specialists: cluster 1 (8) 
 
Combination (Profile – Specialism): 
##   Profile Archetypes `1`   `2`   `3` 
## 1 1       2,6         2     0     0 
## 2 2       4           1     0     0 
## 3 3       2,4,5,7     0     1     1 
## 4 4       1           3     0     0 
## 5 5       3,4         0     0     3 
## 6 6       5           2     0     0 
## 7 7       1,4,7       0     1     0 
   

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Specialism   |
|:--------------------------------------------------------------------------|
| ## 1 5025869 100.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1                |
| ## 2 3069866 99.99% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 3 560713 99.99% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 1                  |
| ## 4 3148844 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 1                 |
| ## 5 6 99.22% 0.74% 0.02% 0.01% 0.00% 0.00% 0.00% 1                       |
| ## 6 3442724 89.59% 3.46% 3.13% 2.95% 0.58% 0.28% 0.00% 1                 |
| ## 7 560454 80.32% 11.05% 6.98% 1.58% 0.07% 0.00% 0.00% 1                 |
| ## 8 2013365 78.43% 8.23% 7.55% 3.76% 1.78% 0.26% 0.00% 1                 |
| ## 9 3122446 58.67% 21.48% 19.70% 0.15% 0.00% 0.00% 0.00% 2               |
| ## 10 560922 45.43% 32.73% 21.84% 0.00% 0.00% 0.00% 0.00% 2               |
| ## 11 560741 53.12% 19.60% 10.54% 7.44% 5.64% 2.84% 0.82% 3               |
| ## 12 560696 42.36% 27.72% 13.91% 10.21% 3.50% 1.57% 0.73% 3              |
| ## 13 560749 42.15% 28.59% 10.25% 10.22% 3.80% 3.57% 1.41% 3              |
| ## 14 560673 42.06% 40.24% 7.23% 4.85% 2.52% 2.11% 0.98% 3                |

| ## Profile Archetypes `1` `2` `3`   |
|:------------------------------------|
| ## 1 1 2,6 2 0 0                    |
| ## 2 2 4 1 0 0                      |
| ## 3 3 2,4,5,7 0 1 1                |
| ## 4 4 1 3 0 0                      |
| ## 5 5 3,4 0 0 3                    |
| ## 6 6 5 2 0 0                      |
| ## 7 7 1,4,7 0 1 0                  |

Municipality 4 
 
6 clusters: 
 
 
##   Cluster     n        rel 
## 1       1  2747 0.05808471 
## 2       2  3933 0.08316241 
## 3       3  6781 0.14338274 
## 4       4 15771 0.33347430 
## 5       5  5715 0.12084241 
## 6       6 12346 0.26105343 
 
##    Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 
## 1 phase0 36.92% 52.87% 34.71% 49.35% 41.44%  30.4% 
## 2 phase1 16.53% 10.09%  9.86%  7.07%  9.29% 17.63% 
## 3 phase2 10.54%  4.44%  6.75%   0.3%  5.57% 13.97% 
## 4 phase3   8.7%  4.48%  7.91%  0.01%  6.76% 16.02% 
## 5 phase4 14.52% 16.08% 19.18% 12.78% 18.74% 21.69% 
## 6 phase5 12.43%  7.82% 16.54% 24.11%  13.8%     0% 
## 7 phase6  0.04%  1.04%  0.04%  0.14%  0.23%  0.01% 
## 8 phase7  0.26%   1.5%  2.85%  3.36%  1.97%  0.03% 
## 9 phase8  0.08%  1.68%  2.15%  2.87%   2.2%  0.26% 
 
 
 
 
 

| ## Cluster n rel        |
|:------------------------|
| ## 1 1 2747 0.05808471  |
| ## 2 2 3933 0.08316241  |
| ## 3 3 6781 0.14338274  |
| ## 4 4 15771 0.33347430 |
| ## 5 5 5715 0.12084241  |
| ## 6 6 12346 0.26105343 |

| ## Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6    |
|:------------------------------------------------------|
| ## 1 phase0 36.92% 52.87% 34.71% 49.35% 41.44% 30.4%  |
| ## 2 phase1 16.53% 10.09% 9.86% 7.07% 9.29% 17.63%    |
| ## 3 phase2 10.54% 4.44% 6.75% 0.3% 5.57% 13.97%      |
| ## 4 phase3 8.7% 4.48% 7.91% 0.01% 6.76% 16.02%       |
| ## 5 phase4 14.52% 16.08% 19.18% 12.78% 18.74% 21.69% |
| ## 6 phase5 12.43% 7.82% 16.54% 24.11% 13.8% 0%       |
| ## 7 phase6 0.04% 1.04% 0.04% 0.14% 0.23% 0.01%       |
| ## 8 phase7 0.26% 1.5% 2.85% 3.36% 1.97% 0.03%        |
| ## 9 phase8 0.08% 1.68% 2.15% 2.87% 2.2% 0.26%        |

##   CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 
## 1                96.8% 19.91%   100% 89.81% 84.28% 91.65% 
## 2      Regulier   3.2%     0%     0%     0%  2.45%     0% 
## 3    Uitgebreid     0% 80.09%     0% 10.19% 13.27%  8.35% 
 
##   CaseStatus     X1     X2     X3     X4     X5     X6 
## 1          G 71.32% 47.94% 94.12% 45.52% 25.72% 43.66% 
## 2          O 28.68% 52.06%  5.88% 54.48% 74.28% 56.34% 
 
##   Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 
## 1       1 24.06% 16.53% 14.58% 17.64% 16.77% 15.79% 
## 2       2 29.97% 29.29% 29.58% 21.39% 21.26% 25.46% 
## 3       3 16.46% 15.04% 19.74%  23.4% 23.19% 24.39% 
## 4       4 19.17%  23.1% 20.35% 20.71% 16.82% 19.69% 
## 5       5 10.34% 15.78% 15.65% 16.69% 21.83% 14.67% 
## 6       6     0%  0.25%  0.03%  0.09%  0.09%  0.01% 
## 7       7     0%     0%  0.07%  0.09%  0.05%     0% 
 
##   Weekday           Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 
## 1 Begin/end of week 53.57% 55.41% 50.58% 55.04% 55.42% 50.14% 
## 2 Midweek           46.43% 44.34% 49.32% 44.78% 44.44% 49.85% 
## 3 Weekend           0.00%  0.25%  0.10%  0.18%  0.14%  0.01% 
 
##              CasePart     X1     X2    X3     X4     X5     X6 
## 1              Aanleg     0%     0% 0.41%  0.41%  9.76%  0.42% 
## 2                Bouw  2.59% 27.28%  0.5% 99.95%  1.96%   100% 
## 3         Brandveilig     0%  7.13%    0%     0%     0%     0% 
## 4  Gebiedsbescherming     0%  3.49%    0%     0%     0%     0% 
## 5    HandelenInStrijd     0%  3.12%    0% 17.22% 87.51% 16.66% 
## 6                 Kap     0%     0%  100%  0.26%  0.44%  0.33% 
## 7         InritUitweg 10.81%     0%    0%  1.83%     0%  1.33% 
## 8              Milieu  1.59% 86.21%    0%  1.98%     0%  3.67% 
## 9            Monument     0%  1.37%    0%     2%  2.72%  2.44% 
## 10            Reclame  2.03%     0%    0%   0.4%     0%  0.42% 
## 11              Sloop 80.43%  2.85%    0%  2.82%  0.85%  3.78% 
 

| ## CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6   |
|:-------------------------------------------------------------|
| ## 1 96.8% 19.91% 100% 89.81% 84.28% 91.65%                  |
| ## 2 Regulier 3.2% 0% 0% 0% 2.45% 0%                         |
| ## 3 Uitgebreid 0% 80.09% 0% 10.19% 13.27% 8.35%             |

| ## CaseStatus X1 X2 X3 X4 X5 X6                  |
|:-------------------------------------------------|
| ## 1 G 71.32% 47.94% 94.12% 45.52% 25.72% 43.66% |
| ## 2 O 28.68% 52.06% 5.88% 54.48% 74.28% 56.34%  |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6   |
|:-------------------------------------------------------|
| ## 1 1 24.06% 16.53% 14.58% 17.64% 16.77% 15.79%       |
| ## 2 2 29.97% 29.29% 29.58% 21.39% 21.26% 25.46%       |
| ## 3 3 16.46% 15.04% 19.74% 23.4% 23.19% 24.39%        |
| ## 4 4 19.17% 23.1% 20.35% 20.71% 16.82% 19.69%        |
| ## 5 5 10.34% 15.78% 15.65% 16.69% 21.83% 14.67%       |
| ## 6 6 0% 0.25% 0.03% 0.09% 0.09% 0.01%                |
| ## 7 7 0% 0% 0.07% 0.09% 0.05% 0%                      |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6             |
|:-----------------------------------------------------------------|
| ## 1 Begin/end of week 53.57% 55.41% 50.58% 55.04% 55.42% 50.14% |
| ## 2 Midweek 46.43% 44.34% 49.32% 44.78% 44.44% 49.85%           |
| ## 3 Weekend 0.00% 0.25% 0.10% 0.18% 0.14% 0.01%                 |

| ## CasePart X1 X2 X3 X4 X5 X6                          |
|:-------------------------------------------------------|
| ## 1 Aanleg 0% 0% 0.41% 0.41% 9.76% 0.42%              |
| ## 2 Bouw 2.59% 27.28% 0.5% 99.95% 1.96% 100%          |
| ## 3 Brandveilig 0% 7.13% 0% 0% 0% 0%                  |
| ## 4 Gebiedsbescherming 0% 3.49% 0% 0% 0% 0%           |
| ## 5 HandelenInStrijd 0% 3.12% 0% 17.22% 87.51% 16.66% |
| ## 6 Kap 0% 0% 100% 0.26% 0.44% 0.33%                  |
| ## 7 InritUitweg 10.81% 0% 0% 1.83% 0% 1.33%           |
| ## 8 Milieu 1.59% 86.21% 0% 1.98% 0% 3.67%             |
| ## 9 Monument 0% 1.37% 0% 2% 2.72% 2.44%               |
| ## 10 Reclame 2.03% 0% 0% 0.4% 0% 0.42%                |
| ## 11 Sloop 80.43% 2.85% 0% 2.82% 0.85% 3.78%          |

Clust  Label  Description  Size (%) 
1  Demolition  Blank procedure, status G, spread over week  5.81% 
cases 
2  Environment  Comprehensive procedure, spread over week  8.32% 
cases 
3  Tree  felling  Blank procedure, status G, spread over week  14.34% 
cases 
4  Construction  Blank procedure, spread over week  33.35% 
cases in phase 
0,5 
5  Act in violation  Blank procedure, status O, spread over week  12.08% 
of  spatial 
planning cases 
6  Other  Blank procedure, spread over week  26.11% 
construction 
cases 
 
Profiles: 
 
 
 

|   Clust | Label            | Description                                 | Size (%)   |
|--------:|:-----------------|:--------------------------------------------|:-----------|
|       1 | Demolition       | Blank procedure, status G, spread over week | 5.81%      |
|         | cases            |                                             |            |
|       2 | Environment      | Comprehensive procedure, spread over week   | 8.32%      |
|         | cases            |                                             |            |
|       3 | Tree felling     | Blank procedure, status G, spread over week | 14.34%     |
|         | cases            |                                             |            |
|       4 | Construction     | Blank procedure, spread over week           | 33.35%     |
|         | cases in phase   |                                             |            |
|         | 0,5              |                                             |            |
|       5 | Act in violation | Blank procedure, status O, spread over week | 12.08%     |
|         | of spatial       |                                             |            |
|         | planning cases   |                                             |            |
|       6 | Other            | Blank procedure, spread over week           | 26.11%     |
|         | construction     |                                             |            |
|         | cases            |                                             |            |

##    Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Archetypes 
## 1   1550894  0.61%  2.12%  0.08%  6.02% 17.12% 74.05%     6 
## 2    560852  0.00%  0.00%  0.00%  1.25% 14.68% 84.06%     6 
## 3         6  0.00%  0.00%  0.00%  0.00%  1.09% 98.91%     6 
## 4    560431 76.49%  0.00%  0.00%  0.00%  0.08% 23.43%     1,2 
## 5    560821 35.60% 34.58%  4.63% 17.09%  4.26%  3.83%     1,2 
## 6    560849 54.49% 45.50%  0.00%  0.00%  0.01%  0.00%     1,2 
## 7    560752  4.96% 17.24% 13.39% 51.82% 11.16%  1.43%     3,4,5 
## 8    560781  2.64%  2.06% 27.52% 53.14% 12.96%  1.68%     3,4,5 
## 9    560796  0.00% 99.79%  0.00%  0.00%  0.21%  0.00%     2 
## 10   560812  5.83%  0.00% 94.17%  0.00%  0.01%  0.00%     3 
Specialism: 
 
 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Archetypes   |
|:-------------------------------------------------------------------|
| ## 1 1550894 0.61% 2.12% 0.08% 6.02% 17.12% 74.05% 6               |
| ## 2 560852 0.00% 0.00% 0.00% 1.25% 14.68% 84.06% 6                |
| ## 3 6 0.00% 0.00% 0.00% 0.00% 1.09% 98.91% 6                      |
| ## 4 560431 76.49% 0.00% 0.00% 0.00% 0.08% 23.43% 1,2              |
| ## 5 560821 35.60% 34.58% 4.63% 17.09% 4.26% 3.83% 1,2             |
| ## 6 560849 54.49% 45.50% 0.00% 0.00% 0.01% 0.00% 1,2              |
| ## 7 560752 4.96% 17.24% 13.39% 51.82% 11.16% 1.43% 3,4,5          |
| ## 8 560781 2.64% 2.06% 27.52% 53.14% 12.96% 1.68% 3,4,5           |
| ## 9 560796 0.00% 99.79% 0.00% 0.00% 0.21% 0.00% 2                 |
| ## 10 560812 5.83% 0.00% 94.17% 0.00% 0.01% 0.00% 3                |

##    Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Specialism 
##  1 560852   84.06% 14.68% 1.25%  0.00%  0.00%  0.00%  1          
##  2 560431   76.49% 23.43% 0.08%  0.00%  0.00%  0.00%  1          
##  3 1550894  74.05% 17.12% 6.02%  2.12%  0.61%  0.08%  1          
##  4 560752   51.82% 17.24% 13.39% 11.16% 4.96%  1.43%  2          
##  5 560781   53.14% 27.52% 12.96% 2.64%  2.06%  1.68%  3          
##  6 560796   99.79% 0.21%  0.00%  0.00%  0.00%  0.00%  4          
##  7 6        98.91% 1.09%  0.00%  0.00%  0.00%  0.00%  4          
##  8 560812   94.17% 5.83%  0.01%  0.00%  0.00%  0.00%  4          
##  9 560821   35.60% 34.58% 17.09% 4.63%  4.26%  3.83%  5          
## 10 560849   54.49% 45.50% 0.01%  0.00%  0.00%  0.00%  6 
Specialists: clusters 1+4+6 (7) 
 
Combination (Profile – Specialism): 
##   Profile Archetypes `1`   `2`   `3`   `4`   `5`   `6` 
## 1 1       6           2     0     0     1     0     0 
## 2 2       1,2         1     0     0     0     1     1 
## 3 3       3,4,5       0     1     1     0     0     0 
## 4 4       2           0     0     0     1     0     0 
## 5 5       3           0     0     0     1     0     0 
 
 
   

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Specialism   |
|:-------------------------------------------------------------------|
| ## 1 560852 84.06% 14.68% 1.25% 0.00% 0.00% 0.00% 1                |
| ## 2 560431 76.49% 23.43% 0.08% 0.00% 0.00% 0.00% 1                |
| ## 3 1550894 74.05% 17.12% 6.02% 2.12% 0.61% 0.08% 1               |
| ## 4 560752 51.82% 17.24% 13.39% 11.16% 4.96% 1.43% 2              |
| ## 5 560781 53.14% 27.52% 12.96% 2.64% 2.06% 1.68% 3               |
| ## 6 560796 99.79% 0.21% 0.00% 0.00% 0.00% 0.00% 4                 |
| ## 7 6 98.91% 1.09% 0.00% 0.00% 0.00% 0.00% 4                      |
| ## 8 560812 94.17% 5.83% 0.01% 0.00% 0.00% 0.00% 4                 |
| ## 9 560821 35.60% 34.58% 17.09% 4.63% 4.26% 3.83% 5               |
| ## 10 560849 54.49% 45.50% 0.01% 0.00% 0.00% 0.00% 6               |

| ## Profile Archetypes `1` `2` `3` `4` `5` `6`   |
|:------------------------------------------------|
| ## 1 1 6 2 0 0 1 0 0                            |
| ## 2 2 1,2 1 0 0 0 1 1                          |
| ## 3 3 3,4,5 0 1 1 0 0 0                        |
| ## 4 4 2 0 0 0 1 0 0                            |
| ## 5 5 3 0 0 0 1 0 0                            |

Municipality 5 
 
9 clusters => 10 clusters would go under 5% cluster size 
 
 
##   Cluster     n        rel 
## 1       1  3519 0.05961477 
## 2       2  3467 0.05873384 
## 3       3 11151 0.18890715 
## 4       4  3073 0.05205916 
## 5       5  3946 0.06684850 
## 6       6 21786 0.36907283 
## 7       7  3330 0.05641295 
## 8       8  5681 0.09624083 
## 9       9  3076 0.05210998 
 
##    Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9 
## 1 phase0 36.81% 34.39% 32.63% 44.28% 51.59% 31.97% 35.85% 70.98% 55.19% 
## 2 phase1 25.93%     0%  1.84% 17.84% 12.14% 23.05% 11.77%  0.29%  9.62% 
## 3 phase2 12.23%     0%  0.25%   8.7%  4.73% 11.85%  6.75%     0%   3.3% 
## 4 phase3 10.18%  0.01%   0.3% 10.05%   4.7% 12.36%  7.06%     0%  2.82% 
## 5 phase4  12.8%  12.7%    16% 14.72% 13.87% 17.47% 16.64%  5.23% 17.96% 
## 6 phase5  0.78% 34.32% 36.71%  1.87%  5.95%  0.21% 14.04%  10.3% 10.21% 
## 7 phase6     0%  0.77%     0%  0.16%  0.71%  0.04%  0.17%  0.15%  0.07% 
## 8 phase7  0.37% 11.43%  3.53%  0.53%  1.85%  0.35%  2.75%   6.8%  0.09% 
## 9 phase8   0.9%  6.38%  8.75%  1.87%  4.46%  2.71%  4.97%  6.25%  0.75% 

| ## Cluster n rel        |
|:------------------------|
| ## 1 1 3519 0.05961477  |
| ## 2 2 3467 0.05873384  |
| ## 3 3 11151 0.18890715 |
| ## 4 4 3073 0.05205916  |
| ## 5 5 3946 0.06684850  |
| ## 6 6 21786 0.36907283 |
| ## 7 7 3330 0.05641295  |
| ## 8 8 5681 0.09624083  |
| ## 9 9 3076 0.05210998  |

| ## Phase Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9    |
|:---------------------------------------------------------------------------|
| ## 1 phase0 36.81% 34.39% 32.63% 44.28% 51.59% 31.97% 35.85% 70.98% 55.19% |
| ## 2 phase1 25.93% 0% 1.84% 17.84% 12.14% 23.05% 11.77% 0.29% 9.62%        |
| ## 3 phase2 12.23% 0% 0.25% 8.7% 4.73% 11.85% 6.75% 0% 3.3%                |
| ## 4 phase3 10.18% 0.01% 0.3% 10.05% 4.7% 12.36% 7.06% 0% 2.82%            |
| ## 5 phase4 12.8% 12.7% 16% 14.72% 13.87% 17.47% 16.64% 5.23% 17.96%       |
| ## 6 phase5 0.78% 34.32% 36.71% 1.87% 5.95% 0.21% 14.04% 10.3% 10.21%      |
| ## 7 phase6 0% 0.77% 0% 0.16% 0.71% 0.04% 0.17% 0.15% 0.07%                |
| ## 8 phase7 0.37% 11.43% 3.53% 0.53% 1.85% 0.35% 2.75% 6.8% 0.09%          |
| ## 9 phase8 0.9% 6.38% 8.75% 1.87% 4.46% 2.71% 4.97% 6.25% 0.75%           |

 
##   CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9 
## 1                97.6%    93% 98.02% 83.18%  26.3% 97.58%   100% 94.36% 61.72% 
## 2      Regulier  0.93%  0.79%  0.72%  3.11%  5.48%  0.91%     0%  0.62%  6.11% 
## 3    Uitgebreid  1.47%  6.21%  1.26%  13.7% 68.22%  1.52%     0%  5.02% 32.16% 
 
##   CaseStatus   X1   X2     X3     X4     X5     X6     X7     X8     X9 
## 1          G 100% 100% 94.76% 96.35% 89.39% 95.77% 90.44% 99.78% 39.35% 
## 2          O   0%   0%  5.24%  3.65% 10.61%  4.23%  9.56%  0.22% 60.65% 
 
##   Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9 
## 1       1 21.26%  14.4% 23.32% 20.73% 18.62% 19.13%    21% 12.92% 16.89% 
## 2       2 18.09% 25.42% 19.44% 24.44% 20.99% 19.94% 24.48% 38.37% 24.39% 
## 3       3 22.22% 30.38% 33.38% 20.45% 27.69% 26.09% 22.57%  3.66% 22.59% 
## 4       4 24.43% 21.23% 21.46% 19.63% 28.07% 20.46% 22.89% 20.11% 24.85% 
## 5       5    14%   8.4%  2.24% 14.72%   4.6% 14.37%  8.94% 24.65% 11.17% 
## 6       6     0%  0.13%  0.07%  0.03%  0.03%     0%  0.06%  0.18%  0.01% 
## 7       7     0%  0.04%  0.09%     0%     0%     0%  0.06%  0.11%  0.11% 
 
##   Weekday           Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9 
## 1 Begin/end of week 59.69% 44.02% 47.02% 55.07% 51.30% 53.96% 52.83% 57.67% 52.90% 
## 2 Midweek           40.31% 55.80% 52.82% 44.89% 48.68% 46.04% 47.05% 42.03% 46.97% 
## 3 Weekend           0.00%  0.17%  0.15%  0.03%  0.03%  0.00%  0.12%  0.29%  0.13% 
 
##              CasePart     X1     X2     X3     X4     X5     X6    X7     X8     X9 
## 1              Aanleg  1.15%  9.77%     0%  25.3%  5.14%     0% 1.43%     0% 12.19% 
## 2                Bouw 48.09% 43.13%   100%  0.57% 31.35%   100%    0%   100% 67.98% 
## 3         Brandveilig   2.2%  7.04%     0% 24.93%   0.9%  0.43%    0%     0%  7.74% 
## 4          FloraFauna  7.27%  0.89%     0%     0%     0%     0%    0%     0%     0% 
## 5  Gebiedsbescherming  0.77%  0.32%     0%     0%  1.82%     0%    0%     0%     0% 
## 6    HandelenInStrijd 15.62%  33.8% 14.03% 42.79% 15.02% 18.53%    0% 19.73% 61.95% 
## 7                 Kap  6.88%  4.27%  0.16%     0%  0.12%  0.45%  100%  0.49%  0.75% 
## 8         InritUitweg     1%  2.53%  1.29%   3.1%     0%  1.53% 1.33%  1.23%     0% 
## 9           Integraal  4.71%     0%     0%     0%     0%     0%    0%   0.2%     0% 
## 10             Milieu 10.03%  8.12%  3.35%     0%   100%  5.24%    0%  6.76%  2.61% 
## 11           Monument  5.58%  2.28%  2.47%     0%     0%  2.14%    0%  2.95%     1% 
## 12            Reclame     0%  1.69%  1.52%  4.97%     0%  1.52%    0%  1.61%  5.85% 
## 13     Roerende Zaken     0%     0%     0%     0%     0%     0%    0%     0%  1.06% 
## 14              Sloop 87.17% 35.44%     0%     0%  2.94%     0%    0%  0.79%     0% 

| ## CaseProcedure Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9   |
|:----------------------------------------------------------------------------------|
| ## 1 97.6% 93% 98.02% 83.18% 26.3% 97.58% 100% 94.36% 61.72%                      |
| ## 2 Regulier 0.93% 0.79% 0.72% 3.11% 5.48% 0.91% 0% 0.62% 6.11%                  |
| ## 3 Uitgebreid 1.47% 6.21% 1.26% 13.7% 68.22% 1.52% 0% 5.02% 32.16%              |

| ## CaseStatus X1 X2 X3 X4 X5 X6 X7 X8 X9                          |
|:------------------------------------------------------------------|
| ## 1 G 100% 100% 94.76% 96.35% 89.39% 95.77% 90.44% 99.78% 39.35% |
| ## 2 O 0% 0% 5.24% 3.65% 10.61% 4.23% 9.56% 0.22% 60.65%          |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9   |
|:----------------------------------------------------------------------------|
| ## 1 1 21.26% 14.4% 23.32% 20.73% 18.62% 19.13% 21% 12.92% 16.89%           |
| ## 2 2 18.09% 25.42% 19.44% 24.44% 20.99% 19.94% 24.48% 38.37% 24.39%       |
| ## 3 3 22.22% 30.38% 33.38% 20.45% 27.69% 26.09% 22.57% 3.66% 22.59%        |
| ## 4 4 24.43% 21.23% 21.46% 19.63% 28.07% 20.46% 22.89% 20.11% 24.85%       |
| ## 5 5 14% 8.4% 2.24% 14.72% 4.6% 14.37% 8.94% 24.65% 11.17%                |
| ## 6 6 0% 0.13% 0.07% 0.03% 0.03% 0% 0.06% 0.18% 0.01%                      |
| ## 7 7 0% 0.04% 0.09% 0% 0% 0% 0.06% 0.11% 0.11%                            |

| ## Weekday Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8 Comp.9             |
|:--------------------------------------------------------------------------------------|
| ## 1 Begin/end of week 59.69% 44.02% 47.02% 55.07% 51.30% 53.96% 52.83% 57.67% 52.90% |
| ## 2 Midweek 40.31% 55.80% 52.82% 44.89% 48.68% 46.04% 47.05% 42.03% 46.97%           |
| ## 3 Weekend 0.00% 0.17% 0.15% 0.03% 0.03% 0.00% 0.12% 0.29% 0.13%                    |

| ## CasePart X1 X2 X3 X4 X5 X6 X7 X8 X9                                          |
|:--------------------------------------------------------------------------------|
| ## 1 Aanleg 1.15% 9.77% 0% 25.3% 5.14% 0% 1.43% 0% 12.19%                       |
| ## 2 Bouw 48.09% 43.13% 100% 0.57% 31.35% 100% 0% 100% 67.98%                   |
| ## 3 Brandveilig 2.2% 7.04% 0% 24.93% 0.9% 0.43% 0% 0% 7.74%                    |
| ## 4 FloraFauna 7.27% 0.89% 0% 0% 0% 0% 0% 0% 0%                                |
| ## 5 Gebiedsbescherming 0.77% 0.32% 0% 0% 1.82% 0% 0% 0% 0%                     |
| ## 6 HandelenInStrijd 15.62% 33.8% 14.03% 42.79% 15.02% 18.53% 0% 19.73% 61.95% |
| ## 7 Kap 6.88% 4.27% 0.16% 0% 0.12% 0.45% 100% 0.49% 0.75%                      |
| ## 8 InritUitweg 1% 2.53% 1.29% 3.1% 0% 1.53% 1.33% 1.23% 0%                    |
| ## 9 Integraal 4.71% 0% 0% 0% 0% 0% 0% 0.2% 0%                                  |
| ## 10 Milieu 10.03% 8.12% 3.35% 0% 100% 5.24% 0% 6.76% 2.61%                    |
| ## 11 Monument 5.58% 2.28% 2.47% 0% 0% 2.14% 0% 2.95% 1%                        |
| ## 12 Reclame 0% 1.69% 1.52% 4.97% 0% 1.52% 0% 1.61% 5.85%                      |
| ## 13 Roerende Zaken 0% 0% 0% 0% 0% 0% 0% 0% 1.06%                              |
| ## 14 Sloop 87.17% 35.44% 0% 0% 2.94% 0% 0% 0.79% 0%                            |

Clust  Label  Description  Size (%) 
1  Demolition  Blank procedure, status G, spread over week  5.96% 
cases 
2  Other cases in  Blank procedure, status G, spread over week, less likely Friday  5.87% 
phase 0,5,7 
3  Construction  Blank procedure, status G, spread over week, not Friday  18.89% 
cases in phase 
0,5 
4  Other cases in  Blank procedure, status G, spread over week  5.21% 
phase 0,1,4 
5  Environment  Comprehensive  procedure,  status  G,  spread over week,  not  6.68% 
cases  Friday 
6  Construction  Blank procedure, status G, spread over week  36.91% 
cases in phase 
0,1,4 
7  Tree  felling  Blank procedure, status G, spread over week, less likely Friday  5.64% 
cases 
8  Construction  Blank procedure, status G, spread over week, not Wednesday  9.62% 
cases in phase 
0 
9  Other cases in  Blank procedure + sometimes comprehensive procedure, more  5.21% 
phase 0,4  likely status O, spread over week 
 
Profiles: 
 
 

|   Clust | Label          | Description                                                     | Size (%)   |
|--------:|:---------------|:----------------------------------------------------------------|:-----------|
|       1 | Demolition     | Blank procedure, status G, spread over week                     | 5.96%      |
|         | cases          |                                                                 |            |
|       2 | Other cases in | Blank procedure, status G, spread over week, less likely Friday | 5.87%      |
|         | phase 0,5,7    |                                                                 |            |
|       3 | Construction   | Blank procedure, status G, spread over week, not Friday         | 18.89%     |
|         | cases in phase |                                                                 |            |
|         | 0,5            |                                                                 |            |
|       4 | Other cases in | Blank procedure, status G, spread over week                     | 5.21%      |
|         | phase 0,1,4    |                                                                 |            |
|       5 | Environment    | Comprehensive procedure, status G, spread over week, not        | 6.68%      |
|         | cases          | Friday                                                          |            |
|       6 | Construction   | Blank procedure, status G, spread over week                     | 36.91%     |
|         | cases in phase |                                                                 |            |
|         | 0,1,4          |                                                                 |            |
|       7 | Tree felling   | Blank procedure, status G, spread over week, less likely Friday | 5.64%      |
|         | cases          |                                                                 |            |
|       8 | Construction   | Blank procedure, status G, spread over week, not Wednesday      | 9.62%      |
|         | cases in phase |                                                                 |            |
|         | 0              |                                                                 |            |
|       9 | Other cases in | Blank procedure + sometimes comprehensive procedure, more       | 5.21%      |
|         | phase 0,4      | likely status O, spread over week                               |            |

 
 
##    Resource Clust1 Clust2 Clust3 Clust4  Clust5 Clust6  Clust7 Clust8 Clust9 Archetypes 
## 1   1254625  1.18% 31.43% 38.23%  0.08%   5.50%  0.42%   6.00% 17.16%  0.00%     2,3,8 
## 2    560613  0.00% 39.58% 16.54%  0.00%   1.21%  0.94%   7.18% 34.56%  0.00%     2,3,8 
## 3  13412010  0.01%  0.00% 99.98%  0.00%   0.00%  0.01%   0.00%  0.00%  0.00%     3 
## 4    560504  0.03%  0.00% 99.92%  0.00%   0.00%  0.04%   0.00%  0.00%  0.00%     3 
## 5    560602  0.04% 15.27% 63.50%  2.35%   5.46%  0.57%   5.13%  0.45%  7.24%     3 
## 6  13412649  0.00%  0.00%  0.01%  0.00%   0.00% 99.99%   0.00%  0.00%  0.00%     6 
## 7    560429 11.43%  2.84%  2.44%  2.45%   4.14% 52.49%   3.56% 11.80%  8.85%     6 
## 8    560600 18.15%  0.03%  0.91%  4.74%   1.26% 60.66%   0.00% 14.26%  0.00%     6 
## 9    560604  9.60%  0.00%  0.56%  2.93%   0.00% 81.94%   1.06%  0.19%  3.72%     6 
## 10   560427  0.04%  0.00%  0.16%  0.00%   0.00%  0.00%  99.80%  0.00%  0.00%     7 
## 11   560596  0.00%  0.00%  0.00%  0.00%   0.00%  0.00% 100.00%  0.00%  0.00%     7 
## 12   560530  2.42%  0.00% 28.25%  0.00%   7.65%  0.00%  12.19%  0.00% 49.49%     3,7,9 
## 13   560532  0.00%  1.82% 32.60%  1.06%   0.00%  0.00%   9.02%  8.24% 47.26%     3,7,9 
## 14  9106499  0.00%  0.00%  0.00%  0.00%   0.00%  0.00%  30.68% 18.47% 50.85%     3,7,9 
## 15   560594  0.00%  0.00%  0.00%  0.00%  99.41%  0.59%   0.00%  0.00%  0.00%     5 
## 16   560598  0.00%  0.00%  0.00%  0.00%  98.30%  0.00%   0.00%  0.00%  1.70%     5 
## 17   560849  0.00%  0.00%  0.00%  0.00% 100.00%  0.00%   0.00%  0.00%  0.00%     5 
## 18  6925826  0.00%  0.00%  0.01%  0.00%  99.99%  0.00%   0.00%  0.00%  0.00%     5 
## 19   560608  0.00%  0.23%  0.00% 52.29%   0.00% 18.60%   5.56%  0.24% 23.09%     4,9 
## 20   560752  0.00%  1.94%  2.73%  8.90%   9.03%  0.00%   7.20% 70.20%  0.00%     8 
## 21  6993893  0.00%  0.00%  0.00% 12.90%   0.00%  0.00%   0.00% 75.55% 11.55%     8 
## 22  8492512  0.84%  0.00%  0.00%  9.02%   5.72%  0.00%   5.08% 77.48%  1.86%     8 
 
 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Clust9 Archetypes   |
|:----------------------------------------------------------------------------------------|
| ## 1 1254625 1.18% 31.43% 38.23% 0.08% 5.50% 0.42% 6.00% 17.16% 0.00% 2,3,8             |
| ## 2 560613 0.00% 39.58% 16.54% 0.00% 1.21% 0.94% 7.18% 34.56% 0.00% 2,3,8              |
| ## 3 13412010 0.01% 0.00% 99.98% 0.00% 0.00% 0.01% 0.00% 0.00% 0.00% 3                  |
| ## 4 560504 0.03% 0.00% 99.92% 0.00% 0.00% 0.04% 0.00% 0.00% 0.00% 3                    |
| ## 5 560602 0.04% 15.27% 63.50% 2.35% 5.46% 0.57% 5.13% 0.45% 7.24% 3                   |
| ## 6 13412649 0.00% 0.00% 0.01% 0.00% 0.00% 99.99% 0.00% 0.00% 0.00% 6                  |
| ## 7 560429 11.43% 2.84% 2.44% 2.45% 4.14% 52.49% 3.56% 11.80% 8.85% 6                  |
| ## 8 560600 18.15% 0.03% 0.91% 4.74% 1.26% 60.66% 0.00% 14.26% 0.00% 6                  |
| ## 9 560604 9.60% 0.00% 0.56% 2.93% 0.00% 81.94% 1.06% 0.19% 3.72% 6                    |
| ## 10 560427 0.04% 0.00% 0.16% 0.00% 0.00% 0.00% 99.80% 0.00% 0.00% 7                   |
| ## 11 560596 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 100.00% 0.00% 0.00% 7                  |
| ## 12 560530 2.42% 0.00% 28.25% 0.00% 7.65% 0.00% 12.19% 0.00% 49.49% 3,7,9             |
| ## 13 560532 0.00% 1.82% 32.60% 1.06% 0.00% 0.00% 9.02% 8.24% 47.26% 3,7,9              |
| ## 14 9106499 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 30.68% 18.47% 50.85% 3,7,9            |
| ## 15 560594 0.00% 0.00% 0.00% 0.00% 99.41% 0.59% 0.00% 0.00% 0.00% 5                   |
| ## 16 560598 0.00% 0.00% 0.00% 0.00% 98.30% 0.00% 0.00% 0.00% 1.70% 5                   |
| ## 17 560849 0.00% 0.00% 0.00% 0.00% 100.00% 0.00% 0.00% 0.00% 0.00% 5                  |
| ## 18 6925826 0.00% 0.00% 0.01% 0.00% 99.99% 0.00% 0.00% 0.00% 0.00% 5                  |
| ## 19 560608 0.00% 0.23% 0.00% 52.29% 0.00% 18.60% 5.56% 0.24% 23.09% 4,9               |
| ## 20 560752 0.00% 1.94% 2.73% 8.90% 9.03% 0.00% 7.20% 70.20% 0.00% 8                   |
| ## 21 6993893 0.00% 0.00% 0.00% 12.90% 0.00% 0.00% 0.00% 75.55% 11.55% 8                |
| ## 22 8492512 0.84% 0.00% 0.00% 9.02% 5.72% 0.00% 5.08% 77.48% 1.86% 8                  |

Specialism: 
 
 
 
   

##    Resource Clust1  Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Clust9 Specialism 
##  1 560602   63.50%  15.27% 7.24%  5.46%  5.13%  2.35%  0.57%  0.45%  0.04%  1          
##  2 1254625  38.23%  31.43% 17.16% 6.00%  5.50%  1.18%  0.42%  0.08%  0.00%  1          
##  3 560596   100.00% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  4 560849   100.00% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  5 6925826  99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  6 13412649 99.99%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  7 13412010 99.98%  0.01%  0.01%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  8 560504   99.92%  0.04%  0.03%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
##  9 560427   99.80%  0.16%  0.04%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
## 10 560594   99.41%  0.59%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
## 11 560598   98.30%  1.70%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  2          
## 12 560429   52.49%  11.80% 11.43% 8.85%  4.14%  3.56%  2.84%  2.45%  2.44%  3          
## 13 560600   60.66%  18.15% 14.26% 4.74%  1.26%  0.91%  0.03%  0.00%  0.00%  4          
## 14 560608   52.29%  23.09% 18.60% 5.56%  0.24%  0.23%  0.00%  0.00%  0.00%  4          
## 15 560530   49.49%  28.25% 12.19% 7.65%  2.42%  0.00%  0.00%  0.00%  0.00%  4          
## 16 560532   47.26%  32.60% 9.02%  8.24%  1.82%  1.06%  0.00%  0.00%  0.00%  4          
## 17 560613   39.58%  34.56% 16.54% 7.18%  1.21%  0.94%  0.00%  0.00%  0.00%  4          
## 18 560604   81.94%  9.60%  3.72%  2.93%  1.06%  0.56%  0.19%  0.00%  0.00%  5          
## 19 8492512  77.48%  9.02%  5.72%  5.08%  1.86%  0.84%  0.00%  0.00%  0.00%  5          
## 20 560752   70.20%  9.03%  8.90%  7.20%  2.73%  1.94%  0.00%  0.00%  0.00%  5          
## 21 6993893  75.55%  12.90% 11.55% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  6          
## 22 9106499  50.85%  30.68% 18.47% 0.00%  0.00%  0.00%  0.00%  0.00%  0.00%  6 
 
Specialists: clusters 2+5 (12) 
 
Combination (Profile – Specialism): 
##   Profile Archetypes `1`   `2`   `3`   `4`   `5`   `6` 
## 1 1       2,3,8       1     0     0     1     0     0 
## 2 2       3           1     2     0     0     0     0 
## 3 3       6           0     1     1     1     1     0 
## 4 4       7           0     2     0     0     0     0 
## 5 5       3,7,9       0     0     0     2     0     1 
## 6 6       5           0     4     0     0     0     0 
## 7 7       4,9         0     0     0     1     0     0 
## 8 8       8           0     0     0     0     2     1 
 

| ## Resource Clust1 Clust2 Clust3 Clust4 Clust5 Clust6 Clust7 Clust8 Clust9 Specialism   |
|:----------------------------------------------------------------------------------------|
| ## 1 560602 63.50% 15.27% 7.24% 5.46% 5.13% 2.35% 0.57% 0.45% 0.04% 1                   |
| ## 2 1254625 38.23% 31.43% 17.16% 6.00% 5.50% 1.18% 0.42% 0.08% 0.00% 1                 |
| ## 3 560596 100.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                   |
| ## 4 560849 100.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                   |
| ## 5 6925826 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                   |
| ## 6 13412649 99.99% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                  |
| ## 7 13412010 99.98% 0.01% 0.01% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                  |
| ## 8 560504 99.92% 0.04% 0.03% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                    |
| ## 9 560427 99.80% 0.16% 0.04% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                    |
| ## 10 560594 99.41% 0.59% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                   |
| ## 11 560598 98.30% 1.70% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2                   |
| ## 12 560429 52.49% 11.80% 11.43% 8.85% 4.14% 3.56% 2.84% 2.45% 2.44% 3                 |
| ## 13 560600 60.66% 18.15% 14.26% 4.74% 1.26% 0.91% 0.03% 0.00% 0.00% 4                 |
| ## 14 560608 52.29% 23.09% 18.60% 5.56% 0.24% 0.23% 0.00% 0.00% 0.00% 4                 |
| ## 15 560530 49.49% 28.25% 12.19% 7.65% 2.42% 0.00% 0.00% 0.00% 0.00% 4                 |
| ## 16 560532 47.26% 32.60% 9.02% 8.24% 1.82% 1.06% 0.00% 0.00% 0.00% 4                  |
| ## 17 560613 39.58% 34.56% 16.54% 7.18% 1.21% 0.94% 0.00% 0.00% 0.00% 4                 |
| ## 18 560604 81.94% 9.60% 3.72% 2.93% 1.06% 0.56% 0.19% 0.00% 0.00% 5                   |
| ## 19 8492512 77.48% 9.02% 5.72% 5.08% 1.86% 0.84% 0.00% 0.00% 0.00% 5                  |
| ## 20 560752 70.20% 9.03% 8.90% 7.20% 2.73% 1.94% 0.00% 0.00% 0.00% 5                   |
| ## 21 6993893 75.55% 12.90% 11.55% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 6                |
| ## 22 9106499 50.85% 30.68% 18.47% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 6                |

| ## Profile Archetypes `1` `2` `3` `4` `5` `6`   |
|:------------------------------------------------|
| ## 1 1 2,3,8 1 0 0 1 0 0                        |
| ## 2 2 3 1 2 0 0 0 0                            |
| ## 3 3 6 0 1 1 1 1 0                            |
| ## 4 4 7 0 2 0 0 0 0                            |
| ## 5 5 3,7,9 0 0 0 2 0 1                        |
| ## 6 6 5 0 4 0 0 0 0                            |
| ## 7 7 4,9 0 0 0 1 0 0                          |
| ## 8 8 8 0 0 0 0 2 1                            |