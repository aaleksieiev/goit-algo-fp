# Monte Carlo Simulation of Dice Throws

## Simulated Probabilities vs Theoretical Probabilities

Моделювання за методом Монте-Карло дуже точно відповідає теоретичній ймовірності викидання двох кубиків. Незначні розбіжності зумовлені випадковою природою моделювання та кінцевою кількістю кидків. Збільшення кількості кидків ще більше зменшить ці розбіжності, оскільки Закон великих чисел диктує, що змодельовані ймовірності повинні збігатися з теоретичними значеннями з більшою кількістю випробувань

    Sum  Simulated Probability  Theoretical Probability
0     2               0.027790                 0.027778
1     3               0.055221                 0.055556
2     4               0.083571                 0.083333
3     5               0.111446                 0.111111
4     6               0.138315                 0.138889
5     7               0.166156                 0.166667
6     8               0.138977                 0.138889
7     9               0.111827                 0.111111
8    10               0.083204                 0.083333
9    11               0.055828                 0.055556
10   12               0.027665                 0.027778