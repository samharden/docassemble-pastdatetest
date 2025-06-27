from datetime import date

def date_in_past(datetocheck):
  try: 
    today = date.today()
    return datetocheck < today
  except Exception as e:
    return e