def ask_count_num():
    while True:
        try:
            numbercount = int(input("che tedad adad ra mikhahid ba ham jam konid? "))
            if numbercount <= 0:
                raise AssertionError
            break
        except AssertionError:
            print("adad balatar az 0 vared konid.")
    total_sum = 0
    for i in range(numbercount):
        number = int(input(f"adad {i+1} ra vared konid: "))
        total_sum += number

    print(f"majmo adad barabar ba {total_sum} mibashad.")

    return

ask_count_num()
