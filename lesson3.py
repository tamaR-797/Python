


#region classs
def remove_non_alphanumeric(input_string):

  cleaned_string = ""
  for char in input_string:
    if char.isalnum():  # Checks if the character is alphanumeric (letter or number)
      cleaned_string += char
  return cleaned_string

my_string = "Hello, World! 123_abc@xyz"
cleaned_result = remove_non_alphanumeric(my_string)

print(f"Cleaned string: {cleaned_result}")

def exc2(mystr):
  newstr=mystr.split()
  max=0
  for i in newstr:
    if mystr.count(i)>max:
      max= mystr.count(i)>max
      maxsr=i
  return maxsr

print(exc2("tamar fdsjfg tamar gfdghf tamar"))


def exc3(fullname):
  newname=fullname.split()
  rt=newname[0][0]+newname[1][0]
  return rt

print(exc3("jdghjggd gfkgkfd"))
#endregion
#region homework
def analyze_list(lst) :
    numbers = set(lst)
    average = sum(lst) / len(lst)
    minimum = min(lst)
    maximum = max(lst)

    return {
      "numbers": numbers,
      "average": average,
      "minimum": minimum,
      "maximum": maximum
    }
my_list = [10, 20, 30, 20, 40, 10, 50, 50]
result = analyze_list(my_list)
print(result)


def filter_dict(d, threshold):

  high_earners = []
  for name, salary in d.items():
    if salary > threshold:
      high_earners.append(name)
  return high_earners


# Example usage
employees = {
  'tamar': 600000,
  'tovi': 750000,
  'ruti': 55000,
  'sari': 90000
}
high_earners = filter_dict(employees, 7000000)
print(f" {high_earners}")

