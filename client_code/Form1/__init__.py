from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.warning.visible = False

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  
  def outlined_button_1_click(self, **event_args):
    
    self.warning.visible = False
    self.Context.visible=False
    self.Answer.visible=False
    self.best_answer.visible=False
    self.timer.visible = False
    self.context.visible = False
    
    self.info.text = "Processing your question, please wait. This process should be appx. 1 minute."
    self.info.visible = True
    
    
    query = self.question.text
    
    try:
      ner = anvil.server.call('ner', query)
      print(ner)
      elastic_contexts, retrieve_time = anvil.server.call('elastic', query, ner, 200)
      contexts, cross_time = anvil.server.call('retrieve', 
                                                query, 
                                                elastic_contexts,
                                                10,
                                                True)
      answers, candidates, read_time = anvil.server.call('read', query, contexts)
      self.context.items = candidates
      ans_list = '\n'.join(list(set([answer['answer'] for answer in answers])))
      self.best_answer.text = f"A: {ans_list}"
      self.timer.text = f"Elapsed time: {retrieve_time + cross_time + read_time :.2f}s"
      self.info.visible = False
      self.timer.visible = True
      self.Context.visible=True
      self.Answer.visible=True
      self.best_answer.visible=True
      self.context.visible = True
      
    except:
      self.warning.visible = True



  

