import xml.etree.ElementTree as ET

def calculate_area(filename):
  """
  Calculates the area of a rectangle from a draw.io diagram.

  Args:
    filename: The path to the .drawio file.

  Returns:
    The area of the rectangle, or None if not found.
  """
  tree = ET.parse(filename)
  root = tree.getroot()

  length = None
  width = None

  # Find the rectangle element and extract length and width
  for element in root.iter('object'):  # Iterate over <object> tags
    #if element.get('id') == 'yZ6IWgLvp9_E0ZAu5OOj-1': # Find the specific rectangle by its ID
      length = float(element.get('length')) if element.get('length') else None
      width = float(element.get('width')) if element.get('width') else None
      break

  # Calculate the area
  if length is not None and width is not None:
    area = length * width
    print(f"The area of the rectangle is: {area}")
    return area
  else:
    print("Could not find rectangle dimensions in the diagram.")
    return None

# Example usage
filename = r"C:\Users\daf\Downloads\Untitled Diagram (1).drawio"  # Replace with your filename
calculate_area(filename)
