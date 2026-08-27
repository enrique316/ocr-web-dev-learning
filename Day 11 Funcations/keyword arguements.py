# **kwargs what is keywords arguments #
def collect(**info):
    print(info)
collect(name="shuhankar" , amount=7000 )

def data (**check):
    print(check)
collect(invoice= "Algo1234", Amount=700000)
#-----#

def data(**x):
    print(x)

data (
    invoice_number= "inv123",
    date = "30-3-1988",
    amount = 7000
)
