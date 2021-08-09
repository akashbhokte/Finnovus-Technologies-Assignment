# Import Module
import pdftables_api

# API KEY VERIFICATION
conversion = pdftables_api.Client('srmylo4nu0z0')
  
# PDf to Excel 
# (Hello.pdf, Hello)
conversion.csv("assignment.pdf", "out2.csv")
