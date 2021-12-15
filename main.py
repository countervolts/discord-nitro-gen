#FFDNG (Fast & Free Discord Nitro Generator) By Countervolts
import os
import random
import string
import time
import ctypes


try:
    from discord_webhook import DiscordWebhook
except ImportError:
    install_discrod_webhook = input(
        f"Module discord_webhook not installed, do you want to install it ? [Y/n]")
    if install_discrod_webhook == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")
try:
    import requests
except ImportError:
    install_requests = input(
        f"Module requests not installed, do you want to install it ? [Y/n]")
    if install_requests == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook")



#Base Nitro Generator:
class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Countervolts")

        else:
            
            self.slowType(f'\33]0;Nitro Generator and Checker - Made by Countervolts\a', speed = .03)

        time.sleep(3)

        self.slowType("Free Fast Discord Nitro Generator V 1.0.0", .03)
        time.sleep(2)
        self.slowType("Made by Countervolts", .05)
        time.sleep(2)


        num = int(500)
				
        url = ''
        webhook = url if url != "" else None
        self.slowType(f"\nGenerating and checking {num} nitro codes now..\n", .03, newLine = False)
        
        time.sleep(2)

        valid = []
        invalid = 0

        for i in range(num):
            try:
                
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
                    
            except Exception as e:
							
                print(f" Error | {url} ")

            if os.name == "nt":
                
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Countervolts")
                print("")

            else:
                
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Countervolts\a', end='', flush=True)

        self.slowType(f"""


Here Your Results:
 Valid Nitros: {len(valid)}
 Invalid Nitros: {invalid}
 Valid Nitro Codes: {', '.join(valid )}""", speed=.03, newLine=True)
 
        url = ""
 
        hook = DiscordWebhook(url = url, content = (f"Here Your Results:\nValid Nitros: {len(valid)}\nInvalid Nitros: {invalid}"))
        
        hook.execute()

        print("Restarting the generator...")

        time.sleep(3)

        NitroGen.main(self)



    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()



    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")
    
            start = time.time()
    
            for i in range(amount):
               code = "".join(random.choices(
                   string.ascii_uppercase + string.digits + string.ascii_lowercase,
                   k = 16
                ))
    
            file.write(f"https://discord.gift/{code}\n")
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")
            

    def quickChecker(self, nitro, notify = None):
        
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)
            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Valid Nitro Code detected! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False


    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200:
                    print(f" Valid | {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Valid Nitro Code detected! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break

                else:
                    print(f" Invalid | {nitro} ")
                    invalid += 1


        return {"valid" : valid, "invalid" : invalid}


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
