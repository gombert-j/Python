# Class to contain a weight
class WeightObject:
  # Constructor: Sets the value, the unit and the units dictionary
  def __init__(self, value, unit, unit_dicts) -> None:
    self.value : float = value
    self.unit : int = unit

    # The dictionary is used when formatting the unit in self.get_formatted_unit()
    self.dicts : dict = unit_dicts
    

  # Formats a message for when the object is printed
  def __str__(self) -> str:
    formatted_unit = self.get_formatted_unit()

    message : str = f"\033[1m{self.value:.3f}\033[0m{formatted_unit}"
    return message


  # Checks the dictionary for the current format of the weight unit
  def get_formatted_unit(self) -> str:
    for key, value in self.dicts.items():
      if value == self.unit:
        return key
