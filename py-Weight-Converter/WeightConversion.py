from WeightObject import WeightObject

# Class to convert weights
class WeightConverter:
  def __init__(self) -> None:
    self._init_weight_dicts()


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
    message += f"Select a unit [1-{i}]: "
    return message

  # Makes the user choose in a list of weight units
  def _input_user_weight_unit(self) -> int:
    choice = int(input(self._parse_weight_dict())) - 1
    return list(self._weight_dict.items())[choice][1]


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


# Handles weight conversion by calling the necessary sub-methods
  def prepare_weight_conversion(self) -> None:
    print("======= WEIGHT TO CONVERT ========")
    weight_to_convert = self._prepare_weight_object()

    print("======= CONVERTED WEIGHT ========")
    output_unit = self._input_user_weight_unit()
    output_value = self._convert(weight_to_convert.value, weight_to_convert.unit, output_unit)

    converted_weight = WeightObject(output_value, output_unit, self._weight_dict)
    print(f"====== RESULTS ========\n{converted_weight}")
