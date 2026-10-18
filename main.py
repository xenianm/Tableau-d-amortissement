# NDINDO Xénia L3 MIASHS
# Tableau d'amortissement

# préconditions :
# periodicite in [1, 2, 4, 12]
# differe < n
# mode in ['annuités', 'amortissements', 'in fine']
# n > 0, r > 0


def tableau_annuites(c0: float, r: float, n: int, periodicite: int, differe: int, mode: str):
    
    r = r / periodicite # le taux par période
    n = n * periodicite # le nombre de période
    differe = differe * periodicite

    print(f"{'t':<4}{'Intérêt':>12}{'Amortis.':>12}{'Annuité':>12}{'Capital dû':>14}")
    tableau = []
    tableau.append([0, 0, 0, 0, c0])
    capital = c0 # le capital restant dû en fin de période


    if mode == 'annuités':

        pr = n - differe # périodes de remboursement
        a = c0 * ( (r * (1+r)**(differe) ) / (1 - (1 + r)**(-pr) ))

        for t in range(1, n + 1):
            i = r * capital

            if t <= differe:
                m = 0
                a_diff = 0
                capital = capital + i # les intérêts sont reportés à la période suivantes

            else:
                a_diff = a
                m = a_diff - i
                capital = capital - m

            tableau.append([t, i, m, a_diff, capital])

            print(f'{t:<4}{i:>12.2f}{m:>12.2f}{a_diff:>12.2f}{capital:>14.2f}')

    elif mode == 'amortissements':

        pr = n - differe #périodes pendant lesquelles on rembourse
        m = c0 / pr

        for t in range(1, n + 1):
            i = r * capital

            if t <= differe:                  # pendant la période du différé
                m_diff = 0
                a = 0
                capital = capital + i

            else:
                if differe == 0:               # il n'y avait pas de différé
                    m_diff = m
                    a = i + m_diff
                    capital = capital - m_diff
                else:                          # fin de la période de différé
                    m_diff = capital / pr
                    a = i + m_diff
                    capital = capital - m_diff

            tableau.append([t, i, m_diff, a, capital])

            print(f'{t:<4}{i:>12.2f}{m_diff:>12.2f}{a:>12.2f}{capital:>14.2f}')


    elif mode == 'in fine':

        for t in range(1, n + 1):
            i = r * capital

            if t <= differe:
                m = 0
                a = 0
                capital = capital + i

            else:
                if t < n:
                    m = 0
                    a = i
                    capital = capital
                else: # à la dernière période
                    m = capital
                    a = i + m
                    capital = capital - m

            tableau.append([t, i, m, a, capital])

            print(f'{t:<4}{i:>12.2f}{m:>12.2f}{a:>12.2f}{capital:>14.2f}')

    return tableau

# # test sans différés
# tableau_annuites(15000, 0.04, 5, 1, 0, 'annuités') # test 1
tableau_annuites(15000, 0.04, 5, 1, 0, 'amortissements') # test 2
# tableau_annuites(15000, 0.04, 5, 1, 0, 'in fine') # test 3

# # avec différés
# tableau_annuites(15000, 0.04, 5, 2, 2, 'annuités') # test 4
# tableau_annuites(15000, 0.04, 5, 4, 2, 'amortissements') # test 5
# tableau_annuites(15000, 0.04, 5, 1, 2, 'in fine') # test 6