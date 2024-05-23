# Nesting
Capital={
  "France":"Paris",
  "India":"Delhi",
  "Russia":"Moscow",
  "United kingdom":"London",


  }



# Creating a Nested list in a dictionary
travel_log={
  "France":["Lille","Paris","Dijon"],
  "Germany":["Berlin","Hamburg","Stuttgart"],


}

# Nesting a dictionary in a dictionary

travel_log={
  "France":{"Cities_visited":["Lille","Paris","Dijon"],"Total_visits":12},
  "Germany":{"Cities_visited":["Berlin","Hamburg","Stuttgart"],"Total_expenditure":"$14587"},


}

# Nesting a dictionary in a list
travel_log
[
  { "Country":"France",
   
   "Cities_visited":["Lille","Paris","Dijon"],
   
   "Total_expenditure":"$14587",
   
   "Total_visits":"12"
  },


  { "Country":"Germany",
   
   "Cities_visited":["Berlin","Hamburg","Stuttgart"],
   
   "Total_expenditure":"$14587",
   
   "Total_visits":"6"
  }
]