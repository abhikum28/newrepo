def character_count(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count


input_string = input("Enter the string you want to be checked: ")
character_to_check = input("Enter the character for which count is required: ")
char_count = character_count(input_string, character_to_check)
print(f"We got {char_count} occurance of {character_to_check} in string {input_string}")