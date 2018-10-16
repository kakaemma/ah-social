import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = "Kel08xM3PPXMpuAkXU2CmGNAb"
credentials['CONSUMER_SECRET'] = "YbQMuZg2Bg22s0Ct0CJTaTe2Eop2xopNWiLrIlpj8IJkpcRSEZ"
credentials['ACCESS_TOKEN'] ="1050020587203125248-TpDsgXR2BSVESMMdVopVSOEsfZN2b5"
credentials['ACCESS_SECRET'] ="4EhlZ0eerlGSkeUbmV6XsH1MyD4MAbJWTrWRv3vqN5uGQ"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)