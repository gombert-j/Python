from classes.WeightObject import WeightObject

# Class to convert weights
class WeightConverter:
  def __init__(self) -> None:
    self._init_weight_dicts()


# Handles weight conversion by calling the necessary sub-methods
  def prepare_weight_conversion(self) -> None:
    print("======= WEIGHT TO CONVERT ========")
    weight_to_convert = self._prepare_weight_object()

    print("======= CONVERTED WEIGHT ========")
    output_unit = self._input_user_weight_unit()
    output_value = self._convert(weight_to_convert.value, weight_to_convert.unit, output_unit)

    converted_weight = WeightObject(output_value, output_unit, self._weight_dict)
    print(f"====== RESULTS ========\n{converted_weight}")


  # Conversion dictionary of different weight units
  def _init_weight_dicts(self) -> None:
    self._weight_dict = {
      "t" : 1000000,
      "kg" : 1000,
      "g": 1,
      "mg": 1/1000,
      "μg": 1/1000000,
      "lbs": 453.59237
    }


  # Parses the weight units dictionary for user choice
  def _parse_weight_dict(self) -> str:
    message : str = ""
    i : int = 0
    for key, value in self._weight_dict.items():
      i += 1
      message += f"[{i}] {key}\n"
    message += f"Select a unit: "
    return message


  # Makes the user choose in a list of weight units (Outputs the value of the unit(e.g: kg = 1000))
  def _input_user_weight_unit(self) -> float:
    # Asks the user to input a weight unit until a valid one is chosen
    choice = None
    while self._verify_user_weight_unit(choice) == False:
      choice = input(self._parse_weight_dict())

    # Try to make choice an int and decrease by 1 (since the dict can be converted into a list
    # and a list starts with 0,  but the user's choice is > 1)
    try:
      choice = int(choice) - 1

    # When the attempt to make a float fails, then it's likely because choice is a string
    except:
      # If the user's choise is a string (in that case, formatted version of the unit, e.g: kg) 
      if isinstance(choice, str):
        choice = choice.lower()
        choice = self._find_weight_unit_index_from_formatted_unit(choice)

    # Return the weight unit's value
    return list(self._weight_dict.items())[choice][1]


  # Find the weight unit value index (e.g: '2') from a unit format (e.g.: kg)
  def _find_weight_unit_index_from_formatted_unit(self, formatted_unit : str) -> float:
    # Find the right unit
    index = list(self._weight_dict.keys()).index(formatted_unit)
    # Find the index
    return index


  # Make sure the user's chosen weight unit fits the dictionary of units
  def _verify_user_weight_unit(self, test_unit) -> bool:
    # Try to turn the test unit into an int and checks if it's between the minimum and the maximum the user can choose
    try:
      test_unit = int(test_unit)
      if (test_unit >= 1) and (test_unit <= len(self._weight_dict)):
        return True

    # If that's not the case (most likely a string)
    except:
      for key, value in self._weight_dict.items():
        try:  
          if test_unit.lower() == key:
            return True
        except:
          pass
      return False


  # Makes the user input a weight
  def _input_user_weight_value(self) -> float:
    choice : float = input("Select a weight: ")
    return choice


  # Creates a WeightObject, containing a value, and a unit
  def _prepare_weight_object(self) -> WeightObject:
    unit = self._input_user_weight_unit()
    value = self._input_user_weight_value()
    return WeightObject(value, unit, self._weight_dict)


  # Converts a weight from one unit to another
  def _convert(self, input_value : float, input_unit : float, output_unit : float) -> float:
    return float(input_value) * (input_unit / output_unit)
