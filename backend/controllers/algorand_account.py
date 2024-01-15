from algosdk import account

class AlgorandAccountGenerator:
    def generate_account(self):
        try:
            private_key, public_address = account.generate_account()
            print("private_key", private_key)
            print("public_address", public_address)
            
            return private_key, public_address
        except Exception as e:
            raise Exception("Failed to generate account:", str(e))

