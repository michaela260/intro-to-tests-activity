INPUT_ERROR = "The input must be a string!"
def count_a_letter(sentence, letter):
    try:
      if not letter.isalpha():
          return None
    except AttributeError:
        raise ValueError(letter, INPUT_ERROR)

    if not sentence:
        return None
    
    count = 0
    for char in sentence:
        if char == letter:
            count +=1
    
    return count
