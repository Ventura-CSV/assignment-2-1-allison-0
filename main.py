def main():
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################

    m_perc = int(input('Enter the amount of male students:'))
    f_perc = int(input'"Enter the amount of female students:)')
    nb_perc = int(input('Enter the amount of non-binary students:'))



    ########################################
    # Do not delete the return statement
    ########################################
    print(
        f'The percentage of males, females and non-binary \t {m_perc: .2f} \t {f_perc: .2f} \t {nb_perc: .2f}')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()
