def one_digit_mul(x, y):
    if len(str(x)) != 1 or len(str(y)) != 1:
        raise ValueError("Attempted to multiply numbers with more than one digits")
    return str(int(x) * int(y))


def add(x, y):
    return str(int(x) + int(y))


def subtract(x, y):
    return str(int(x) - int(y))


def mul_by_pow_of_10(x, n):
    return x + "0" * n


def karatsuba_mul(x, y):
    # print(f"Called K_Mul with numbers {x, y}", end="\n\n")

    if len(x) == 1 and len(y) == 1:
        result = one_digit_mul(x, y)
        # print(f"Called K_Mul with numbers {x, y}", end="\t")
        # print(f"Result: {result}", end="\n\n")
        return result
    else:
        len_x = len(x)
        len_y = len(y)

        if len_x == len_y - 1:
            x = "0" + x
            len_x += 1

        if len_y == len_x - 1:
            y = "0" + y
            len_y += 1

        # print(f"x: {x}, y: {y}")
        a, b = x[:len_x // 2], x[len_x // 2:]
        c, d = y[:len_y // 2], y[len_y // 2:]

        ac = karatsuba_mul(a, c)
        bd = karatsuba_mul(b, d)
        apb_cpd = karatsuba_mul(add(a, b), add(c, d))

        ad_p_bc = subtract(
            subtract(apb_cpd, ac), bd
        )

        part_1 = mul_by_pow_of_10(ac, len_x - (len_x // 2) + len_x - (len_x // 2))
        part_2 = mul_by_pow_of_10(ad_p_bc, len_x - (len_x // 2))
        part_3 = bd

        result = add(
            add(
                part_1, part_2
            ), part_3)
        # print(f"Called K_Mul with numbers {x, y}", end="\t")
        # print(f"Result: {result}", end="\n\n")

    return result


def main():
    # Numbers are treated as strings intentionally, as to restrict the program to use the custom multiplication
    # and not the python default multiplication (which is efficient by default)
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"

    karatsuba_result = karatsuba_mul(x, y)
    correct_result = str(int(x) * int(y))

    if karatsuba_result == correct_result:
        print(f"result: {karatsuba_result}")
        print("Karatsuba Multiplication executed correctly!")
    else:
        print("Karatsuba Multiplication did not execute correctly!!")
        print(f"karatsuba result: {karatsuba_result}")
        print(f"correct result: {correct_result}")


if __name__ == '__main__':
    main()
