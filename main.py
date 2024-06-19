def main():
    # Comlete your code here
    # Use m_perc, f_perc, nb_perc for your results

    m_num = int(input('Enter the number of male students:'))
    f_num = int(input('Enter the number of female students:'))
    nb_num = int(input('Enter the number of non-binary students:'))

    # Calculate the percentages

    class_size = m_num + f_num + nb_num
    m_perc = (m_num / class_size) * 100
    f_perc = (f_num / class_size) * 100
    nb_perc = (nb_num / class_size) * 100


    ########################################
    # Do not delete the return statement
    ########################################
    print(
        f'The percentage of males, females and non-binary \t {m_perc: .2f} \t {f_perc: .2f} \t {nb_perc: .2f}')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()
