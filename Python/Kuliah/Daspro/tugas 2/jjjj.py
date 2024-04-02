
def is_palindrome(num):
    # Fungsi ini memeriksa apakah suatu bilangan adalah palindrom atau bukan
    return str(num) == str(num)[::-1]

def find_next_palindrome(input_num):
    num = input_num + 1
    while True:
        if is_palindrome(num):
            return num
        num += 1
