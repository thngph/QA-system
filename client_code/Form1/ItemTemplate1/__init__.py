from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.answer.text = f"{self.item['answer']:>20}    ({round(self.item['score'],4):>5})"
    self.context.text = self.item['context']

    # Any code you write here will run before the form opens.