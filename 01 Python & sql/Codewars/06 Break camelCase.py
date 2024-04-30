# Break camelCase :

'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""


'''

def break_camel_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result.strip()  # Remove any leading/trailing spaces

# Example usage:
print(break_camel_case("camelCasing"))  # Output: "camel Casing"
print(break_camel_case("identifier"))   # Output: "identifier"
print(break_camel_case(""))             # Output: ""