"""
Definations of operations based on the choices of user and the judging program
"""
import fetch
import constant

constant
def queryContribution():
    return 1

constant
def queryDonation():
    return 2

def judge(choice):
    if queryContribution() == choice:
        fetch.queryContribution()
    elif queryDonation == choice:
        fetch.queryDonation()
    else :
        print("Undefined Query Type, Please Check Input Validity.")