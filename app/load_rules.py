def getCustomRules():
  contents = ''
  custom_rules = {}

  #split rules into an array
  with open('./app/house_rules.txt') as file:
    contents = file.read()

  contents = contents.split("\n")

  for rule in contents:
    data = rule.split(":")
    custom_rules[data[0]] = data[1]

  return custom_rules