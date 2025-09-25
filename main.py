def str_to_digits(s, base):
    return [int(ch, base) for ch in s.upper()]

def digits_to_str(digits, base):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(chars[d] for d in digits)

def remove_leading_zeros(digits):
    while len(digits) > 1 and digits[0] == 0:
        digits.pop(0)
    return digits

def add_digits(a, b, base):
    a, b = a[::-1], b[::-1]
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    carry = 0
    result = []
    for i in range(max_len):
        s = a[i] + b[i] + carry
        result.append(s % base)
        carry = s // base
    if carry:
        result.append(carry)
    return result[::-1]

def sub_digits(a, b, base):
    a, b = a[::-1], b[::-1]
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    borrow = 0
    result = []
    for i in range(max_len):
        s = a[i] - b[i] - borrow
        if s < 0:
            s += base
            borrow = 1
        else:
            borrow = 0
        result.append(s)
    return remove_leading_zeros(result[::-1])

def mul_digits(a, b, base):
    a, b = a[::-1], b[::-1]
    result = [0] * (len(a) + len(b))
    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            total = result[i + j] + a[i] * b[j] + carry
            result[i + j] = total % base
            carry = total // base
        result[i + len(b)] += carry
    return remove_leading_zeros(result[::-1])

def compare_digits(a, b):
    a = remove_leading_zeros(a[:])
    b = remove_leading_zeros(b[:])
    if len(a) != len(b):
        return len(a) - len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return a[i] - b[i]
    return 0



def convert_base(digits, base_from, base_to):
    """Converte uma lista de dígitos da base_from para base_to sem usar base decimal."""
    number = digits[:]
    result = []

    while compare_digits(number, [0]) > 0:
        quotient = []
        remainder = 0
        for d in number:
            acc = remainder * base_from + d
            quotient.append(acc // base_to)
            remainder = acc % base_to
        result.append(remainder)
        number = remove_leading_zeros(quotient)
    return result[::-1] if result else [0]

def main():
    base1 = int(input("Base do primeiro valor: "))
    valor1 = input("Primeiro valor: ")
    base2 = int(input("Base do segundo valor: "))
    valor2 = input("Segundo valor: ")
    operacao = input("Operação (+, -, *, /): ")
    base_result = int(input("Base do resultado: "))

    digits1 = str_to_digits(valor1, base1)
    digits2 = str_to_digits(valor2, base2)

    # Convert both numbers to same base before operation — choose base1
    if operacao == '+':
        # Convert digits2 to base1
        digits2_base1 = convert_base(digits2, base2, base1)
        result_digits = add_digits(digits1, digits2_base1, base1)
    elif operacao == '-':
        digits2_base1 = convert_base(digits2, base2, base1)
        result_digits = sub_digits(digits1, digits2_base1, base1)
    elif operacao == '*':
        digits2_base1 = convert_base(digits2, base2, base1)
        result_digits = mul_digits(digits1, digits2_base1, base1)
    elif operacao == '/':
        digits2_base1 = convert_base(digits2, base2, base1)
        result_digits = div_digits(digits1, digits2_base1, base1)
    else:
        print("Operação inválida.")
        return

    # Convert result to base_result
    result_converted = convert_base(result_digits, base1, base_result)
    result_str = digits_to_str(result_converted, base_result)

    print(f"Resultado: {result_str} (base {base_result})")

if __name__ == "__main__":
    main()
