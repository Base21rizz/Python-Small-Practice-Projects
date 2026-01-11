from random import randint, random, choices, choice, sample
import string

# Functions


def user_id_gen_by_user(length, times):
    print("\n#Output:")
    possible_characters = string.ascii_letters + string.digits
    for i in range(times):
        print('#', end='')
        print(''.join(choices(possible_characters, k=length)))


def rgb_color_gen():
    print(f"# rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})")


def generate_hex_colors(input):
    possible_characters = 'a' + 'b' + 'c' + 'd' + 'e' + 'f' + string.digits
    for i in range(input):
        print('#', end='')
        print(''.join(choices(possible_characters, k=6)))


def generate_rgb_colors(input):
    for i in range(input):
        print(f"# rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})")


def shuffle_list(input_list):
    return sample(input_list, k=len(input_list))


# Main code
print(f"Random_User_ID: {randint(1, 10)}{choice(string.ascii_letters)}{choice(string.ascii_letters)}{randint(1, 10)}{randint(1, 10)}{choice(string.ascii_letters)}")
chs, ids = map(int, input("User Input: ").split())

user_id_gen_by_user(chs, ids)
rgb_color_gen()

hex = int(input("\nHexa colors?: "))
generate_hex_colors(hex)
rgb = int(input("\nrgb colors?: "))
generate_rgb_colors(rgb)

my_items = ['1', '2', '3', '4', '5']
new_list = shuffle_list(my_items)
print(f"Original List: {my_items}")
print(f"Shuffled List: {new_list}")
