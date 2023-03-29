import base64
from http import client
import json 
import numpy as np
import requests

class SAI:
    def __init__(self):
        self.code_ver = ''
        self.code_chall = ''
        # hard coded for testing but will not be permantly
        self.end_point = ''
        self.clientID = 'a9dead9b7824450eb62344a7eeb7df2f'
        

    # generates random string for code verifier
    def gen_code_ver(self):
        # acts as bank of characters fo code verifier
        str_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4',
                    '5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','S']
        
        # biulds code verifier
        for i in range(0,20):
            self.code_ver += str_list[np.random.randint(0,int(len(str_list)))]
        
        
    
    
       
        
    # encodes code challenge
    def encode_ver(self):
        self.code_chall = base64.urlsafe_b64decode(self.code_ver)


    
    def send_req(self):
        data_json = {
            'client_id' : self.clientID,
            'respone_type' : 'code',
            'redirect_uri' : 'https://localhost:8888/callback',
            'code_challenge_method' : 'S256',
            'code_challenge' : self.code_chall
        }

        resp = requests.get(self.end_point, data= data_json)
        data = resp.json()

        return data


s = SAI()
print(s.send_req())

