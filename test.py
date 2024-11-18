number = "523-a:!-7890"

number = (number.
          replace("(","").
          replace(")","").
          replace(".","").
          replace("-","").
          replace("+","").
          replace(" ","")
          )
print(number.find(ord('a')))
print(number)
