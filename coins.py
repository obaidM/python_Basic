
import random


class Coin:
       def __init__(self, rare= False, clean = True, **kwargs):

           for  key,value in kwargs.items():
                setattr(self,key,value)

           self.is_rare = rare
           self.is_clean = clean

           if self.is_rare == True:
              self.value = self.original_value *1.25
           else:
              self.value = self.original_value

           if self.is_clean == True:
              self.color = self.original_color
           else:
               self.color = self.rusty_color

       def rust(self):
            self.color = self.rusty_color

       def clean(self):
           self.color = self.clean_color

       def flip(self):
          heads_option = [True, False]
          choice = random.choice(heads_option)
          self.heads = choice

       def __del__(self):
            print("Coin Spent")


class Pound(Coin):
  def __init__(self):
      data={
          "original_value": 1.00,
          "clean_color": "gold",
          "rusty_color": "greenish",
          "num_edges": 1,
           "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
          }
      super().__init__(**data)

    
            
        
class one_pence(Coin):
  def __init__(self):
      data={
          "original_value": 0.01,
          "clean_color": "bronze",
          "rusty_color": "brownish",
          "num_edges": 1,
           "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
          }
      super().__init__(**data)
    

class two_pence(Coin):
  def __init__(self):
      data={
          "original_value": 0.02,
          "clean_color": "bronze",
          "rusty_color": "brownish",
          "num_edges": 1,
           "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
          }
      super().__init__(**data) 


class five_pence(Coin):
  def __init__(self):
      data={
          "original_value": 0.05,
          "clean_color": "silver",
          "rusty_color": None,
          "num_edges": 1,
           "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
          }
      super().__init__(**data)

      def rust(self):
            self.color = "silver"

class ten_pence(Coin):
  def __init__(self):
      data={
          "original_value": 0.1,
          "clean_color": "silver",
          "rusty_color": None,
          "num_edges": 1,
           "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
          }
      super().__init__(**data)

      def rust(self):
            self.color = "silver"

